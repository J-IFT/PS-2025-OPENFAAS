import random

quotes = [
    "La simplicité est la sophistication suprême.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Talk is cheap. Show me the code.",
    "Premature optimization is the root of all evil.",
    "Programs must be written for people to read."
]

def handle(event, context):
    return {
        "statusCode": 200,
        "body": random.choice(quotes)
    }
