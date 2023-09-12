#!/bin/bash

# Download sppe from Google Drive
filename='./joints_detectors/Alphapose/models/sppe/duc_se.pth'

fileid='1OPORTWB2cwd5YTVBX-NE8fsauZJWsrtW'
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=${fileid}' -O- | sed -rn 's/.confirm=([0-9A-Za-z_]+)./\1\n/p')&id=${fileid}" -O ${filename} && rm -rf /tmp/cookies.txt

# Download yolo from Google Drive
filename='./joints_detectors/Alphapose/models/yolo/yolov3-spp.weights'

fileid='1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC'
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=${fileid}' -O- | sed -rn 's/.confirm=([0-9A-Za-z_]+)./\1\n/p')&id=${fileid}" -O ${filename} && rm -rf /tmp/cookies.txt


