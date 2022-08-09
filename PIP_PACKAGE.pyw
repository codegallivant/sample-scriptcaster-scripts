import subprocess
import sys
import lib.exterior_connection as exterior_connection
import os


def pip_command(package, command):
    subprocess.check_call([sys.executable, "-m", "pip", *command, package])


print("Getting package name from Exterior...")

client = exterior_connection.authenticate(f"{os.environ['SC_APP_FOLDER_PATH']}creds/service_account_credentials.json")
sheet = exterior_connection.open_sheet("Exterior",os.environ["SC_COMPUTER_NAME"],client)
_ , parameter_values = exterior_connection.get_parameter_values(sheet)

package_name = parameter_values["Pip Package name"]
pip_op_type = parameter_values["Pip Operation type"]

if pip_op_type == "Upgrade":
    command = ["install","--upgrade"]
    pip_op_type = "Upgrad"
elif pip_op_type == "Install":
    command = ["install"]
elif pip_op_type == "Uninstall":
    command = ["uninstall","-y"]

print(f"{pip_op_type}ing {package_name}...")
pip_command(package_name, command)
print(f"{pip_op_type}ed.", package_name)
