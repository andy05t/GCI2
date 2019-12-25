#!/bin/sh

echo Staring GCI script...
sleep 5

#xhost +
export DISPLAY=:0

cd /home/andrey/Documents
/usr/bin/python3 GCI2.py

