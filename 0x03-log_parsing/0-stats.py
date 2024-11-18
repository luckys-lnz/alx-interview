#!/usr/bin/python3
'''Script to read stdin line by line and compute metrics.'''
import sys

# Possible status codes
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}


def print_statistics(total_file_size, status_code_counts):
    '''Print the current statistics.

    Args:
        total_file_size (int): Cumulative total of file sizes.
        status_code_counts (dict): Dictionary with status code counts.
    '''
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def parse_log_line(line):
    '''Parse a log line and extract the status code and file size.

    Args:
        line (str): A single log line.

    Returns:
        tuple: A tuple containing the status code and file size, or (None, 0)
        if the line is invalid.
    '''
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, 0
        status_code = parts[-2]
        file_size = int(parts[-1])
        if status_code in VALID_STATUS_CODES:
            return status_code, file_size
    except (ValueError, IndexError):
        pass
    return None, 0


def main():
    '''Main function to read and process stdin.'''
    total_file_size = 0
    status_code_counts = {code: 0 for code in VALID_STATUS_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line.strip())
            if status_code:
                status_code_counts[status_code] += 1
            total_file_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        raise

    print_statistics(total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
