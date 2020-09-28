#!/bin/bash
if [ -f "/home/easycanvas/easy-canvas/config/appConfig.json" ];then
  echo "using user appConfig"
else
  echo "copy default appConfig"
  cp /home/easycanvas/easy-canvas/docker/appConfig.json /home/easycanvas/easy-canvas/config/appConfig.json
fi

if [ -f "/home/easycanvas/easy-canvas/config/requirements.json" ];then
  echo "using user requirements"
else
  echo "copy default requirements"
  cp /home/easycanvas/easy-canvas/docker/requirements.json /home/easycanvas/easy-canvas/config/requirements.json
fi

python3 main.py
