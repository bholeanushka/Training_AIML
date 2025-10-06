import yaml
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(levelname)s - %(message)s')

try:
    # Read YAML file
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        logging.info("Config loaded successfully.")

        # Extract database info
        db = config['database']
        connection_string = f"Connecting to {db['host']}:{db['port']} as {db['user']}"
        print(connection_string)

except FileNotFoundError:
    logging.error("config.yaml not found.")
    print("ERROR - config.yaml not found.")
