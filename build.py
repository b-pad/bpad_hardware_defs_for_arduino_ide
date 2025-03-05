#! /bin/python
from os import system
import subprocess


def run_system_command(command):
    """
    Executes a system command and returns its output.

    Args:
        command: A string or a list of strings representing the command.

    Returns:
        A string containing the output of the command, or None if an error occurred.
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None


system("cat release.py")

# Future script for releasing bpad packages for Arduino IDE

# show previous releases
system("ls -la release")

# Gather the version
version = input("Enter next release version number (eg: 0.0.0): ")
version = "v" + version
print("The version you entered is: " + version + "!")

# Commit and tag release version
system("git tag " + version)
system("git push --tags")

shortsha = run_system_command("git rev-parse --short HEAD")

#if shortsha:
#	print(shortsha)

zip_filename = "bpad-" + version + "-"+shortsha+".zip"

# Zip up the esp32 directory as such:
system("zip -r " + zip_filename + " esp32/* > zip.log")

# Move the zip file to the release folder
system("mv " + zip_filename + " release/")

# Upload the zip file to github releases

# Create a new release in the platforms section of the package_bpad.app_index.json file

# Copy the release url and paste it into the package_bpad.app_index.json file in the "url" field.

# Update the "archiveFileName" field.

# Generate a SHA-256 on th ecommand line:
filesha = run_system_command("sha256sum ./release/" + zip_filename)
print("Checksum: SHA-256:" + filesha)

# Update the "checksum" field.

