import json
import redis
import os
from datetime import datetime

def handle(event, context):
    try:
        data = json.loads(event.body)
        message = data.get("message")

        if not message:
            return {"statusCode": 400, "body": "Missing 'message' field"}

        r = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis-master"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            decode_responses=True
        )

        timestamp = datetime.now().isoformat()
        r.set(timestamp, message)

        return {"statusCode": 200, "body": f"Message saved at {timestamp}"}

    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
