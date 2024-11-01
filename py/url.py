import requests
from pathlib import Path
import json


def url_checker(url):
    try:
        get = requests.get(url)
        # if the requests succeeds
        if get.status_code == 200:
            return(f"{url}: is reachable, Status_Code : {get.status_code}")
        else:
            return(f"{url}: is not reachable, Status_Code: {get.status_code}")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url} is not reachable \nErr: {e}")


if __name__ == '__main__':
    relative_path = Path('ansible/py/url_status.txt')
    json_relative_path = Path('./json/__urls__.json')
    txtfl = relative_path.resolve()
    urls = json_relative_path.resolve()

    with open(urls, 'r') as f:
        data = json.load(f)

    macDT = (data['mac'])
    winDT = (data['windows'])

    with open(txtfl, "w", encoding='utf-8') as f:


        for apps in macDT:
            for url in apps:
                #  Download the file
                if apps.get(url):
                    urlLink = apps.get(url)
                    # Check URL status
                    result = (url_checker(urlLink))
                    f.write(f'macOS: {result}\n')

        for apps in winDT:
            for url in apps:
                # Download the file
                if apps.get(url):
                    urlLink = apps.get(url)
                    response = requests.get(urlLink)
                    result = (url_checker(urlLink))
                    f.write(f'winOS: {result}\n')

    f.close()