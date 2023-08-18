import os
import numpy as np
import time

# 터미널 지우기
def clear_terminal(): 
    os.system('cls')
    
def sleep_one_frame():
    time.sleep(1/10)  # 나중에 combine할 때는 framerate/fps로 대체
    
def print_array():
    x,y = loaded_matrix.shape
    for i in range (x):
        for j in range (y):
            print(loaded_matrix[i][j]*2, end = '')
        print()
    
cnt = 0
folder_path = r"C:\Users\82103\Desktop\imagetext" # 병합 시 유의!

# 텍스트 파일이 없을 때 까지 계속 돌기 
while(True):
    # 파일이 있는지 체크.
    try:
        loaded_matrix = np.load(os.path.join(folder_path, rf"txt\txt_{cnt:04d}.npy"))
    except FileNotFoundError:
        print("Error: File not found. Could not load matrix. Maybe end of a video?")
        break
    
    # 한 프레임 돌리기
    clear_terminal()
    print_array()
    sleep_one_frame()
    cnt += 1
    
