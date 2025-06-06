import csv
import os
import json
from datetime import datetime

def handle(event, context):
    try:
        data = json.loads(event.body)
        date_from_nats = data.get("date", "")
        print(f"Reçu : {data}")

        input_path = "./data/input.csv"
        output_path = "./depot/output.csv"
        user_id = "US7"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transformed_rows = []

        # Lire le fichier CSV
        with open(input_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transformed_row = {
                    "order_id": row["order_id"],
                    "product": row["product"].lower(),
                    "quantity": row["quantity"],
                    "customer": row["customer"].upper(),
                    "Processed-Date": now,
                    "process_by": user_id
                }
                transformed_rows.append(transformed_row)

        # Écrire le fichier transformé
        fieldnames = transformed_rows[0].keys()
        with open(output_path, 'w', newline='', encoding='utf-8') as out_csv:
            writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transformed_rows)

        return f"Transformation réussie, fichier écrit dans {output_path}"

    except Exception as e:
        return f"Erreur : {str(e)}"
