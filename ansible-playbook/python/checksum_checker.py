import hashlib
import requests

def checksum():
    # URL of the file
    url1 = 'https://slack.com/ssb/download-osx-universal'
    url2 = 'https://zoom.us/client/5.17.5.29101/zoomusInstallerFull.pkg'
    url3 = 'https://www.sonos.com/redir/controller_software_mac2'
    url4 = 'https://download.teamviewer.com/download/TeamViewerHost.dmg'
    url5 = 'https://dl.google.com/drive-file-stream/GoogleDrive.dmg'
    url0 = 'https://cloudgz.gravityzone.bitdefender.com/Packages/MAC/0/3WTALe/setup_downloader.dmg'
    url6 = "https://d3gcli72yxqn2z.cloudfront.net/downloads/connect/latest/bin/ibm-aspera-connect_4.2.8.540_macOS_x86_64.pkg"
    url7 = "https://sg-software.ems.autodesk.com/deploy/rv/Current_Release/MacOS-release.dmg"
    url8 = "https://get.videolan.org/vlc/3.0.20/macosx/vlc-3.0.20-universal.dmg"
    url9 = "https://download.scdn.co/SpotifyInstaller.zip"
    url0 = "https://pax.discord.com/api/download?platform=osx"
    url11 = "https://web.whatsapp.com/desktop/mac_native/release/?configuration=Release"

    # Download the file
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    response5 = requests.get(url5)
    response6 = requests.get(url6)
    response7 = requests.get(url7)
    response8 = requests.get(url8)
    response9 = requests.get(url9)
    response10 = requests.get(url0)
    response11 = requests.get(url11)


    # Calculate the checksum
    checksum1 = hashlib.sha256(response1.content).hexdigest()
    checksum2 = hashlib.sha256(response2.content).hexdigest()
    checksum3 = hashlib.sha256(response3.content).hexdigest()
    checksum4 = hashlib.sha256(response4.content).hexdigest()
    checksum5 = hashlib.sha256(response5.content).hexdigest()
    checksum6 = hashlib.sha256(response6.content).hexdigest()
    checksum7 = hashlib.sha256(response7.content).hexdigest()
    checksum8 = hashlib.sha256(response8.content).hexdigest()
    checksum9 = hashlib.sha256(response9.content).hexdigest()
    checksum10 = hashlib.sha256(response10.content).hexdigest()
    checksum11 = hashlib.sha256(response11.content).hexdigest()

    # Print the checksum
    return checksum1, checksum2, checksum3, checksum4, checksum5, checksum6, checksum7, checksum8, checksum9, checksum10, checksum11

with open("./border_control/slack_check.txt", "w") as f:
    print(checksum()[0], file=f)

with open("./border_control/zoom_check.txt", "w") as f:
    print(checksum()[1], file=f)

with open("./border_control/sonos_check.txt", "w") as f:
    print(checksum()[2], file=f)

with open("./border_control/tmvhost_check.txt", "w") as f:
    print(checksum()[3], file=f)

with open("./border_control/gdrive_check.txt", "w") as f:
    print(checksum()[4], file=f)

with open("./border_control/ibm_aspera_check.txt", "w") as f:
    print(checksum()[5], file=f)

with open("./border_control/rv_check.txt", "w") as f:
    print(checksum()[6], file=f)

with open("./border_control/vlc_check.txt", "w") as f:
    print(checksum()[7], file=f)

with open("./border_control/spotify_check.txt", "w") as f:
    print(checksum()[8], file=f)

with open("./border_control/discord_check.txt", "w") as f:
    print(checksum()[9], file=f)

with open("./border_control/whatsapp_check.txt", "w") as f:
    print(checksum()[10], file=f)

