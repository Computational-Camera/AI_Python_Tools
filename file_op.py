

import glob, os
import shutil

#copy files

if not os.path.exists(directory):
    os.makedirs(directory)
try:
    shutil.copy(src, directory+dst)    
except:
    print() 

# search files   
for root, dirs, files in sorted(os.walk(DATA_DIR)):
    for f in files:
        fullpath = os.path.join(root, f)
        if os.path.splitext(fullpath)[1] == '.json':
            file_id = f.split('.') 
