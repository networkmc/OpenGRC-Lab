#!/bin/bash
echo "Resetting GRC lab..."
python3 manage.py flush --noinput
python3 manage.py loaddata sample.json
echo "Lab reset complete. Visit http://192.168.57.1:8010/admin"
