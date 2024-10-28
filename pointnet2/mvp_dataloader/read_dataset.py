import h5py
import numpy as np

# HDF5 파일 열기
with h5py.File('./data/mvp_dataset/mvp_train_gt.h5', 'r') as f:
    # 각 데이터셋 불러오기
    labels = f['labels'][:]  # labels 데이터셋 불러오기
    complete_pcds = f['complete_pcds'][:]  # complete_pcds 데이터셋 불러오기
    colors = f['colors'][:]  # colors 데이터셋 불러오기
    normal = f['normal'][:]  # normal 데이터셋 불러오기
    
    # 데이터 타입 확인
    print(type(labels))  # 이때는 <class 'numpy.ndarray'>가 출력돼야 정상입니다.
    print(type(complete_pcds))
    print(type(colors))
    print(type(normal))
