from telemetry import telemetry_stream, logger, trace_abnormal

LAST_NAME = "MENDOZA"
SEED_NUM = 0
FAVORITE_ARTIST = "SYD HARTHA"

filter_valid = lambda x: isinstance(x, (int, float))

@logger
def process_pipeline():
    count = len(LAST_NAME) + SEED_NUM + 3
    seed = sum(ord(c) for c in FAVORITE_ARTIST) % 20 + 1

    valid, invalid, abnormal = [], [], []

    for reading in telemetry_stream(count, seed):
        try:
            if not filter_valid(reading):
                raise ValueError("Non-numeric reading")
            valid.append(reading)
            if reading > 70:
                abnormal.append(reading)
        except ValueError:
            invalid.append(reading)

    print(f"Student Inputs: {LAST_NAME}, {SEED_NUM}, {FAVORITE_ARTIST}")
    print(f"Processed Readings: {count}")
    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")
    print(f"Abnormal Conditions: {abnormal}")

    if abnormal:
        depth = trace_abnormal(abnormal[0])
        print(f"Recursive Analysis Depth for {abnormal[0]}: {depth}")

    status = "CRITICAL" if abnormal else "NORMAL"
    print(f"Overall Equipment Status: {status}")

process_pipeline()