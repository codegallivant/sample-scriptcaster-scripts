import pyautogui as pag
import lib.exterior_connection as exterior_connection
import os


print("Obtaining message and title text from Exterior...")
client = exterior_connection.authenticate(os.path.join(os.environ["SC_APP_FOLDER_PATH"],"creds/service_account_credentials.json"))
sheet = exterior_connection.open_sheet("Exterior", os.environ["SC_COMPUTER_NAME"], client)
_ , parameter_values = exterior_connection.get_parameter_values(sheet)
message = parameter_values["Alert box message"]
title = parameter_values["Alert box title"]
print("Creating alert box...")
pag.alert(text = str(message), title = str(title))
print("Box closed.")
