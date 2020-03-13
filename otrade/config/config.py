import os
import sys
from pathlib import Path

ENV_DIR = Path(os.path.dirname(sys.modules['__main__'].__file__)).parent
ENV_FILE = os.path.join(ENV_DIR, '.env')
ENV_EXCEPTION = 'Not available'

try:
    with open(ENV_FILE) as f:
        for line in f:
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

    # Robinhood Credentials
    RH_USERNAME = os.environ['RH_USERNAME']
    RH_PASS = os.environ['RH_PASS']
except Exception as e:
    print('Exception in config:', e)
    RH_USERNAME = ENV_EXCEPTION
    RH_PASS = ENV_EXCEPTION
