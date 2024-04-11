import scipy.io
import numpy as np
import torch

def convert(path):
    """
    Converts annotation data from a .mat file to a .pt file using PyTorch.

    Args:
        path (str): The path to the directory containing the .mat file.

    Returns:
        None
    """
    
    # Seq1 : Decoded 6417 frames
    mat_file = f'{path}/annot.mat'
    mat = scipy.io.loadmat(mat_file)
    mat = {k:v for k, v in mat.items() if k[0] != '_'}
    # ['annot2', 'annot3', 'cameras', 'frames', 'univ_annot3']
    # parsing arrays in arrays in mat file  
    # process annot2[:,:] object => np.array # (14,1) (6416, 56)
    annot2 = np.array(list(mat['annot2'].squeeze()))
    a,b,_ = annot2.shape
    mat['annot2'] = annot2.reshape(a,b,-1,2) # 28*2=56
    # process annot3[:,:] object => np.array # (14,1) (6416, 84)
    annot3 = np.array(list(mat['annot3'].squeeze()))
    a,b,_ = annot3.shape
    mat['annot3'] = annot3.reshape(a,b,-1,3) # 28*3=84
    # process univ_annot3[:,:] object => np.array # (14,1) (6416, 84)
    univ_annot3 = np.array(list(mat['univ_annot3'].squeeze()))
    a,b,_ = univ_annot3.shape
    mat['univ_annot3'] = univ_annot3.reshape(a,b,-1,3)
    # cameras # (1,14)
    mat['cameras'] = mat['cameras'].squeeze()
    # frames # (6416,1)
    mat['frames'] = mat['frames'].squeeze()

    torch.save(mat, f'{path}/annot.pt')
    print("SUMMARY\n", { key: mat[key].shape for key in 
        ['annot2', 'annot3', 'cameras', 'frames', 'univ_annot3'] })

if __name__ == '__main__':
    split='subset'
    S = 'S'+input('enter subj id:')
    Seq = 'Seq'+input('enter Seq:')
    convert(f'../{split}/{S}/{Seq}')