import os
REDIS_URL = f"redis://{os.environ.get('REDIS_HOST')}:6379/1"
