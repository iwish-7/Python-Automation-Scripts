import os
from datetime import datetime #datetime is both a module and a class 

# print(os.getcwd())
folder = input("Enter the folder path: ")
os.chdir(folder)

curr_date = datetime.today().strftime('%Y-%m-%d')

for file in os.listdir(folder):
    new_name = f"{curr_date}_{file}"
    os.rename(file, new_name)

print("All files have been renamed")