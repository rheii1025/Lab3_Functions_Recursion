# telemetry.py
def telemetry_stream(count, seed):
    for i in range(count):
        yield (seed * (i + 1)) % 100 if i != 2 else "BAD"  # inject one bad value

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def trace_abnormal(value, depth=0):
    if value <= 1:
        return depth
    return trace_abnormal(value // 2, depth + 1)