#!/bin/bash

docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=root -e POSTGRES_DB=mails -d postgres

docker run --name redis -p 6379:6379 -d redis