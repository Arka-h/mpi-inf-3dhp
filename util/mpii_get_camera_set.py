def mpii_get_camera_set(camera_set_name):
    """
    Retrieves a specific set of camera indices based on the provided camera set name.

    Args:
        camera_set_name (str): The name of the camera set to retrieve ('ceiling', 'mm3d_chest', 'regular', 'relevant', 'vnect').

    Returns:
        list: A list of camera indices corresponding to the specified camera set.
    """
    if camera_set_name == 'ceiling': # Top down views
        return list(range(11, 14))
    elif camera_set_name == 'mm3d_chest': # Subset of chest high, used in "Monocular 3D Human Pose Estimation in-the-wild Using Improved CNN supervision"
        return [0, 2, 4, 7, 8]
    elif camera_set_name == 'regular': # Cameras with regular lenses, not fisheye
        return list(range(14))
    elif camera_set_name == 'relevant': # All cameras except the ceiling mounted ones
        return list(range(11))
    elif camera_set_name == 'vnect': # Chest high, knee high and 2 cameras angled down. Use for VNect @ SIGGRAPH 17
        return [0, 1, 2, 4, 5, 6, 7, 8]
    else:
        return []

if __name__== '__main__':
    camera_set = ['ceiling', 'mm3d_chest', 'regular', 'relevant', 'vnect']
    camera_set_name = input(f'Enter camera set {camera_set}:')
    print(mpii_get_camera_set(camera_set_name))

