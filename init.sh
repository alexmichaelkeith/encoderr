#!/bin/bash

mkdir -p /config/db
mkdir -p /config/artwork
touch /config/db/database.db
python src/init_db.py

uvicorn src.main:app --host 0.0.0.0 --port 8000