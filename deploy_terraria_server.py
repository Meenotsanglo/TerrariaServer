import requests
import subprocess
import os

# Direct URL to the world file
WORLD_URL = "https://qravlinciblimqfepcbd.supabase.co/storage/v1/object/public/kingcityterraria/KING_CITY.wld?t=2024-09-20T01%3A27%3A43.020Z"
WORLD_FILE_PATH = "KING_CITY.wld"  # Local path where the world file will be saved

# URL to the Terraria server executable
SERVER_URL = "https://github.com/Meenotsanglo/TerrariaServer/raw/9fbf2a7257b278b21654e1316c11324b195f9f77/TerrariaServer.exe"
SERVER_PATH = "TerrariaServer.exe"  # Local path where the server executable will be saved
SERVER_PORT = "7777"  # Port for the server

# Download the world file
response = requests.get(WORLD_URL)
with open(WORLD_FILE_PATH, 'wb') as f:
    f.write(response.content)

# Download the server executable
response = requests.get(SERVER_URL)
with open(SERVER_PATH, 'wb') as f:
    f.write(response.content)

# Check if the server executable exists
print("Current working directory:", os.getcwd())
print("Server executable exists:", os.path.isfile(SERVER_PATH))

# Start the server
subprocess.run([SERVER_PATH, '-world', WORLD_FILE_PATH, '-port', SERVER_PORT])
