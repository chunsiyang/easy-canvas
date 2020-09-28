FROM python:3.7

RUN apt install -y nodejs \
    && apt install -y npm
 
RUN useradd -ms /bin/bash easycanvas
WORKDIR  /home/easycanvas
RUN cd /home/easycanvas \
    && git clone --depth=1 https://github.com/chunsiyang/easy-canvas/

RUN cd easy-canvas/front-end \
    && npm install \
    && npm run build:prod \
RUN cd /home/easycanvas/easy-canvas
USER easycanvas
CMD python3 main.py
