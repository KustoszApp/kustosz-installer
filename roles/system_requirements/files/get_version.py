#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.request
from datetime import datetime

LATEST_STR = "latest"
gh_date_format = "%Y-%m-%dT%H:%M:%SZ"


def get_release_date(release_obj):
    date_str = release_obj.get("published_at")
    return datetime.strptime(date_str, gh_date_format)


def main():
    parser = argparse.ArgumentParser(
        description="Get Kustosz component version from GitHub API"
    )
    parser.add_argument("--component")
    parser.add_argument("--version", nargs='?', default=LATEST_STR)

    args = parser.parse_args()

    if args.version != LATEST_STR:
        print(args.version)
        return

    url = f"https://api.github.com/repos/KustoszApp/{args.component}/releases"

    req = urllib.request.Request(
        url=url,
        headers={
            "Accept": "application/vnd.github.v3+json",
        },
    )
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            sys.exit(1)
        data = json.load(response)

    latest_release = data[0]
    for release in data:
        latest_release_dt = get_release_date(latest_release)
        this_release_dt = get_release_date(release)
        if this_release_dt > latest_release_dt:
            latest_release = release

    print(latest_release.get('tag_name'))


if __name__ == "__main__":
    main()
