import shutil

vigilance_indices = [10, 21, 32, 43]
img_1_indices = [123, 124, 125, 126]
img_2_indices = [127, 128, 129, 130]

for i in range(4):
    v_idx = vigilance_indices[i]
    i1_idx = img_1_indices[i]
    i2_idx = img_2_indices[i]
    im1 = f"../shir/htmls_80/inputs/flowers_inference/structure/{i1_idx}.jpg"
    im2 = f"../shir/htmls_80/inputs/flowers_inference/structure/{i2_idx}.jpg"
    shutil.copy(im1, f"./flowers/structures/{v_idx}.jpg")
    shutil.copy(im1, f"./flowers/textures/{v_idx}.jpg")
    shutil.copy(im1, f"./flowers/ours/{v_idx}.jpg")
    shutil.copy(im2, f"./flowers/sa/{v_idx}.jpg")
    shutil.copy(im2, f"./flowers/sd/{v_idx}.jpg")
    shutil.copy(im2, f"./flowers/splice/{v_idx}.jpg")
    shutil.copy(im2, f"./flowers/wct2/{v_idx}.jpg")
