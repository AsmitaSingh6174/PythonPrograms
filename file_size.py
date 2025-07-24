import os

totalSize = 0
folder_path = r"C:\Users\DELL-PC\OneDrive\Desktop\Python"  # Raw string to avoid \U issues

for file in os.listdir(folder_path):
    filepath = os.path.join(folder_path, file)
    if os.path.isfile(filepath):  # Only count file sizes, not folders
        totalSize += os.path.getsize(filepath)

print("Total Size of All files is:", totalSize, "bytes")