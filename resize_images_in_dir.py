import os
import cv2

path = "/home/p51pro/UD/Academic/ELEG604/Project/DataSet/val/repro_msx"
for file_name in os.listdir(path):
    img = cv2.imread(os.path.join(path,file_name))
    resized = cv2.resize(img, (160,120), interpolation = cv2.INTER_AREA)
    cv2.imwrite(os.path.join(path,file_name), resized)
