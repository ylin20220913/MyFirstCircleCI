! /usr/bin/env bash

set -e

export DEBIAN_FRONTEND="noninteractive"

# Install
echo ">>>>>>>>>>> INSTALLING ROBOT FRAMEWORK"
pip install RPi.GPIO

# robot framework
pip3 install robotframework
pip3 install elasticsearch

# build m7ats module for robot framework
echo ">>>>>>>>>>>M7ATS module"
# git clone https://ztrldgit01.ztr.biz/tests/shims/robo-ats.git
# cd robo-ats
python3 -m pip install .
# cd ..
robot .