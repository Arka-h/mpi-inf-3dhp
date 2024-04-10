from get_frames import *
from mpii_get_camera_set import *
from mpii_get_joint_set import *
from mpii_get_sequence_info import *
from convert import *

base_dir = '/home/sampath/arka/gen-ai/sd-dino/data/mpi_inf_3dhp'
# get frames by running ffmpeg
get_frames(base_dir)

# For all files in dataset, convert to annot.pt
for S in os.listdir(base_dir):
    if S.startswith('S'):
        for Seq in os.listdir(f'{base_dir}/{S}'):
            convert(f'{base_dir}/{S}/{Seq}')

# Select the joint set
jnt_set = mpii_get_joint_set('relevant') # Takes one of 3: ('all', 'relevant', 'extended')

# Select the camera set
cam_set = mpii_get_camera_set('vnect') # Takes one of 5: ('ceiling', 'mm3d_chest', 'regular', 'relevant', 'vnect')

# ================================================================================================================

# Query user for specific instances
S=int(input('select subject#:'))
Seq=int(input('select seq#:'))

# Sequence info [augmentable?,fps?,#frames?]
seq_info = mpii_get_sequence_info(S, Seq)

# TODO: create tools to visualize a few frames
# Visualize 2d-pose here
# Visualize 3d-pose here