import os
import requests

# Configuration
WORLD_URL = "https://qravlinciblimqfepcbd.supabase.co/storage/v1/object/public/kingcityterraria/KING_CITY.wld?t=2024-09-20T01%3A27%3A43.020Z"
WORLD_FILE_PATH = "C:\\terraria\\worlds\\MyWorld.wld"  # Adjust as needed
SERVER_PATH = "C:\\TerrariaServer\\TerrariaServer.exe"  # Path to the server executable

def download_world():
    response = requests.get(WORLD_URL)
    with open(WORLD_FILE_PATH, 'wb') as f:
        f.write(response.content)

def start_server():
    os.startfile(SERVER_PATH)

if __name__ == "__main__":
    download_world()
    start_server()
