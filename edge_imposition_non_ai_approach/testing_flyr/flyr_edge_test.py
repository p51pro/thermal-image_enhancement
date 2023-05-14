import flyr

thermogram = flyr.unpack("/home/p51pro/UD/Academic/ELEG604/Project/thermal-image_enhancement/edge_imposition_non_ai_approach/testing/thermal/FLIR7321.jpg")
thermogram.render_pil(edge_emphasis=0.0).save("render-no-edge-emphasis.png")
thermogram.render_pil(edge_emphasis=0.275).save("render-edge-emphasis.png")

mask = thermogram.kelvin > thermogram.kelvin.mean()
thermogram.render_pil(edge_emphasis=0.275, mask=mask).save("render-edge-emphasis-masked.png")
