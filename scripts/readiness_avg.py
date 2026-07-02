readiness_log = [
    {"date": "2026-06-28", "hrv": 97, "rhr": 48, "sleep_duration": 8.5},
    {"date": "2026-06-29", "hrv": 95, "rhr": 49, "sleep_duration": 7.0},
    {"date": "2026-06-30", "hrv": 100, "rhr": 47, "sleep_duration": 9.0},
    {"date": "2026-07-01", "hrv": 96, "rhr": 48, "sleep_duration": 8.0},
]


def average(values):
    return sum(values) / len(values)

def flag_data(log):
    return [day["date"] for day in log if day["hrv"] < 80 or day["rhr"] > 49 or day["sleep_duration"] < 7.5]

hrv_values = [day["hrv"] for day in readiness_log]
rhr_values = [day["rhr"] for day in readiness_log]
sleep_values = [day["sleep_duration"] for day in readiness_log]

print(f"Average HRV: {average(hrv_values):.1f}")
print(f"Average RHR: {average(rhr_values):.1f}")
print(f"Average sleep: {average(sleep_values):.1f}h")

print(f"Days with elevated data: {flag_data(readiness_log)}")