import requests

urls = [
"https://slack.com/ssb/download-osx-universal",
"https://zoom.us/client/6.0.2.33403/zoomusInstallerFull.pkg?archType=arm64",
"https://www.sonos.com/redir/controller_software_mac2",
"https://download.teamviewer.com/download/TeamViewerHost.dmg",
"https://dl.google.com/drive-file-stream/GoogleDrive.dmg",
"https://d3gcli72yxqn2z.cloudfront.net/downloads/connect/latest/bin/ibm-aspera-connect_4.2.12.780_macOS_x86_64.pkg",
"https://sg-software.ems.autodesk.com/deploy/rv/Current_Release/MacOS-release.dmg",
"https://get.videolan.org/vlc/3.0.20/macosx/vlc-3.0.20-universal.dmg",
"https://download.scdn.co/SpotifyInstaller.zip", 
"https://discord.com/api/download?platform=osx", 
"https://web.whatsapp.com/desktop/mac_native/release/?configuration=Release",
"https://cdn.wacom.com/u/productsupport/drivers/mac/professional/WacomTablet_6.4.5-3.dmg",
"https://builds.parsec.app/package/parsec-macos.pkg",
]


def url_checker(url):
    try:
        get = requests.get(url)
        # if the requests succeeds
        if get.status_code == 200:
            return(f"{url}: is reachable")
        else:
            return(f"{url}: is not reachable, status_code: {get.status_code}")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url} is not reachable \nErr: {e}")

with open("/home/eng/ansible/ansible-playbook/python/textfile.txt", "w", encoding='utf-8') as f:

    for url in urls:
        result = (url_checker(url))
        f.write(f'{result}\n')

f.close()
