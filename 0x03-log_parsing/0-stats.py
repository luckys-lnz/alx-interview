#!/usr/bin/python3
'''A professional-grade script for parsing HTTP request logs and computing
metrics.
'''
import re
import sys
from typing import Dict

# Precompiled regex pattern for log parsing
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+)\s*'
    r'-\s*\[(?P<date>[^\]]+)\]\s*'
    r'"(?P<request>[^"]+)"\s*'
    r'(?P<status_code>\d{3})\s*'
    r'(?P<file_size>\d+)'
)

# Valid HTTP status codes for tracking
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}


def extract_input(input_line: str) -> Dict[str, int]:
    '''Extracts the status code and file size from a line of an HTTP request
    log.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        Dict[str, int]: A dictionary containing the extracted status code and
        file size.
    '''
    match = LOG_PATTERN.match(input_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        if status_code in VALID_STATUS_CODES:
            return {'status_code': status_code, 'file_size': file_size}
    return {'status_code': '0', 'file_size': 0}


def print_statistics(total_file_size: int,
                     status_codes_stats: Dict[str, int]) -> None:
    '''Prints the accumulated statistics of the HTTP request logs.

    Args:
        total_file_size (int): The total file size accumulated.
        status_codes_stats (Dict[str, int]): A dictionary mapping status codes
        to their occurrences.
    '''
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}')


def update_metrics(line: str,
                   total_file_size: int,
                   status_codes_stats: Dict[str, int]) -> int:
    '''Updates the total file size and status code statistics from a log line.

    Args:
        line (str): A single log line.
        total_file_size (int): The current total file size.
        status_codes_stats (Dict[str, int]): The dictionary to update with
        status code counts.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run() -> None:
    '''Runs the log parser, reading from stdin and printing metrics every
    10 lines.
    '''
    line_count = 0
    total_file_size = 0
    status_codes_stats = {code: 0 for code in VALID_STATUS_CODES}

    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line.strip(), total_file_size, status_codes_stats)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        sys.exit(0)


if __name__ == '__main__':
    run()
