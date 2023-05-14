from easydict import EasyDict as edict
import json

config = edict()
config.TRAIN = edict()
config.TRAIN.batch_size = 32 # [16] use 8 if your GPU memory is small
config.TRAIN.lr_init = 1e-4
config.TRAIN.beta1 = 0.9

## initialize G
config.TRAIN.n_epoch_init = 1
    # config.TRAIN.lr_decay_init = 0.1
    # config.TRAIN.decay_every_init = int(config.TRAIN.n_epoch_init / 2)

## adversarial learning (SRGAN)
config.TRAIN.n_epoch = 500
config.TRAIN.lr_decay = 0.1
config.TRAIN.decay_every = int(config.TRAIN.n_epoch / 2)

## train set location
config.TRAIN.hr_img_path = '/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/train/msx/'
config.TRAIN.lr_img_path = '/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/train/msx_orig_size'

config.VALID = edict()
## test set location
config.VALID.hr_img_path = '/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/val/msx/'
config.VALID.lr_img_path = '/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/val/msx_orig_size'

def log_config(filename, cfg):
    with open(filename, 'w') as f:
        f.write("================================================\n")
        f.write(json.dumps(cfg, indent=4))
        f.write("\n================================================\n")
