mpii_data_path = '../'

def mpii_get_camera_set(camera_set_name):
    if camera_set_name == 'regular':
        camera_set = list(range(14))  # Cameras with regular lenses, not fisheye
    elif camera_set_name == 'relevant':
        camera_set = list(range(11))  # All cameras except the ceiling mounted ones
    elif camera_set_name == 'ceiling':
        camera_set = list(range(11, 14))  # Top down views
    elif camera_set_name == 'vnect':
        camera_set = [0, 1, 2, 4, 5, 6, 7, 8]  # Chest high, knee high and 2 cameras angled down. Use for VNect @ SIGGRAPH 17
    elif camera_set_name == 'mm3d_chest':
        camera_set = [0, 2, 4, 7, 8]  # Subset of chest high, used in "Monocular 3D Human Pose Estimation in-the-wild Using Improved CNN supervision"
    else:
        camera_set = []
    return camera_set

def mpii_get_joint_set(joint_set_name):
    all_joint_names = ['spine3', 'spine4', 'spine2', 'spine', 'pelvis', 
                       'neck', 'head', 'head_top', 'left_clavicle', 'left_shoulder', 'left_elbow', 
                       'left_wrist', 'left_hand',  'right_clavicle', 'right_shoulder', 'right_elbow', 'right_wrist', 
                       'right_hand', 'left_hip', 'left_knee', 'left_ankle', 'left_foot', 'left_toe', 
                       'right_hip' , 'right_knee', 'right_ankle', 'right_foot', 'right_toe']
    
    if joint_set_name == 'all':
        joint_idx = list(range(1, 29))
        joint_parents_o1 = [3, 1, 4, 5, 5, 2, 6, 7, 6, 9, 10, 11, 12, 6, 14, 15, 16, 17, 5, 19, 20, 21, 22, 5, 24, 25, 26, 27]
        joint_parents_o2 = [4, 3, 5, 5, 5, 1, 2, 6, 2, 6, 9, 10, 11, 2, 6, 14, 15, 16, 4, 5, 19, 20, 21, 4, 5, 24, 25, 26]
        joint_names = all_joint_names
    elif joint_set_name == 'relevant':
        joint_idx = [8, 6, 15, 16, 17, 10, 11, 12, 24, 25, 26, 19, 20, 21, 5, 4, 7]
        joint_parents_o1 = [2, 16, 2, 3, 4, 2, 6, 7, 15, 9, 10, 15, 12, 13, 15, 15, 2]
        joint_parents_o2 = [16, 15, 16, 2, 3, 16, 2, 6, 16, 15, 9, 16, 15, 12, 15, 15, 16]
        joint_names = [all_joint_names[i-1] for i in joint_idx]
    elif joint_set_name == 'extended':
        joint_idx = [8, 6, 15, 16, 17, 10, 11, 12, 24, 25, 26, 19, 20, 21, 5, 4, 7, 18, 13, 28, 23]
        joint_parents_o1 = [2, 16, 2, 3, 4, 2, 6, 7, 15, 9, 10, 15, 12, 13, 15, 15, 2, 5, 8, 11, 14]
        joint_parents_o2 = [16, 15, 16, 2, 3, 16, 2, 6, 16, 15, 9, 16, 15, 12, 15, 15, 16, 4, 7, 10, 13]
        joint_names = [all_joint_names[i-1] for i in joint_idx]
    else:
        joint_idx = []
        joint_parents_o1 = []
        joint_parents_o2 = []
        joint_names = []
    
    return joint_idx, joint_parents_o1, joint_parents_o2, joint_names

def mpii_get_sequence_info(subject_id, sequence):
    ub_augmentable = False
    lb_augmentable = False
    bg_augmentable = False
    chair_augmentable = False
    fps = 25
    
    if subject_id == 1:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6416
        elif sequence == 2:
            ub_augmentable = True
            chair_augmentable = True
            num_frames = 12430
            fps = 50
    elif subject_id == 2:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6502
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6081
    elif subject_id == 3:
        fps = 50
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 12488
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 12283
    elif subject_id == 4:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6171
        elif sequence == 2:
            chair_augmentable = True
            ub_augmentable = True
            num_frames = 6675
    elif subject_id == 5:
        fps = 50
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 12820
        elif sequence == 2:
            chair_augmentable = True
            ub_augmentable = True
            bg_augmentable = True
            lb_augmentable = True
            num_frames = 12312
    elif subject_id == 6:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6188
        elif sequence == 2:
            ub_augmentable = True
            lb_augmentable = True
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6145
    elif subject_id == 7:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6239
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6320
    elif subject_id == 8:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6468
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6054
    
    return bg_augmentable, ub_augmentable, lb_augmentable, chair_augmentable, fps, num_frames
