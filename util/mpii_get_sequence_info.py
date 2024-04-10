def mpii_get_sequence_info(subject_id, sequence):
    """
    Retrieves information about a specific sequence for a given subject.

    Args:
        subject_id (int): The ID of the subject.
        sequence (int): The sequence number.

    Returns:
        dict: A dictionary containing information about the sequence, including augmentability and frame details.
    """
    seq_info = [
        [(True, False, False, True, 25, 6416),(False, True, False, True, 50, 12430)],
        [(True, False, False, True, 25, 6502),(True, True, True, True, 25, 6081)],
        [(True, False, False, True, 50, 12488),(True, True, True, True, 50, 12283)],
        [(True, False, False, True, 25, 6171),(False, True, False, True, 25, 6675)],
        [(True, False, False, True, 50, 12820),(True, True, True, True, 50, 12312)],
        [(True, False, False, True, 25, 6188),(True, True, True, True, 25, 6145)],
        [(True, True, True, True, 25, 6239),(True, False, False, True, 25, 6320)],
        [(True, True, True, True, 25, 6468),(True, False, False, True, 25, 6054)]
    ]
    
    bg_augmentable, ub_augmentable, lb_augmentable, chair_augmentable, fps, num_frames = seq_info[subject_id-1][sequence-1]
    return {'bg_augmentable':bg_augmentable,
            'ub_augmentable':ub_augmentable,
            'lb_augmentable':lb_augmentable,
            'chair_augmentable':chair_augmentable,
            'fps':fps,
            'num_frames':num_frames}
    
if __name__=='__main__':
    subject_id = int(input('Enter subject id:'))
    sequence = int(input('Enter sequence id:'))
    print(subject_id, sequence)
    print(mpii_get_sequence_info(subject_id, sequence))