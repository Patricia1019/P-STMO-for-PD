import numpy as np
import pdb
import pandas as pd
import math

file_path = './outputs/test_3d_output_H013_GA_02_20210922_133913_postprocess.npy'
motion_path = './motion_cap/H013_GA_02_jointsangle.csv'

poses = np.load(file_path)[:,5:,:]
motion = pd.read_csv(motion_path)

joints = np.array(['Pelvis', 'RHip', 'RKnee', 'RAnkle', 'RToe', 'Site', 'LHip', 'LKnee', \
    'LAnkle', 'LeftToe', 'Site', 'Spine', 'Spine1', 'Neck', 'Head', 'Site', 'LShoulder',\
         'LShoulder', 'LElbow', 'LWrist', 'LThumb', 'Site', 'L_Wrist_End', 'Site', 'RShoulder', \
            'RShoulder', 'RElbow', 'RWrist', 'RThumb', 'Site', 'R_Wrist_End', 'Site'])
joints = np.delete(joints,[4, 5, 9, 10, 11, 16, 20, 21, 22, 23, 24, 28, 29, 30, 31])
joints:array(['Pelvis', 'RHip', 'RKnee', 'RAnkle', 'LHip', 'LKnee', 'LAnkle',
       'Spine1', 'Neck', 'Head', 'Site', 'LShoulder', 'LElbow', 'LWrist',
       'RShoulder', 'RElbow', 'RWrist'], dtype='<U11')
def angle3pt(p, q, r):
    if p[0]!=0 and q[0]!=0 and r[0]!=0:
        ang = math.degrees(math.atan2(r[1]-q[1], r[0]-q[0]) - math.atan2(p[1]-q[1], p[0]-q[0]))
        return ang + 360 if ang < 0 else ang


pdb.set_trace()