"""
Parse an Apple Health export.xml file and extract daily HRV, resting heart
rate (RHR), and sleep duration, using only the Zepp (Amazfit) data source
for consistency with the athlete's primary tracking device.

Apple Health exports can contain multiple overlapping data sources (e.g. an
old sleep-tracking app, a second heart-rate app, or a previous phone owner's
synced data). Mixing sources leads to inconsistent readings, so this script
filters everything down to a single trusted source before aggregating.

Usage:
    python scripts/parse_health_export.py
"""

import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime

INPUT_PATH = "data/raw/Export.xml"
OUTPUT_PATH = "data/health_history.csv"

TRUSTED_SOURCE = "Zepp"

HRV_TYPE = "HKQuantityTypeIdentifierHeartRateVariabilitySDNN"
RHR_TYPE = "HKQuantityTypeIdentifierRestingHeartRate"
SLEEP_TYPE = "HKCategoryTypeIdentifierSleepAnalysis"
# Zepp writes both individual sleep-stage segments (Core/Deep/REM) AND a
# separate "InBed" summary record spanning the whole night. Only count
# actual asleep-stage values, otherwise the InBed summary double-counts
# on top of the stage segments and roughly doubles the total.
SLEEP_ASLEEP_PREFIX = "HKCategoryValueSleepAnalysisAsleep"

# Physiologically plausible ranges, used to drop obvious sensor glitches.
HRV_RANGE = (5, 300)      # ms
RHR_RANGE = (30, 120)     # bpm
SLEEP_RANGE = (0, 16)     # hours per night


def parse_date(date_str):
    # Apple Health dates look like "2026-07-03 04:54:00 +0200"
    return datetime.strptime(date_str[:19], "%Y-%m-%d %H:%M:%S")


def parse_health_export(path):
    hrv_by_day = defaultdict(list)
    rhr_by_day = defaultdict(list)
    sleep_seconds_by_day = defaultdict(float)

    # iterparse streams the file instead of loading it fully into memory,
    # important here since the export is hundreds of MB.
    context = ET.iterparse(path, events=("start", "end"))

    for event, elem in context:
        if event == "end" and elem.tag == "Record":
            record_type = elem.get("type")
            source = elem.get("sourceName")

            if source != TRUSTED_SOURCE:
                elem.clear()
                continue

            if record_type == HRV_TYPE:
                day = parse_date(elem.get("startDate")).date()
                hrv_by_day[day].append(float(elem.get("value")))

            elif record_type == RHR_TYPE:
                day = parse_date(elem.get("startDate")).date()
                rhr_by_day[day].append(float(elem.get("value")))

            elif record_type == SLEEP_TYPE:
                value = elem.get("value")
                if not value.startswith(SLEEP_ASLEEP_PREFIX):
                    elem.clear()
                    continue
                start = parse_date(elem.get("startDate"))
                end = parse_date(elem.get("endDate"))
                # Assign the sleep segment to the wake-up date, matching how
                # the daily check-in logs "last night's sleep" each morning.
                day = end.date()
                sleep_seconds_by_day[day] += (end - start).total_seconds()

            elem.clear()

    return hrv_by_day, rhr_by_day, sleep_seconds_by_day


def average(values):
    return sum(values) / len(values)


def in_range(value, value_range):
    return value_range[0] <= value <= value_range[1]


def build_daily_table(hrv_by_day, rhr_by_day, sleep_seconds_by_day):
    all_days = set(hrv_by_day) | set(rhr_by_day) | set(sleep_seconds_by_day)
    rows = []

    for day in sorted(all_days):
        hrv = average(hrv_by_day[day]) if day in hrv_by_day else None
        rhr = average(rhr_by_day[day]) if day in rhr_by_day else None
        sleep_hours = (
            sleep_seconds_by_day[day] / 3600 if day in sleep_seconds_by_day else None
        )

        if hrv is not None and not in_range(hrv, HRV_RANGE):
            hrv = None
        if rhr is not None and not in_range(rhr, RHR_RANGE):
            rhr = None
        if sleep_hours is not None and not in_range(sleep_hours, SLEEP_RANGE):
            sleep_hours = None

        rows.append(
            {
                "date": day.isoformat(),
                "hrv": round(hrv, 1) if hrv is not None else "",
                "rhr": round(rhr, 1) if rhr is not None else "",
                "sleep": round(sleep_hours, 2) if sleep_hours is not None else "",
            }
        )

    return rows


def write_csv(rows, path):
    with open(path, "w") as f:
        f.write("date,hrv,rhr,sleep\n")
        for row in rows:
            f.write(f"{row['date']},{row['hrv']},{row['rhr']},{row['sleep']}\n")


if __name__ == "__main__":
    print(f"Parsing {INPUT_PATH} (this can take a minute for large exports)...")
    hrv_by_day, rhr_by_day, sleep_seconds_by_day = parse_health_export(INPUT_PATH)

    print(f"Days with HRV data: {len(hrv_by_day)}")
    print(f"Days with RHR data: {len(rhr_by_day)}")
    print(f"Days with sleep data: {len(sleep_seconds_by_day)}")

    rows = build_daily_table(hrv_by_day, rhr_by_day, sleep_seconds_by_day)
    write_csv(rows, OUTPUT_PATH)

    print(f"Wrote {len(rows)} daily rows to {OUTPUT_PATH}")
