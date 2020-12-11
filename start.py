'''
    Organize files in windows system 
'''

from os import listdir
from shutil import move

DOWNLOAD_DIR = r'C:\Users\User1\Downloads'
ENTRY = {
    'Documents': {
        'Destination': r'C:\Users\User1\Documents',
        'Ext': ['.docs', '.xlsx', '.csv'],
    },
    'Music': {
        'Destination': r'C:\Users\User1\Music',
        'Ext': ['.mp3']
    },
    'Pictures': {
        'Destination': r'C:\Users\User1\Pictures\Saved Pictures',
        'Ext': ['.png', '.jpng', '.jpg']
    },
    'Books': {
        'Destination': r'D:\study', # this my directory where i store my pdf
        'Ext': ['.pdf']
    },
}

for item in listdir(DOWNLOAD_DIR):
    for entry in ENTRY:
        for data in ENTRY[entry]['Ext']:
            if item.endswith(data):
                move(str(DOWNLOAD_DIR+r'\\'+item),str(ENTRY[entry]['Destination']+r'\\'+item))
                print(item, ' to ', ENTRY[entry]['Destination'])