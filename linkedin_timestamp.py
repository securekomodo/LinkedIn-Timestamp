#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
import datetime


def get_post_id(url):
    """
    Extracts the post ID from a given LinkedIn URL.

    Args:
    - url (str): The LinkedIn post URL.

    Returns:
    - str: The extracted post ID, or None if not found.
    """
    regex = r"activity-([0-9]+)"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None


def extract_unix_timestamp(post_id):
    """
    Converts a given post ID into a UNIX timestamp.

    Args:
    - post_id (str): The LinkedIn post ID.

    Returns:
    - int: The extracted UNIX timestamp.
    """
    as_binary = format(int(post_id), "064b")
    first42_chars = as_binary[:42]
    timestamp = int(first42_chars, 2)
    return timestamp


def unix_timestamp_to_human_date(timestamp):
    """
    Converts a UNIX timestamp to a human-readable UTC date format.

    Args:
    - timestamp (int): The UNIX timestamp.

    Returns:
    - str: The human-readable UTC date.
    """
    date_object = datetime.datetime.utcfromtimestamp(timestamp / 1000)
    human_date_format = date_object.strftime("%a, %d %b %Y %H:%M:%S (UTC)")
    return human_date_format


def get_date(url):
    """
    Fetches the date of a given LinkedIn post URL.

    Args:
    - url (str): The LinkedIn post URL.

    Returns:
    - str: The post's date in human-readable format, or None if not found.
    """
    post_id = get_post_id(url)
    if post_id:
        unix_timestamp = extract_unix_timestamp(post_id)
        human_date_format = unix_timestamp_to_human_date(unix_timestamp)
        return human_date_format
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract the date from a LinkedIn post URL.")
    parser.add_argument("url", help="LinkedIn post URL")
    args = parser.parse_args()

    date = get_date(args.url)
    if date:
        print(f"Date: {date}")
    else:
        print("No valid post ID found in the provided URL.")
