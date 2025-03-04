#! /bin/python
from os import system
system("cat release.py")

# Future script for releasing bpad packages for Arduino IDE

# Commit and tag release version

# Zip up the esp32 directory as such:
# $ zip -r bpad-vX.X.X-SHORTSHA.zip esp32/*

# Upload the zip file to github releases

# Create a new release in the platforms section of the package_bpad.app_index.json file

# Copy the release url and paste it into the package_bpad.app_index.json file in the "url" field.

# Update the "archiveFileName" field.

# Generate a SHA-256 on th ecommand line:
# $ sha256sum bpad-v0.1.0-818ebdce.zip

# Update the "checksum" field.

