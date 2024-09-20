import os
import requests
import subprocess

# Configuration
WORLD_URL = "https://qravlinciblimqfepcbd.supabase.co/storage/v1/object/public/kingcityterraria/KING_CITY.wld?t=2024-09-20T01%3A27%3A43.020Z"
WORLD_FILE_PATH = "/opt/render/project/src/MyWorld.wld"  # Use the correct path for Render
SERVER_PORT = "7777"

def download_world():
    response = requests.get(WORLD_URL)
    with open(WORLD_FILE_PATH, 'wb') as file:
        file.write(response.content)

def start_server():
    command = f"./TerrariaServer -x64 -world {WORLD_FILE_PATH} -port {SERVER_PORT}"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    download_world()
    start_server()
