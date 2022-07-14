import ctypes

ok = ctypes.windll.user32.BlockInput(True)
print("User input blocked.")
			
