def open_log(log_path):
    try:
        print(f"Opening log as write mode in {log_path}")

        return open(log_path, "w", encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found. Creating new log in {log_path}")

        return open(log_path, "x", encoding="utf-8")
    except PermissionError:
        print("Could not open log file in write mode: permission denied.")

        return open(log_path, "r", encoding="utf-8")


def write_log(log, content):
    hasWritable = hasattr(log, 'writable') and callable(log.writable)

    if hasWritable and log.writable():
        log.write(f"{content}\n")