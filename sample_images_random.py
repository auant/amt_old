import random
import shutil
import glob
import os


def sample_images():
    filenames = glob.glob(f"../shir/htmls_80/baselines/flowers_inference/splice/*.jpg")
    all_indices = []
    for file in filenames:
        filename = os.path.basename(file).split(".")[0]
        all_indices.append(filename)
    
    sample_len = 50
    indices = random.sample(all_indices, sample_len)
    for i in range(sample_len):
        idx = indices[i]
        shutil.copy(f"../shir/htmls_80/inputs/flowers_inference/structure/{idx}.jpg", f"./flowers/structures/{i}.jpg")
        shutil.copy(f"../shir/htmls_80/inputs/flowers_inference/appearance/{idx}.jpg", f"./flowers/textures/{i}.jpg")
        shutil.copy(f"../../narekt/projects/splicing-in-scale/outputs/testing_pairs/flowers_inference_flowers-nn-lpips-id-0.1/{idx}.png", f"./flowers/ours/{i}.png")
        shutil.copy(f"../shir/htmls_80/baselines/flowers_inference/korean/{idx}.jpg", f"./flowers/sd/{i}.jpg")
        shutil.copy(f"../shir/htmls_80/baselines/flowers_inference/SA/{idx}.jpg", f"./flowers/sa/{i}.jpg")
        shutil.copy(f"../shir/htmls_80/baselines/flowers_inference/splice/{idx}.jpg", f"./flowers/splice/{i}.jpg")
        shutil.copy(f"../shir/htmls_80/baselines/flowers_inference/wct2/{idx}.jpg", f"./flowers/wct2/{i}.jpg")


sample_images()
