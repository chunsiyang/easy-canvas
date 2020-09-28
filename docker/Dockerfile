FROM nikolaik/python-nodejs
 
RUN useradd -ms /bin/bash easycanvas
WORKDIR  /home/easycanvas
RUN git clone --depth=1 https://github.com/chunsiyang/easy-canvas/
WORKDIR  /home/easycanvas/easy-canvas/front-end 
RUN npm install 
RUN npm run build:prod
WORKDIR /home/easycanvas/easy-canvas
CMD sh docker/start.sh
