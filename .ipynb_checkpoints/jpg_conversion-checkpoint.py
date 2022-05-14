from PIL import Image
import glob
import os
from argparse import ArgumentParser


def jpg_conversion(folder_path):
    filenames = glob.glob(f"{folder_path}/**/*.png")
    for file in filenames:
        print(file)
        dirname = os.path.dirname(file)
        filename = os.path.basename(file).split(".")[0]
        img = Image.open(file)
        rgb_img = img.convert('RGB')
        rgb_img.save(f"{dirname}/{filename}.jpg")
        os.remove(file)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--folder_path", type=str)
    args = parser.parse_args()
    jpg_conversion(args.folder_path)
