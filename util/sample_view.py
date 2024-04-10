import torch
S = 'S'+input('enter subj id:')
Seq = 'Seq'+input('enter Seq:')

annot = torch.load(f'../{S}/{Seq}/annot.pt')
print("shapes\n", 
    { key: annot[key].shape for key in 
        ['annot2', 'annot3', 'cameras', 'frames', 'univ_annot3'] })