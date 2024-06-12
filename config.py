import os
import sys
sys.path.append('/Users/daichikiyozaki/confluence_api_test/venv/lib/python3.10/site-packages')
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def load_env_or_exit(env_name: str) -> str:
    """
    Get the value of the environment variable.
    If it is not set, an error message is displayed and the program is terminated.
    """
    env_val = os.getenv(env_name)
    if not env_val:
        sys.exit(
            f"Error: {env_name} not set. Please consider adding a .env file with {env_name}."
        )
    return env_val


# Export configuration variables
CONFLUENCE_URL = load_env_or_exit("CONFLUENCE_URL")
CONFLUENCE_TOKEN = load_env_or_exit("CONFLUENCE_TOKEN")
CONFLUENCE_USERNAME = load_env_or_exit("CONFLUENCE_USERNAME")
CONFLUENCE_SPACE_KEY = load_env_or_exit("CONFLUENCE_SPACE_KEY")
