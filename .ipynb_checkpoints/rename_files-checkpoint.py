import os
from argparse import ArgumentParser


def rename_files(folder_path, start_idx, end_idx, delta):
    for i in range(end_idx, start_idx-1, -1):
        os.rename(f"{folder_path}/{i}.jpg", f"{folder_path}/{i+delta}.jpg")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--folder_path", type=str)
    args = parser.parse_args()
    rename_files(f"{args.folder_path}/ours", 40, 49, 4)
    rename_files(f"{args.folder_path}/ours", 30, 39, 3)
    rename_files(f"{args.folder_path}/ours", 20, 29, 2)
    rename_files(f"{args.folder_path}/ours", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/sa", 40, 49, 4)
    rename_files(f"{args.folder_path}/sa", 30, 39, 3)
    rename_files(f"{args.folder_path}/sa", 20, 29, 2)
    rename_files(f"{args.folder_path}/sa", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/sd", 40, 49, 4)
    rename_files(f"{args.folder_path}/sd", 30, 39, 3)
    rename_files(f"{args.folder_path}/sd", 20, 29, 2)
    rename_files(f"{args.folder_path}/sd", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/structures", 40, 49, 4)
    rename_files(f"{args.folder_path}/structures", 30, 39, 3)
    rename_files(f"{args.folder_path}/structures", 20, 29, 2)
    rename_files(f"{args.folder_path}/structures", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/textures", 40, 49, 4)
    rename_files(f"{args.folder_path}/textures", 30, 39, 3)
    rename_files(f"{args.folder_path}/textures", 20, 29, 2)
    rename_files(f"{args.folder_path}/textures", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/splice", 40, 49, 4)
    rename_files(f"{args.folder_path}/splice", 30, 39, 3)
    rename_files(f"{args.folder_path}/splice", 20, 29, 2)
    rename_files(f"{args.folder_path}/splice", 10, 19, 1)
    
    rename_files(f"{args.folder_path}/wct2", 40, 49, 4)
    rename_files(f"{args.folder_path}/wct2", 30, 39, 3)
    rename_files(f"{args.folder_path}/wct2", 20, 29, 2)
    rename_files(f"{args.folder_path}/wct2", 10, 19, 1)
