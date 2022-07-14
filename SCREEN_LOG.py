import pyautogui as pag
import USER_CONSTANTS
import datetime
import time
import ggl_api.gdprocesses as gdprocesses

print("Taking screenshot...")
im1 = pag.screenshot()
im_name = "SCREEN_LOG " + USER_CONSTANTS.COMPUTER_NAME + " " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') + " .jpg"

path = f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts/user_script_generations/screen_logs"
im1.save(rf"{path}/{im_name}")
print(f"'{im_name}' created.")

print("Authenticating with Google Drive...")
gdprocesses.set_client_config_path("creds/client_secret.json")
client = gdprocesses.authenticate_client("creds/gdriveauthcreds.txt")
print(f"Uploading '{im_name}' to Exterior...")
gdprocesses.upload_file(client, 'Exterior/Screen_Logs', path, im_name)
print("Screenshot successfully uploaded to Exterior/Screen_Logs .")

		
