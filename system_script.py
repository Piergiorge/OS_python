import os

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Change the current working directory
os.chdir("/home/user/documents")

# Print the contents of the new working directory
for file in os.listdir():
    print(file)

# Create a new directory
os.mkdir("new_dir")

# Remove the new directory
os.rmdir("new_dir")

# Remove a file
os.remove("old_file.txt")

# Rename a file
os.rename("old_name.txt", "new_name.txt")

# Get information about a file
info = os.stat("file.txt")
print(f"Size: {info.st_size} bytes")
print(f"Permissions: {oct(info.st_mode)}")
print(f"Modification time: {info.st_mtime}")
