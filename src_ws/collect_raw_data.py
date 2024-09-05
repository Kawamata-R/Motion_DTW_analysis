import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# inital setting
pair_num = 19
input_condname_list = ['dor','integration','solo']
output_condname_list = ['dividing','integration','solo']
sub_num = 2

pair_trial = 1
cond_trial = 1
sub_trial = 1
# 元のフォルダと移動先のフォルダのパスを指定

source_folder = '../motion_data/raw_data/all_data/'
destination_folder = '../motion_data/raw_data/raw_motion_data/'

def copy_motionfile(input_csv,output_csv):
    # 移動先のフォルダが存在しない場合は作成
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # ファイルを移動
    shutil.copy2(input_csv, output_csv)
    print(f'copyed : {output_csv}')
        
def main():
#    for pair in range(pair_num):
    for pair in range(1):
        for cond_trial in range(len(input_condname_list)):
            for sub in range(sub_num):
                pair_trial = pair+19
                sub_trial = sub+1
                
                input_path = source_folder+'pair'+str(pair_trial)+'/'+input_condname_list[cond_trial]+'/session1/Participant/'
                input_csv_name  = input_path+'transform_participant'+str(sub_trial)+'.csv'
                output_csv_name = destination_folder+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+output_condname_list[cond_trial]+'.csv'

                copy_motionfile(input_csv_name,output_csv_name)
# パスを指定して実行する例
if __name__ == '__main__':
    main()
