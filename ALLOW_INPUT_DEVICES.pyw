import ctypes


ok = ctypes.windll.user32.BlockInput(False)
print("User Input Unblocked.")
			
