from get_frames import *
from mpii_get_camera_set import *
from mpii_get_joint_set import *
from mpii_get_sequence_info import *
from convert import *

split=input('select split ["subset", "test", "train"]: ')
base_dir = f'/home/sampath/arka/gen-ai/sd-dino/data/mpi_inf_3dhp/{split}'
# get frames by running ffmpeg
get_frames(base_dir, 0) # Only generate the frames for camera 0 right now

# For all files in dataset, convert to annot.pt
for S in os.listdir(base_dir):
    if S.startswith('S'):
        for Seq in os.listdir(f'{base_dir}/{S}'):
            convert(f'{base_dir}/{S}/{Seq}')

# Select the joint set {jnt_idx, jnt_parents_o1, jnt_parents_o2, jnt_names}
jnt_set = mpii_get_joint_set('relevant') # Takes one of 3: ('all', 'relevant', 'extended')

# Select the camera set [indices]
# cam_set = mpii_get_camera_set('vnect') # Takes one of 5: ('ceiling', 'mm3d_chest', 'regular', 'relevant', 'vnect')
cam_set = [0] # Only select camera 0 right now
# ================================================================================================================

# Query user for specific instances
S=int(input('select subject#:'))
Seq=int(input('select seq#:'))
# Sequence info [augmentable?,fps?,#frames?]
seq_info = mpii_get_sequence_info(S, Seq)

# TODO: create tools to visualize a few frames
annot = torch.load(f'{base_dir}/S{S}/Seq{Seq}/annot.pt') # pick the annotations for the selected subj S and Seq #
# annot keys : 'annot2', 'annot3', 'cameras', 'frames', 'univ_annot3'
print(annot['cameras'])