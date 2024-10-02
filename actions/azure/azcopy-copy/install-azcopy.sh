#! /bin/sh
sudo apt-get update
sudo apt-get install -y curl
curl -sSL -O https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y azcopy

# Show version
echo "azcopy version:"
azcopy --version
# Show path
echo "azcopy path:"
type azcopy
