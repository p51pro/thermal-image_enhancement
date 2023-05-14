import os 
import cv2

inp_dir = "/home/p51pro/UD/Academic/ELEG604/Project/RTNet_PyTorch/data/train/thermal"

for file_name in os.listdir(inp_dir):
    file_path = os.path.join(inp_dir,file_name)
    inp_img = cv2.imread(file_path)
    out_img = cv2.resize(inp_img, (640,480), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(file_path,out_img)
