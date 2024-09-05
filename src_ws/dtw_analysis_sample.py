
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

# DTWパスをプロットする関数
def plot_dtw_path(time_series_1, time_series_2, path, output_file):
    plt.figure(figsize=(10, 5))

    # 時系列データ1をプロット
    plt.plot(time_series_1, label='Participant 1', color='blue')
    # 時系列データ2をプロット
    plt.plot(time_series_2, label='Participant 2', color='orange')

    # ワーピングパスをプロット
    for (i, j) in path:
        plt.plot([i, j], [time_series_1[i], time_series_2[j]], color='gray', linestyle='--', linewidth=0.5)

    plt.title('DTW Warping Path'+condname_list[cond_trial])
    plt.legend()
    plt.tight_layout()

    # プロットをPNGとして保存
    plt.savefig(output_file)
    plt.show()

def main(input1_csv, input2_csv, output_png):
    print(f'#=====================================================#\nSTART dtw sample code\n input 1:'+input1_csv+'\ninput 2:'+input2_csv)
    # CSVファイルを読み込む
    data1 = pd.read_csv(input1_csv)
    data2 = pd.read_csv(input2_csv)
    
    # 時系列データの列を選択する (例: column1, column2)
    time_series_1 = data1['y_preprocessed'].values.tolist()
    time_series_2 = data2['y_preprocessed'].values.tolist()

    print(f'Time Series 1 Shape: {type(time_series_1)}')
    print(f'Time Series 2 Shape: {type(time_series_2)}')
    print(f'Time Series 1 Data: {time_series_1[:5]}')  # 最初の5つの値をプリントして確認
    print(f'Time Series 2 Data: {time_series_2[:5]}')  # 最初の5つの値をプリントして確認

    # DTWを計算する
    #distance, path = fastdtw(time_series_1, time_series_2, dist=euclidean)
    distance, path = fastdtw(time_series_1, time_series_2)

    # DTWの結果をプロットして保存
    plot_dtw_path(time_series_1, time_series_2, path, output_png)
    print(f'DTW distance: {distance}')
    print(f'Plot saved as {output_png}')

# パスを指定して実行する例
if __name__ == '__main__':
    input_path = '../motion_data/extracted_motion_data/'
    for pair in range(1):
        for cond_trial in range(len(condname_list)):           
            pair_trial = pair+1
            input_csv_sub1 = input_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+condname_list[cond_trial]+'.csv'  # ここに入力CSVファイルのパスを指定
            input_csv_sub2 = input_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial+1)+'_'+condname_list[cond_trial]+'.csv'  # ここに入力CSVファイルのパスを指定
    
            figure_path = '../figure_ws/dtw_path_fig/'
            output_png = figure_path+'transform_pair'+str(pair_trial)+'_sub'+str(sub_trial)+'_'+condname_list[cond_trial]+'.png'   # ここに出力PNGファイルのパスを指定
            main(input_csv_sub1,input_csv_sub2, output_png)
