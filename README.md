# Motion DTW(Dynamic Time Wraping) analysis
#### date   : 2024-09-02
#### author : kawamata
#### brief  : ロボット操作の同期解析をDTWにて行う

## 0.Contents
### 0.1. Enviromment
 - OS : windows 11
 - python : 3.10.12
 - docker os : ubuntu 22
### 0.2. Directory
 - raw_data
 - src_ws
 - figure_ws
 - result_doc_ws
 - dockerfile_ws

## 1. Command
### 1.1. Docker set up
 - docker file build 
 ```bash
 cd dockerfiel_ws
 docker build  . -t dtw_ws_image
 ```
 - make container
 
