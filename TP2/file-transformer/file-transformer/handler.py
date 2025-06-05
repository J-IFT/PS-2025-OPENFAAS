import csv
import os
from datetime import datetime
import json

def capitalize_clean(s):
    if not isinstance(s, str):
        return s
    return s.strip().capitalize()

def handle(event):
    input_path = "data/input.csv"
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = f"depot/orders_{today}.csv"

    if not os.path.exists(input_path):
        return json.dumps({"error": f"Le fichier {input_path} est introuvable."})

    os.makedirs("depot", exist_ok=True)

    try:
        with open(input_path, mode='r', encoding='utf-8') as infile, \
             open(output_path, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                row['product'] = capitalize_clean(row.get('product'))
                row['customer'] = capitalize_clean(row.get('customer'))
                writer.writerow(row)

        return json.dumps({"message": f"Fichier transformé et sauvegardé dans {output_path}"})

    except Exception as e:
        return json.dumps({"error": "Erreur durant le traitement du fichier", "details": str(e)})
