import random
import shutil
import glob
import os


def sample_images():
    root_folder = f"/home/projects/talide/splicing_shape_texture/shir/htmls/baselines/flowers_inference"
    target_folder = "./flowers"
    indices =  [0, 1, 4, 5, 7, 10, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 32, 33, 35, 37, 38, 39, 41,  50, 51, 53, 54, 55, 56, 57, 58, 62, 64, 69, 70, 72, 73, 74, 76, 79, 80, 81,  87, 99]
    cur_idx = 0

    for idx in indices:
        shutil.copy(f"{root_folder}/ours/{idx}.png", f"{target_folder}/ours/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/appearance/{idx}.png", f"{target_folder}/textures/{cur_idx}.png")
        cur_idx += 1


sample_images()
