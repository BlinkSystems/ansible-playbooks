import requests
from pathlib import Path
import json


relative_path = Path('ansible/py/url_status.txt')
json_relative_path = Path('./json/urls.json')
txtfl = relative_path.resolve()
urls = json_relative_path.resolve()

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

    with open(urls, 'r') as f:
        data = json.load(f)

    with open(txtfl, "w", encoding='utf-8') as f:

        for url in data:
            result = (url_checker(data[url]))
            f.write(f'{result}\n')

    f.close()