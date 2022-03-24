import sys
from pathlib import Path
import numpy as np
import os
import argparse
from tqdm.autonotebook import tqdm  

MASTER_SEED = 548131
NUM_MOCAPS = 13225
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 2.93\blender.exe"
CAM_HEIGHT = [0.9, 0.9]
CAM_DIST = [3.9, 3.9]
RESOLUTION = [256, 256]
SPLIT = 'train'
DATASET_NAME_CUSTOM = 'ntu_custom'


def render_id(idx, zrot_deg):
    cmd = f'"{BLENDER_PATH}" -b -t 1 -P main.py --'
    cmd += f' --datasetname ntu --split_name {SPLIT} --smpl_estimation_method vibe --smpl_result_path ../data/ntu/vibe/{SPLIT} --vidlist_path vidlists/ntu/{SPLIT}.txt'
    cmd += f' --bg_path ../data/ntu/backgrounds/ --output_path ../data/surreact/{DATASET_NAME_CUSTOM}/vibe --tmp_path ../data/surreact/{DATASET_NAME_CUSTOM}/tmp_vibe_output'
    cmd += f' --idx {idx} --frand 1 --resx {RESOLUTION[0]} --resy {RESOLUTION[1]} --cam_dist {CAM_DIST[0]} {CAM_DIST[1]} --cam_height {CAM_HEIGHT[0]} {CAM_HEIGHT[1]} --zrot_euler {zrot_deg} --track_order 0'

    print(f'Executing {cmd}')
    os.system(cmd)
s    
def main():
    p = argparse.ArgumentParser(description='Renders samples for the dataset.')
    opts = p.parse_args()

    np.random.seed(MASTER_SEED)

    with tqdm(total=NUM_MOCAPS) as pbar:
        for idx in range(NUM_MOCAPS):
            zrot_deg = np.random.uniform(0, 360)
            render_id(idx, zrot_deg)
            pbar.update(1)



if __name__ == "__main__":
    main()