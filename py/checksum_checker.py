import json
from pathlib import Path
import requests
import hashlib


def checksum(urls):
    with open(urls, 'r') as f:
        data = json.load(f)

    macDT = (data['mac'])
    winDT = (data['windows'])

    # Check macOS URL links
    for apps in macDT:
        for url in apps:
            #  Download the file
            if apps.get(url):
                urlLink = apps.get(url)
                response = requests.get(urlLink)
                if response.ok:
                    # # Calculate the checksum
                    checksum = hashlib.sha256(response.content).hexdigest()
                    with open(f"./border_control/{url}_check.txt", "w") as f:
                        print(checksum, file=f)
                else:
                    print(f"Can't reach {urlLink}!")
            else:
                pass

    # Check windows URL links
    for apps in winDT:
        for url in apps:
            # Download the file
            if apps.get(url):
                urlLink = apps.get(url)
                response = requests.get(urlLink)
                if response.ok:
                    # # Calculate the checksum
                    checksum = hashlib.sha256(response.content).hexdigest()
                    with open(f"./border_control/win_{url}_check.txt", "w") as f:
                        print(checksum, file=f)
                else:
                    print(f"Can't reach {urlLink}!")
            else:
                pass


if __name__ == '__main__':
    json_relative_path = Path('./json/__urls__.json')
    urls = json_relative_path.resolve()
    checksum(urls)
    

