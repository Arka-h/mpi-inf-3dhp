import os
import argparse
def get_frames(base_dir, args):
    """
    Creates frames from video files in specified directories using ffmpeg.

    Args:
        base_dir (str): The base directory containing the video files.
        args (list): List of arguments, including the index for frame extraction.

    Returns:
        None
    """
    print(args)
    idx=args.index
    for S in os.listdir(base_dir):
        if S.startswith('S'):
            for seq in os.listdir(f'{base_dir}/{S}'):
                for subdir in ['ChairMasks', 'FGmasks', 'imageSequence']:
                    if not os.path.exists(f'{base_dir}/{S}/{seq}/{subdir}/frames_{idx}'): # Only generate if not already present
                        os.mkdir(f'{base_dir}/{S}/{seq}/{subdir}/frames_{idx}')
                        os.system(f'ffmpeg -i "{base_dir}/{S}/{seq}/{subdir}/video_{idx}.avi" -qscale:v 1 "{base_dir}/{S}/{seq}/{subdir}/frames_{idx}/img_{idx}_%06d.jpg"')
                    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--index', type=int, default=0)
    args = parser.parse_args()
    base_dir = '/home/sampath/arka/gen-ai/sd-dino/data/mpi_inf_3dhp'
    get_frames(base_dir, args)