import json
from pathlib import Path
import requests
import hashlib


def checksum(urls):
    # URL of the file
    with open(urls, 'r') as f:
        data = json.load(f)

    apps = ['slack', 'zoom', 'sonos',
            'tmvhost', 'gdrive', 'ibm_aspera',
            'rv', 'vlc', 'spotify',
            'discord', 'whatsapp', 'wacom',
            'parsec']

    num = 0

    for url in data:
        # Download the file
        response = requests.get(f"{data[url]}")
        # Calculate the checksum
        checksum = hashlib.sha256(response.content).hexdigest()
        # Save checksum
        if url == apps[num]:
            with open(f"./border_control/{url}_check.txt", "w") as f:
                print(checksum, file=f)
        else:
            print(f"Something's wrong {url} doesn't match!")

        num += 1

if __name__ == '__main__':
    json_relative_path = Path('./json/urls.json')
    urls = json_relative_path.resolve()
    checksum(urls)
