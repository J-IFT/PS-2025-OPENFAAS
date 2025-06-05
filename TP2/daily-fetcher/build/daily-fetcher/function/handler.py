import json
from datetime import datetime

def handle(req):
    now = datetime.now()
    message = {
        "timestamp": now.isoformat(),
        "message": "Nouvelle commande à traiter"
    }
    return json.dumps(message)
