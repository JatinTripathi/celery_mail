#!/bin/bash

docker run --name db -e POSTGRES_PASSWORD=postgres -d postgres
docker run -it --name life_goals --link db:db -p 80:80 jatintripathi/goal_balance