#!/usr/bin/python3
"""
_summary_
"""

import sys
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def signal_handler(sig, frame):
    """_summary_

    Args:
        sig (_type_): _description_
        frame (_type_): _description_
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """_summary_
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


signal.signal(signal.SIGINT, signal_handler)
for line in sys.stdin:
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])
        total_file_size += file_size
        if (status_code in [str(a) for a in status_code_counts.keys()]):
            status_code_counts[int(status_code)] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

    except (IndexError, ValueError):
        continue

print_stats()
