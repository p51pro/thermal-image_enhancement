import os 
import numpy as np 
import cv2
import flyr


    
def get_metadata(thermal_path):
    thermogram = flyr.unpack(thermal_path)
    optical_pil, optical_pil_without_pre_processing, render_pil_raw, render_pil, ratio_offset, origin_x, origin_y, crop_box = thermogram.picture_in_picture_pil(render_opacity=0.8, render_crop=False, get_meta_data_only=True)
    return [origin_x, origin_y, render_pil.size], optical_pil_without_pre_processing, render_pil
    

def get_thermal_roi(metadata, thermal_raw):
    thermal_raw = cv2.blur(thermal_raw,(3,3))
    return thermal_raw
 
def get_rgb_roi(metadata, rgb_raw):
    rgb_raw = rgb_raw[metadata[1]:metadata[1]+metadata[2][1],metadata[0]:metadata[0]+metadata[2][0],:]
    return rgb_raw
        
def enhance_img(rgb, thermal):  
    mask = cv2.Laplacian(rgb, cv2.CV_8U, ksize=3)

    mask_inv = cv2.bitwise_not(mask)
    thermal_enhanced = cv2.add(thermal, mask)
    thermal_enhanced_inv = cv2.bitwise_and(thermal, mask_inv)
    
    #gamma = 1/2
    #gamma_corrected = np.array(255*(rgb / 255) ** gamma, dtype = 'uint8')
    
    #contrast=5
    #brightness=2
    #rgb = cv2.addWeighted( rgb, contrast, rgb, 0, brightness)
    gamma = 3
    gamma_corrected = np.array(255*(rgb / 255) ** gamma, dtype = 'uint8')
    
    output = cv2.addWeighted(thermal_enhanced_inv, 0.7, gamma_corrected, 0.4, 0)
    
    return output
    
def process_img(rgb_path, thermal_path, out_msx_path, out_thermal_path, out_rgb_path):
    rgb = cv2.imread(rgb_path)
    thermal = cv2.imread(thermal_path)
    
    metadata, rgb, thermal = get_metadata(thermal_path)
    thermal = np.array(thermal)
    rgb = np.array(rgb)
    #thermal = cv2.resize(thermal, (160,120), interpolation = cv2.INTER_AREA)
    #rgb = cv2.resize(rgb, (480,640), interpolation = cv2.INTER_AREA)
    
    rgb_roi = get_rgb_roi(metadata, rgb)
    thermal_roi = get_thermal_roi(metadata, thermal)

    #print(metadata)
    #print(rgb_roi.shape)
    #print(thermal_roi.shape)
    
    thermal_roi = cv2.cvtColor(thermal_roi, cv2.COLOR_BGR2RGB)
    rgb_roi = cv2.cvtColor(rgb_roi, cv2.COLOR_BGR2RGB)
    msx_out_img = cv2.resize(enhance_img(rgb_roi,thermal_roi), (640, 480), interpolation = cv2.INTER_CUBIC)  
    cv2.imwrite(out_msx_path, msx_out_img)
    rgb_roi = cv2.resize(rgb_roi, (640, 480), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(out_rgb_path,rgb_roi)
    thermal_roi = cv2.resize(thermal_roi, (160, 120), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(out_thermal_path,thermal_roi)

    
    
dataset_path = "/home/p51pro/UD/Academic/ELEG604/Project/presentation/"
output_path = "/home/p51pro/UD/Academic/ELEG604/Project/presentation/msx/"

if not os.path.exists(output_path):
    os.mkdir(output_path)
rgb_img_path = os.path.join(dataset_path,"rgb")
thermal_img_path = os.path.join(dataset_path,"thermal")

out_msx_path = os.path.join(output_path, "msx")
if not os.path.exists(out_msx_path):
    os.mkdir(out_msx_path)
    
out_thermal_path = os.path.join(output_path, "thermal")
if not os.path.exists(out_thermal_path):
    os.mkdir(out_thermal_path)
    
out_rgb_path = os.path.join(output_path, "rgb")
if not os.path.exists(out_rgb_path):
    os.mkdir(out_rgb_path)
    
for file_name in os.listdir(thermal_img_path):
    try:
        #print(file_name)
        out_msx = os.path.join(out_msx_path,file_name)
        out_thermal = os.path.join(out_thermal_path,file_name)
        out_rgb = os.path.join(out_rgb_path,file_name)
        process_img(os.path.join(rgb_img_path,file_name), os.path.join(thermal_img_path,file_name), out_msx, out_thermal, out_rgb)
    except:
        print(file_name)
    
