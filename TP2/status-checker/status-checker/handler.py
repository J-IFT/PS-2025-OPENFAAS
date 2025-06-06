import os
import json

def handle(event, context):
    try:
        # Le chemin vers le dossier "depot" (local)
        depot_path = "./depot"
        files = []

        if os.path.exists(depot_path):
            files = [f for f in os.listdir(depot_path) if os.path.isfile(os.path.join(depot_path, f))]
        else:
            return json.dumps({"error": "Le dossier depot n'existe pas."})

        return json.dumps({
            "files_found": len(files),
            "files": files
        })

    except Exception as e:
        return json.dumps({"error": str(e)})
