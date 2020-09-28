#!/bin/bash
sed -i "s/127.0.0.1/$DB_HOST" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/27017/$DB_PORT" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/easy-canvas/$DB_NAME" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/root/$DB_USER" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/your_db_password/$DB_PWD" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/your_from_email/$EMAIL_FROM" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/your_email_host/$EMAIL_HOST" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/you_email_username/$EMAIL_USERNAME" \
/home/easycanvas/easy-canvas/config/appConfig.json

sed -i "s/you_email_passwd/$EMAIL_PASSWORD" \
/home/easycanvas/easy-canvas/config/appConfig.json

python3 main.py
