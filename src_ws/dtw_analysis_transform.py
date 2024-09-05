
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


# inital setting
pair_num = 19
condname_list = ['dividing','integration','solo']
sub_num = 2

pair_trial = 1
cond_trial = 0
sub_trial = 1
plot_flug = False
debug_mode = False

# DTWパスをプロットする関数
def plot_dtw_path(time_series_1, time_series_2, path, output_file,distance,trans):
    plt.figure(figsize=(16, 8))

    # 時系列データ1をプロット
    plt.plot(time_series_1, label='Participant 1', color='blue')
    # 時系列データ2をプロット
    plt.plot(time_series_2, label='Participant 2', color='orange')

    # ワーピングパスをプロット
    for (i, j) in path:
        plt.plot([i, j], [time_series_1[i], time_series_2[j]], color='gray', linestyle='--', linewidth=0.5)
    
    
    if trans == 0: 
        plt.title('DTW Warping Path'+condname_list[cond_trial]+' distance_x:'+str(distance))
    elif trans == 1: 
        plt.title('DTW Warping Path'+condname_list[cond_trial]+' distance_y:'+str(distance))
    elif trans == 2: 
        plt.title('DTW Warping Path'+condname_list[cond_trial]+' distance_z:'+str(distance))
    
    plt.legend()
    plt.tight_layout()

    # プロットをPNGとして保存
    plt.savefig(output_file)
    if plot_flug:
        plt.show()
        
        
def main(input_csv_path,result_figure_path):
    print(f'#=====================================================#\nSTART dtw position analysis code')
    
    for cond_trial in range(len(condname_list)):
        print(f'analysis condinton : {condname_list[cond_trial]}')
        for pair in range(pair_num):
            pair_trial = pair+1
            sub_trial = 1
            print(f'analysis pair is : pair{str(pair_trial)}')
            input_csv_sub1 = input_csv_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+condname_list[cond_trial]+'.csv'  # ここに入力CSVファイルのパスを指定
            input_csv_sub2 = input_csv_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial+1)+'_'+condname_list[cond_trial]+'.csv'  # ここに入力CSVファイルのパスを指定
    
            output_png = result_figure_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'-sub'+str(sub_trial+1)+'_'+condname_list[cond_trial]  # ここに出力PNGファイルのパスを指定
            # CSVファイルを読み込む
            data1 = pd.read_csv(input1_csv)
            data2 = pd.read_csv(input2_csv)
            
            # caluculate dtw (x,y,,z,ave)
            for trans in range(4):
                if trans == 0:
                    
                    # 時系列データ:x
                    time_series_1 = data1['x_preprocessed'].values.tolist()
                    time_series_2 = data2['x_preprocessed'].values.tolist()
                    distance_x, path = fastdtw(time_series_1, time_series_2)
                    output_png_x = output_png+'_x.png'
                    # DTWの結果をプロットして保存
                    plot_dtw_path(time_series_1, time_series_2, path, output_png_x,distance_x,trans)
                    print(f'Plot saved as {output_png_x}')

                        
                elif trans == 1:
                    # 時系列データ:y
                    time_series_1 = data1['y_preprocessed'].values.tolist()
                    time_series_2 = data2['y_preprocessed'].values.tolist()
                    distance_y, path = fastdtw(time_series_1, time_series_2)
                    output_png_y = output_png+'_y.png'
                    # DTWの結果をプロットして保存
                    plot_dtw_path(time_series_1, time_series_2, path, output_png_y,distance_y,trans)
                    print(f'Plot saved as {output_png_y}')

                    
                elif trans == 2:
                    # 時系列データ:z
                    time_series_1 = data1['z_preprocessed'].values.tolist()
                    time_series_2 = data2['z_preprocessed'].values.tolist()
                    distance_z, path = fastdtw(time_series_1, time_series_2)
                    output_png_z = output_png+'_z.png'
                    
                    # DTWの結果をプロットして保存
                    plot_dtw_path(time_series_1, time_series_2, path, output_png_z,distance_z,trans)
                    print(f'Plot saved as {output_png_z}')

                        
                elif trans == 3:
                    # 時系列データ:ave(x+y+z/3)
                    distance_ave = (distance_x+distance_y+distance_z)/3


            print(f'DTW distance_x: {distance_x} ,DTW distance_y: {distance_y} ,DTW distance_z: {distance_z} ,DTW distance_ave: {distance_ave}')













# パスを指定して実行する例
if __name__ == '__main__':
    input_path = '../motion_data/extracted_motion_data/'
    figure_path = '../figure_ws/dtw_path_fig/'
    main(input_path,figure_path)
            