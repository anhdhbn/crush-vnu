import os
from urllib.request import urlretrieve
import sys
import platform
import tarfile
import subprocess

platform_os = platform.system().lower()
chilkat_version = os.getenv("CHILKAT_VERSION", "9.5.0.79")
python_version = f"{sys.version_info[0]}.{sys.version_info[1]}"

architecture = platform.machine()
if "arm" in architecture:
    architecture = "arm"

if architecture == "AMD64":
    architecture = "x86_64"

if architecture == "amd64":
    architecture = "x86_64"

if architecture == "i386":
    architecture = "i686"

extension = "tar.gz" if platform_os != "windows" else "zip"
type_os = "" if platform_os == "windows" else f"-{platform_os}"

def download_chilkat():
    link = f"https://chilkatdownload.com/{chilkat_version}/chilkat-9.5.0-python-{python_version}-{architecture}{type_os}.{extension}"
    filepath = f"chilkat-9.5.0-python-{python_version}-{architecture}{type_os}.{extension}"
    urlretrieve(link, filepath)
    return filepath

def extract_file(fname):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        tar.close()

def install_chilkat():
    filepath = download_chilkat()
    extract_file(filepath)
    folder_name = f"chilkat-9.5.0-python-{python_version}-{architecture}{type_os}"
    output = subprocess.call(["python", "installChilkat.py"], cwd=folder_name)
    print(output)