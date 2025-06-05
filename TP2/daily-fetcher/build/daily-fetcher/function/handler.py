import json
from datetime import datetime
import requests
import os

def handle(event, context):
    # Générer la date du jour
    today = datetime.now().strftime("%Y-%m-%d")
    payload = {"date": today}

    # Publier sur NATS via OpenFaaS gateway (async invoke)
    gateway = os.getenv("gateway_url", "http://gateway.openfaas:8080")
    topic = "orders.import"
    url = f"{gateway}/async-function/file-transformer"
    headers = {
        "Content-Type": "application/json",
        "X-Nats-Topic": topic
    }
    print(f"DEBUG: url={url}, payload={payload}")
    try:
        resp = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f"DEBUG: status={resp.status_code}, text={resp.text}")
        return f"Message publié sur NATS ({topic}) : {payload}, status={resp.status_code}"
    except Exception as e:
        print(f"Erreur lors de la publication : {str(e)}")
        return f"Erreur lors de la publication : {str(e)}"
