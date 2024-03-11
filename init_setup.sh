#!/bin/bash

echo "SSH to machine"
read -p "Enter username@ip: " varname
echo "Enter password: "
read -s password

# Define the path to the .dmg file on the local machine
local_dmg_path="./apps/xcode/Command_Line_Tools_for_Xcode_15.dmg"

# Define the mount point for the .dmg file on the remote machine
remote_mount_point="/Volumes/Command Line Developer Tools"

# Transfer the .dmg file to the remote machine
rsync -avzh --stats --progress -e "ssh" $local_dmg_path $varname:/tmp/cmd_tools.dmg

echo "dmg successully copied to $varname"

# Install the application on the remote machine
ssh "$varname" <<EOF
    # Mount the .dmg file
    hdiutil attach -nobrowse -mountpoint "$remote_mount_point" "/tmp/cmd_tools.dmg"

    # Install file with install -pkg method
    echo "$password" | sudo -S installer -pkg "$remote_mount_point/Command Line Tools.pkg" -target / 2> /dev/null

    # Unmount the .dmg file
    hdiutil detach "$remote_mount_point"

    # Clean up the temporary .dmg file
    rm "/tmp/cmd_tools.dmg"
EOF

password=""