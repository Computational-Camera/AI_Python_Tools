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
            
import pandas as pd 

frame_id    = []  
label_id    = []  
class_id    = [] 
boxes_list  = [] 
confidence  = []

df  = pd.DataFrame({'Frame_ID':frame_id, 'Lable_ID':obj_class, 'Class':obj_class, 'Confidence':confidence, 'Box':boxes_list}) 
df.to_csv(OUTPUT_CSV_DIR, index=False, columns=['Frame_ID', 'Lable_ID', 'Class', 'Confidence', 'Box']) # add date     

#load csv files from directory
for file in glob.glob("./*.csv"):
    df = pd.read_csv(file)
    labels   = df['label'].values.tolist()

#creat folder
os.makedirs(out_dir +'/checkpoint', exist_ok=True)
