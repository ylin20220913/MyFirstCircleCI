! /usr/bin/env bash

set -e

export DEBIAN_FRONTEND="noninteractive"

# Install
echo ">>>>>>>>>>> INSTALLING ROBOT FRAMEWORK"
apt-get update --allow-releaseinfo-change

# robot framework
pip3 install robotframework
pip3 install elasticsearch


# build m7ats module for robot framework
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>M7ATS module"
cd robo-ats
python3 -m pip install .

cd ../
robot .