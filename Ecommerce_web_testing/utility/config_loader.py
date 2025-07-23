import json
def load_env_config(env="dev"):
    """
    Load environment configuration from a JSON file.
    
    :param file_path: Path to the JSON configuration file.
    :return: Dictionary containing the configuration data.
    """
    with open('data/test_json') as f:
        data = json.load(f)
    return data[env]