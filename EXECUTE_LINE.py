import ggl_api.exterior_connection as exterior_connection
import USER_CONSTANTS

client = exterior_connection.authenticate("creds/service_account_credentials.json")
sheet = exterior_connection.open_sheet("Exterior", USER_CONSTANTS.COMPUTER_NAME, client)

print('Recieved code will now be executed.')

try:
	print("The code is-")
	print(str(sheet.cell(sheet.find("CODE_LINE").row+1,sheet.find("CODE_LINE").col).value))
	print("Executing...")
	exec(str(sheet.cell(sheet.find("CODE_LINE").row+1,sheet.find("CODE_LINE").col).value))
	sheet.update_cell(sheet.find("LINE_EXECUTION_STATUS").row+1,sheet.find("LINE_EXECUTION_STATUS").col,"Success")
	print("Code execution was successful!")
except:
	sheet.update_cell(sheet.find("LINE_EXECUTION_STATUS").row+1,sheet.find("LINE_EXECUTION_STATUS").col,"Failed")
	print("Code execution gave an exception! Please check the code again and retry.")

print("Process complete.")

			
