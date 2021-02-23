# Modules Python Index 
# pypi.org
# pip also works to install
# pip install colorama  

# from datetime import timdelta, date

from colorama import Fore, Style, init
import datetime  

print(datetime.date.today()) # Actual date
print(datetime.timedelta(minutes=70)) # Min to Hours

init(convert=True) # Helps to make appear color in terminal 
print(Fore.GREEN + "Hello World")

# Learn about module FLASK, TKINTER
# Learn about framework DJANGO