import os

img_dir="./img"

old_file_names=os.listdir(img_dir)
old_full_paths= [os.path.join(img_dir, x) for x in old_file_names]


tag="dog"

for i in range (len(old_file_names)):
    new_file_name=tag+"."+str(i+1 )+".jpg"
    new_full_path=os.path.join(img_dir,new_file_name)
    os.rename(old_full_paths[i],new_full_path)
