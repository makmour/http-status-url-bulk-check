import requests

with open('urls.txt', 'r') as f:
    for line in f:
        url = line.strip()  # Remove leading/trailing whitespaces, newlines, etc.
        print(url, end=' @ ')

        try:
            r = requests.get(url)
            if r.status_code == 200:
                print('200 @ Success!')
            elif r.status_code == 301:
                print('301 @ Moved Permanently!')
            elif r.status_code == 404:
                print('404 @ Not Found!')
            elif r.status_code == 302:
                print('302 @ Object Moved!')
            elif r.status_code == 403:
                print('403 @ Forbidden!')
            else:
                print(f'{r.status_code} @ Unknown Status')
        except requests.ConnectionError:
            print('Connection Error')
