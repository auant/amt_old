import os
from argparse import ArgumentParser


def rename_files(folder_path, start_idx, end_idx, delta):
    for i in range(end_idx, start_idx-1, -1):
        os.rename(f"{folder_path}/{i}.jpg", f"{folder_path}/{i+delta}.jpg")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--folder_path", type=str)
    args = parser.parse_args()
    rename_files(args.folder_path, 40, 49, 4)
    rename_files(args.folder_path, 30, 39, 3)
    rename_files(args.folder_path, 20, 29, 2)
    rename_files(args.folder_path, 10, 19, 1)
