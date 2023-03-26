import os 
import shutil

inp_dir = "/home/p51pro/UD/Academic/ELEG604/Project/100_FLIR"
output_dir = "/home/p51pro/UD/Academic/ELEG604/Project/output_files"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

thermal_output = os.path.join(output_dir,"thermal/")
if not os.path.exists(thermal_output):
    os.mkdir(thermal_output)

rgb_output = os.path.join(output_dir,"rgb/")
if not os.path.exists(rgb_output):
    os.mkdir(rgb_output)

#FLIR4451.jpg
file_index_to_name=dict()
for inp_name in os.listdir(inp_dir):
    index = int(str(inp_name.split(".jpg")[0]).split("FLIR")[-1])
    file_index_to_name[index] = inp_name
while(len(file_index_to_name.keys())!=0):
    last=min(file_index_to_name.keys())
    last_but_one=min(file_index_to_name.keys())+1
    if int(last_but_one) in file_index_to_name.keys():
        thermal_shift_src = os.path.join(inp_dir,file_index_to_name[last])
        rgb_shift_src = os.path.join(inp_dir,file_index_to_name[last_but_one])
        thermal_shift_dest = os.path.join(thermal_output,file_index_to_name[last])
        rgb_dst_name = "FLIR{}.jpg".format(int(str(file_index_to_name[last].split(".jpg")[0]).split("FLIR")[-1]))  
        file_index_to_name[last_but_one]
        rgb_shift_dest = os.path.join(rgb_output,rgb_dst_name)
        shutil.copy(rgb_shift_src, rgb_shift_dest)
        shutil.copy(thermal_shift_src, thermal_shift_dest)

        del file_index_to_name[last]
        del file_index_to_name[last_but_one]
    else:
        print("Anomoly in {}".format(last_but_one))
        del file_index_to_name[last] 

