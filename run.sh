#!/bin/bash
set -ex

SQL_CNT='sql_cnt'
SCRAP_CNT='python_scrap_cnt'
DB_NAME='pokerdb'
NETWORK='scrapping'
USER='root'
PASSWORD='totoxxx123'

docker run -d --name $SQL_CNT -e MYSQL_ROOT_PASSWORD=$PASSWORD -e MYSQL_DATABASE=$DB_NAME -e MYSQL_USER=$USER -e MYSQL_HOST=$SQL_CNT mysql # Run mysql container
docker run -itd --name $SCRAP_CNT --mount type=bind,src=$(PWD)/app,dst=/app python_scrapping # Run python container

docker network create $NETWORK # Create a new docker network
docker network connect $NETWORK $SCRAP_CNT # Connect python container to previously created network
docker network connect $NETWORK $SQL_CNT # Connect sql container to previously created network

docker exec -it $SCRAP_CNT python3 main.py # Run python script in container