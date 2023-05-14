#import flyr
#thermogram = flyr.unpack("/home/p51pro/UD/Academic/ELEG604/Project/thermal-image_enhancement/edge_imposition_non_ai_approach/testing/thermal/FLIR7321.jpg")
#thermogram.render_pil(edge_emphasis=0.0).save("render-no-edge-emphasis.png")
#thermogram.render_pil(edge_emphasis=1).save("render-edge-emphasis.png")
#mask = thermogram.kelvin > thermogram.kelvin.mean()
#thermogram.render_pil(edge_emphasis=1, mask=mask).save("render-edge-emphasis-masked.png")

import os
import flyr

base_path = "/home/p51pro/UD/Academic/ELEG604/Project/thermal-image_enhancement/edge_imposition_non_ai_approach/testing/thermal/"
for file_name in os.listdir(base_path):
    thermogram = flyr.unpack(os.path.join(base_path,file_name))
    optical_pil, optical_pil_without_pre_processing, render_pil_raw, render_pil, metadata, origin_x, origin_y, crop_box  = thermogram.picture_in_picture_pil(render_opacity=0.8, render_crop=False, get_meta_data_only=True)
    #print(origin_x," ", origin_y," ", render_pil.size, " ", ratio_offset, " ",crop_box)
    render_pil_raw.save("render_pil_raw_{}.png".format(file_name))


"""
optical_pil.save("optical_pil.png")
optical_pil_without_pre_processing.save("optical_pil_without_pre_processing.png")
render_pil.save("render_pil.png")
render_pil_raw.save("render_pil_raw.png")
"""



