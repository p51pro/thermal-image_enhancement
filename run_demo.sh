#!/bin/sh

cd /home/p51pro/UD/Academic/ELEG604/Project/live_demo/SRGAN 

python3 /home/p51pro/UD/Academic/ELEG604/Project/live_demo/SRGAN/improved_msx_gen.py

echo "Completed preprocessing"

cd /home/p51pro/UD/Academic/ELEG604/Project/live_demo/SRGAN/SRGAN

conda activate auth_srgan

python3 train.py --mode=eval

echo "Completed inference !!!"
