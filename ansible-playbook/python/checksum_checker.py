import hashlib
import requests

def checksum():
    # URL of the file
    urls = [
    "https://slack.com/ssb/download-osx-universal",
    "https://zoom.us/client/5.17.11.31580/zoomusInstallerFull.pkg",
    "https://www.sonos.com/redir/controller_software_mac2",
    "https://download.teamviewer.com/download/TeamViewerHost.dmg",
    "https://dl.google.com/drive-file-stream/GoogleDrive.dmg",
    "https://d3gcli72yxqn2z.cloudfront.net/downloads/connect/latest/bin/ibm-aspera-connect_4.2.8.540_macOS_x86_64.pkg",
    "https://sg-software.ems.autodesk.com/deploy/rv/Current_Release/MacOS-release.dmg",
    "https://get.videolan.org/vlc/3.0.20/macosx/vlc-3.0.20-universal.dmg",
    "https://download.scdn.co/SpotifyInstaller.zip", 
    "https://pax.discord.com/api/download?platform=osx", 
    "https://web.whatsapp.com/desktop/mac_native/release/?configuration=Release",
    "https://cdn.wacom.com/u/productsupport/drivers/mac/professional/WacomTablet_6.4.5-3.dmg",
    "https://builds.parsec.app/package/parsec-macos.pkg",
    ]

    num = 1

    for url in urls:
        # Download the file
        response = requests.get(f"{url}")
        # Calculate the checksum
        checksum = hashlib.sha256(response.content).hexdigest()
        # Save checksum
        if num == 1:
            with open("./border_control/slack_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 2:
            with open("./border_control/zoom_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 3:
            with open("./border_control/sonos_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 4:
            with open("./border_control/tmvhost_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 5:
            with open("./border_control/gdrive_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 6:
            with open("./border_control/ibm_aspera_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 7:
            with open("./border_control/rv_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 8:
            with open("./border_control/vlc_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 9:
            with open("./border_control/spotify_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 10:
            with open("./border_control/discord_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 11:
            with open("./border_control/whatsapp_check.txt", "w") as f:
                print(checksum, file=f)
        elif num == 12:
            with open("./border_control/wacom_check.txt", "w") as f:
                print(checksum, file=f)
        else:
            with open("./border_control/parsec_check.txt", "w") as f:
                print(checksum, file=f)

        num += 1

checksum()
