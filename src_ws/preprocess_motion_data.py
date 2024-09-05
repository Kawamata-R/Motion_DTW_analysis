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

session_time = {'prerest':60,'task':180,'postrest':30} #[sec]


pair_trial = 1
cond_trial = 1
sub_trial = 1
# 元のフォルダと移動先のフォルダのパスを指定

all_raw_data_dir = '../motion_data/raw_data/all_data/'
raw_motion_dir = '../motion_data/raw_data/raw_motion_data/'
extracted_data_dir = '../motion_data/extracted_motion_data/'

#file コピー
def copy_motionfile(input_csv,output_csv):
    # 移動先のフォルダが存在しない場合は作成
    if not os.path.exists(raw_motion_dir):
        os.makedirs(raw_motion_dir)

    # ファイルを移動
    shutil.copy2(input_csv, output_csv)
    print(f'copyed : {output_csv}')
    
# task字のデータ抽出 baselien fitting
def extracted_task_baselined_data(input_df):
    print('extracted task data')
    trigger_data = input_df['triggerValue'].values.tolist()
    print(f'trigger data : {trigger_data[:5]}')
    trigger_index = ([i for i, x in enumerate(trigger_data) if x == 1.0])
    print(f'trigger index : {trigger_index}')
    extracted_task_df = input_df[trigger_index[1]:trigger_index[2]]
    print('baseline fitting')
    baseline_vale = input_df[trigger_index[1]-1:trigger_index[1]]
    print(f'baseline_vale : index{trigger_index[1]-1} :\n{baseline_vale}')
    extracted_task_df.loc[:,'x_preprocessed'] = extracted_task_df['x']-baseline_vale.loc[trigger_index[1]-1,'x']# x:col num = 2
    extracted_task_df.loc[:,'y_preprocessed'] = extracted_task_df['y']-baseline_vale.loc[trigger_index[1]-1,'y']# x:col num = 3
    extracted_task_df.loc[:,'z_preprocessed'] = extracted_task_df['z']-baseline_vale.loc[trigger_index[1]-1,'z']# x:col num = 4
    if len(extracted_task_df) != 0:
        print('extracted and baselined raw data !')
        return extracted_task_df
    else:
        print('failed to extracting ')
        return False
    

def collect_rawdata(motion_csv,process_csv):
    print('collect raw data')
    motion_data = pd.read_csv(motion_csv)
    process_data = pd.read_csv(process_csv)
    all_collect_data = pd.concat([process_data, motion_data], axis=1)
    collect_data = all_collect_data.drop(columns=['duration','qx','qy','qz','qw'])
    if len(collect_data) != 0:
        print('collected raw data !')
        return collect_data
    else:
        print('failed to collecting ')
        return False

def main():
#    for pair in range(pair_num):
    for pair in range(1):
        for cond_trial in range(len(input_condname_list)):           
        #for cond_trial in range(1):
            for sub in range(sub_num):
                pair_trial = pair+1
                sub_trial = sub+1
                
                input_path = all_raw_data_dir+'pair'+str(pair_trial)+'/'+input_condname_list[cond_trial]+'/session1/'
                input_motion_csv_name  = input_path+'Participant/transform_participant'+str(sub_trial)+'.csv'
                input_process_csv_name  = input_path+'ProcessInfo/processDuration.csv'
                output_csv_name = raw_motion_dir+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+output_condname_list[cond_trial]+'.csv'
                raw_data_df = collect_rawdata(input_motion_csv_name,input_process_csv_name)
                output_csv_name = extracted_data_dir+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+output_condname_list[cond_trial]+'.csv'     
                extracted_df = extracted_task_baselined_data(raw_data_df)
                #copy_motionfile(input_csv_name,output_csv_name)
                extracted_df.to_csv(output_csv_name) 
                
                
                
# パスを指定して実行する例
if __name__ == '__main__':
    main()
