#!/bin/bash
rm sample.db
python3 database.py
python3 populate.py
python3 app.py
