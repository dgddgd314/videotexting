import cv2
import os
import math
import numpy as np
import time

# 기본적인 setting
video_path = r"C:\Users\82103\Desktop\imagetext\sample.mp4" # 파일 경로
framerate = 3 # save 1 image for every (framerate) frames
size = 20 # 몇 개의 픽셀이 하나의 글자로 표현되는가?

# main2. img2txt
def img2txt(cnt):
    output_directory = os.path.join(folder_path, f"txt")

    # 이미지의 높이와 너비 얻기
    height, width = frame.shape

    # 저장할 행렬 만들기
    rows = math.floor(height / size)
    cols = math.floor(width / size)
    pixel = np.empty((rows, cols), dtype=str)

    symbol = [" ", ".", "*", "+", "#", "%", "@", "■"]

    # 블록 순회하며 평균 밝기 값 계산
    for y in range(rows):
        for x in range(cols):
            block = frame[y * size: (y + 1) * size, x * size: (x + 1) * size]
            block_mean = np.mean(block)
            pixel[y, x] = symbol[math.floor(block_mean/(256/len(symbol)))]
                
    # 만들어진 텍스트 저장
    np.save(os.path.join(folder_path, rf"txt\txt_{cnt:04d}.npy"), pixel)
    cnt += 1

# 터미널 지우기
def clear_terminal(): 
    os.system('cls')
    
def sleep_one_frame():
    time.sleep(framerate/fps)  # 나중에 combine할 때는 framerate/fps로 대체
    
def print_array():
    x,y = loaded_matrix.shape
    for i in range (x):
        for j in range (y):
            print(loaded_matrix[i][j]*2, end = '')
        print()

# main1. video2imgs
if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file '{video_path}' not found.")
else:
    # 텍스트 파일 만들기
    folder_path = os.path.dirname(video_path)
    output_directory = os.path.join(folder_path, f"txt")

    # Output_directory 폴더가 있는지?
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Image Folder created successfully.")
    else:
        print(f"Folder already exists.")
        
    cnt = 0

    # 영상 파일 열기
    cap = cv2.VideoCapture(video_path)
    
    # 영상 파일 분석
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    second = total_frames/fps
    result_frames = math.ceil(total_frames/framerate)
    print(f"Video fps : {fps}, Total {second} sec/{total_frames} frames. Expecting {result_frames} frames as result. Start image extraction...")

    # 프레임 인덱스 초기화
    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 각 프레임을 사진으로 저장
        if frame_index % framerate == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img2txt(cnt)
            cnt += 1

        frame_index += 1

    # 영상 파일 닫기
    cap.release()
    cv2.destroyAllWindows()

    # 이미지화 작업 완료 메시지 및 파일 위치 출력
    print(f"Txt extraction completed. Total {cnt} txts.")
    print(f"Txt files saved in: {os.path.abspath(output_directory)}")
    
    # main3. txtshow
    # 텍스트 파일이 없을 때 까지 계속 돌기 
    cnt = 0
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
        
    
    
    
    