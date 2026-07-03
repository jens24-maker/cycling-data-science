import csv

def load_data(path):
    data = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "date": row["date"],
                "hrv": float(row["hrv"]),
                "rhr": float(row["rhr"]),
                "sleep": float(row["sleep"])
            })
    return data

def average(values):
    return sum(values) / len(values)

def flag_low_hrv(data, threshold_percent=15):
    hrv_values = [day["hrv"] for day in data]
    hrv_avg = average(hrv_values)
    flagged = []
    for day in data:
        drop_percent = (hrv_avg - day["hrv"]) / hrv_avg * 100
        if drop_percent >= threshold_percent:
            flagged.append(day["date"])
    return flagged

if __name__ == "__main__":
    data = load_data("data/readiness_log.csv")

    hrv_values = [day["hrv"] for day in data]
    rhr_values = [day["rhr"] for day in data]
    sleep_values = [day["sleep"] for day in data]

    hrv_avg = average(hrv_values)
    print(f"HRV average used for comparison: {hrv_avg:.1f}")
    for day in data:
        drop = (hrv_avg - day["hrv"]) / hrv_avg * 100
        print(f"{day['date']}: HRV {day['hrv']}, drop {drop:.1f}%")

    print(f"HRV average: {average(hrv_values):.1f}")
    print(f"RHR average: {average(rhr_values):.1f}")
    print(f"Sleep average: {average(sleep_values):.1f}h")

    flagged_days = flag_low_hrv(data)
    print(f"Days with HRV drop >=15%: {flagged_days}")