import requests
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import argparse
import csv

headers = {'User-Agent': 'BulkStatusCheck/1.0 (+https://github.com/makmour)'}

session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount('http://', adapter)
session.mount('https://', adapter)

def check_url(url):
    try:
        response = session.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return url, response.status_code, 'Success'
    except requests.exceptions.HTTPError as e:
        return url, response.status_code, f'HTTP Error: {e}'
    except requests.exceptions.Timeout:
        return url, 'Timeout', 'Timeout Error'
    except requests.exceptions.RequestException as e:
        return url, 'Error', f'Request Error: {e}'

def main(file):
    with open(file, 'r') as f:
        urls = [line.strip() for line in f]

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_url, urls)

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Status Code', 'Message'])
        for result in results:
            print(f"{result[0]} @ {result[1]} - {result[2]}")
            writer.writerow(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bulk URL Status Checker')
    parser.add_argument('-f', '--file', default='urls.txt', help='Path to file containing URLs (default: urls.txt)')
    args = parser.parse_args()
    main(args.file)
