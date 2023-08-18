import cv2
import numpy as np
import math
import os

folder_path = r"C:\Users\82103\Desktop\imagetext" # 병합 시 유의!
output_directory = os.path.join(folder_path, f"txt")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Txt Folder created successfully.")
else:
    print(f"Txt Folder already exists.")

# 이미지 파일 경로 설정
cnt = 0
size = 25 # 한 글자 당 프레임 수
while (True):
    image_path = os.path.join(folder_path, rf"image\frame_{cnt:04d}.jpg")
    if not os.path.exists(image_path):
        print(f"Txt convert finished. Total {cnt} frames.")
        break

    # 이미지 로드
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 이미지의 높이와 너비 얻기
    height, width = image.shape

    # 저장할 행렬 만들기
    rows = math.floor(height / size)
    cols = math.floor(width / size)
    pixel = np.empty((rows, cols), dtype=str)

    symbol = [" ", "^", "*", "!", "#", "%", "&", "$", "@", "■"]

    # 블록 순회하며 평균 밝기 값 계산
    for y in range(rows):
        for x in range(cols):
            block = image[y * size: (y + 1) * size, x * size: (x + 1) * size]
            block_mean = np.mean(block)
            pixel[y, x] = symbol[math.floor(block_mean/25.6)]
            
    # 만들어진 텍스트 저장
    np.save(os.path.join(folder_path, rf"txt\txt_{cnt:04d}.npy"), pixel)
    cnt += 1
    
