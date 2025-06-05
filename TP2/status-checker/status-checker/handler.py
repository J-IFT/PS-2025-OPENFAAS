import os
import json

def handle(event, context):
    folder = "./depot"
    os.makedirs(folder, exist_ok=True)
    try:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        return json.dumps({"nb_files": len(files)})
    except Exception as e:
        return json.dumps({"error": str(e)})
