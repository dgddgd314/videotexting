import cv2
import numpy as np
import math

# 이미지 파일 경로 설정
number = 10
image_path = rf"C:\Users\82103\Desktop\imagetext\sampleimage\frame_{number:04d}.jpg"
size = 30  # size or one letter

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
        
np.save(rf"C:\Users\82103\Desktop\imagetext\sampletxt\txt_{number:04d}.npy", pixel)




