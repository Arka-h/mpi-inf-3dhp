import os
import argparse
import os

def get_frames(base_dir, idx):
    """
    Generate frames from video files in the specified directory.

    Args:
        base_dir (str): The base directory containing the video files.
        idx (int): The index of camera no./vdo file to generate frames from.

    Returns:
        None
    """
    for S in os.listdir(base_dir):
        if S.startswith('S'):
            for seq in os.listdir(f'{base_dir}/{S}'):
                for subdir in ['ChairMasks', 'FGmasks', 'imageSequence']:
                    if not os.path.exists(f'{base_dir}/{S}/{seq}/{subdir}/frames_{idx}'): # Only generate if not already present
                        os.mkdir(f'{base_dir}/{S}/{seq}/{subdir}/frames_{idx}')
                        os.system(f'ffmpeg -i "{base_dir}/{S}/{seq}/{subdir}/video_{idx}.avi" -qscale:v 1 "{base_dir}/{S}/{seq}/{subdir}/frames_{idx}/img_{idx}_%06d.jpg"')
                    

if __name__ == '__main__':
    split='subset'
    base_dir = f'/home/sampath/arka/gen-ai/sd-dino/data/mpi_inf_3dhp/{split}'
    idx=int(input('Enter index: '))
    get_frames(base_dir, idx)