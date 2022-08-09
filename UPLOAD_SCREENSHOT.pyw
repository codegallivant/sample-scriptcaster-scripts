import pyautogui as pag
import datetime
import time
import lib.gdrive_pyinteract as gdi
import os

print("Taking screenshot...")
im1 = pag.screenshot()
im_name = "SCREEN_LOG " + os.environ["SC_COMPUTER_NAME"] + " " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') + " .jpg"

if not os.path.isdir('Screenshots'):
    os.mkdir("Screenshots")
path = f"{os.environ['SC_USERSCRIPTS_FOLDER_PATH']}/Screenshots"
im1.save(rf"{path}/{im_name}")
print(f"'{im_name}' created.")

print("Authenticating with Google Drive...")
gdi.set_client_config_path(f"{os.environ['SC_APP_FOLDER_PATH']}/creds/gdrive_api_credentials.json")
client = gdi.authenticate_client(f"{os.environ['SC_APP_FOLDER_PATH']}/creds/gdriveauthcreds.txt")
print(f"Uploading '{im_name}' to Exterior...")
gdi.upload_file(client, 'Exterior/Screen_Logs', path, im_name)
print("Screenshot successfully uploaded to Exterior/Screen_Logs .")

		
