def open_log(file_path):
    try:
        return open(file_path, "w", encoding="utf-8")
    except PermissionError:
        print("Could not open log file in write mode: permission denied.")

        return open(file_path, "r", encoding="utf-8")


def write_log(log, content):
    hasWritable = hasattr(log, 'writable') and callable(log.writable)

    if hasWritable and log.writable():
        log.write(content)