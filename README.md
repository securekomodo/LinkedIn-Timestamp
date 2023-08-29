# LinkedIn Timestamp Tool

LinkedIn Timestamp Tool is a Python script that extracts the exact date and time a LinkedIn post was created from its URL. This information is valuable for Open Source Intelligence (OSINT) investigations and penetration testing scenarios.

## Problem Statement

LinkedIn displays the relative date of a post, such as "3 days ago" or "4 months ago", making it difficult to correlate events, analyze activity patterns, or build a temporal profile of a target. This tool addresses this challenge by providing the exact date and time a post was created.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/securekomodo/linkedin-timestamp.git
```

2. Change into the cloned directory:

```bash
cd linkedin-timestamp
```

## Usage

To use the LinkedIn Timestamp Tool, run the following command, providing the LinkedIn post URL as an argument:

```bash
python linkedin_timestampl.py "https://www.linkedin.com/posts/activity-XXXXXXXXXXXXXXXXXXX/"
```

Replace `XXXXXXXXXXXXXXXXXXX` with the actual post ID.

## Example

```bash
python linkedin_timestamp_tool.py "https://www.linkedin.com/posts/activity-7059632719437168640"
```

Output:

```
Date: Wed, 03 May 2023 21:00:01 (UTC)
```

## Applications

The LinkedIn Timestamp Tool can be used in various OSINT and penetration testing scenarios, including:

1. Activity analysis
2. Event correlation
3. Historical context
4. Temporal profiling

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
