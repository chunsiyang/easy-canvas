FROM python:3.7

RUN apt-get -y update \
    && apt-get install curl \
    && curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get install -y nodejs \
    && apt-get install -y npm
 
RUN useradd -ms /bin/bash easycanvas
WORKDIR  /home/easycanvas
RUN git clone --depth=1 https://github.com/chunsiyang/easy-canvas/
WORKDIR  /home/easycanvas/easy-canvas/front-end 
RUN npm install 
RUN npm run build:prod
WORKDIR /home/easycanvas/easy-canvas
USER easycanvas
CMD python3 main.py
