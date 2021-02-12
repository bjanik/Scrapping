#!/bin/bash
set -e

docker run -d --name sql_cnt -e MYSQL_ROOT_PASSWORD=totoxxx123 mysql  # Run mysql container
docker run -itd --name python_scrap_cnt python_scrapping # Run python container

docker network create scrapping # Create a new docker network

docker network connect scrapping python_scrap_cnt # Connect python container to previously created network
docker network connect scrapping sql_cnt # Connect sql container to previously created network

docker exec -it python_scrap_cnt python3 main.py # Run python script in container

docker exec -it sql_cnt mysql -uroot -ptotoxxx123 --execute 'use pokerdb; SELECT * FROM ALL_TIME_PLAYERS;'