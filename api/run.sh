#/bin/bash
# executer le code train.py
python3 train.py
# delpoyer l'API 
uvicorn api.main:app --reload --host "0.0.0.0" --port 5000