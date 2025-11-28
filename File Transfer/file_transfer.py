import shutil
source = input("Enter the source file path: ")
destination = input("Enter the destination path: ")

try:
  shutil.copy(source, destination)
  print(f"File has been transferred from {source} to {destination} successfully!")
except FileNotFoundError:
  print("Source file not found. Please check the path.")
except PermissionError:
  print("Permission denied. Cannot copy the file.")
except Exception as e:
  print(f"An error occurred: {e}")
