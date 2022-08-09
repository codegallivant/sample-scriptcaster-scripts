# sample-scriptcaster-scripts

<br>

Sample scripts for [script-caster app](https://github.com/codegallivant/script-caster).
<br>
[Copy of Exterior](https://docs.google.com/spreadsheets/d/1-wv6vr59HgRiFLgtHK0UWTZpZ9824Kmz-BNgz9Xq0YI/edit?usp=sharing).

<br>

## Script descriptions

- `GET_LOCATION.pyw`<br>
  Gets IP location of target machine and writes information to Exterior.

- `UPLOAD_SCREENSHOT.pyw`  <br>
  Takes a screenshot of the target machine and uploads it to a Google Drive folder.

- `STAY_AWAKE.pyw`<br>
  Forces computer to not go to sleep by pressing the F15 key every 60 seconds.

- `PIP_PACKAGE.pyw`<br>
  Installs/updates/uninstalls pip packages. Useful if you're creating a python script using pip modules which are currently not installed on the target computer. The package name is inputted in Exterior.

- `AlERT_BOX.pyw`<br>
  Creates an alert box. You can input the title and text in Exterior.

- `EXECUTE_LINE.pyw`<br>
  Executes a line of code. You can input the line in Exterior.

- `NEXT_VIRTUAL_DESKTOP.pyw & PREVIOUS_VIRTUAL_DESKTOP.pyw`<br>
  Moves to subsequent/previous virtual desktop.

<br>

## Tools to deal with Exterior and Google Drive
Scripts often need to interact with Exterior and Google Drive. To do so, the files `lib/exterior_connection.py` and `lib/gdrive_pyinteract.py` can be imported. Examples of their usage can be found in `UPLOAD_SCREENSHOT.pyw`, `GET_LOCATION.pyw` and a few others. You can also find more details on `lib/gdrive_pyinteract.py` in this [repository](https://github.com/codegallivant/gdrive-interact-python).

<br>

## How script-caster runs the scripts
1. It downloads the all the files in this repository into a folder of your choice. You can set the folder path in Settings (Visible in app GUI).
2. It checks Exterior for the switch for the script.
3. If the switch is enabled, the script is run. Upon completion of execution of the script, it's switch in Exterior is turned off automatically. If you turn the script's switch off while the script is running, the script will be terminated without it's execution completing.

