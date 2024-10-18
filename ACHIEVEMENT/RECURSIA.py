import requests
from datetime import datetime

min_tem = 0
date = None

url = 'https://parsinger.ru/3.4/3/dialog.json'
response = requests.get(url=url)

    
print(response)

F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}

def get_files(path, depth=0):
    for f in path:
        print('--'*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" "*(depth+1), ", ".join(path[f]))
            
print(get_files(F))

