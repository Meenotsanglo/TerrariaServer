import requests
import subprocess

# Direct URL to the world file
WORLD_URL = "https://qravlinciblimqfepcbd.supabase.co/storage/v1/object/public/kingcityterraria/KING_CITY.wld?t=2024-09-20T01%3A27%3A43.020Z"
WORLD_FILE_PATH = "KING_CITY.wld"  # Local path where the world file will be saved
SERVER_PATH = "C:\\TerrariaServer\\TerrariaServer.exe"  # Path to the Terraria server executable
SERVER_PORT = "7777"  # Port for the server

# Download the world file
response = requests.get(WORLD_URL)
with open(WORLD_FILE_PATH, 'wb') as f:
    f.write(response.content)

# Start the server
subprocess.run([SERVER_PATH, "-world", WORLD_FILE_PATH, "-port", SERVER_PORT])
