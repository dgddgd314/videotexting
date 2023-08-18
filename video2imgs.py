import cv2
import os
import math

# 영상 파일 경로
video_path = r"C:\Users\82103\Desktop\imagetext\sample.mp4"

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file '{video_path}' not found.")
else:
    # 이미지 파일 만들기
    folder_path = os.path.dirname(video_path)
    output_directory = os.path.join(folder_path, f"image")

    # Output_directory 폴더가 있는지?
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Image Folder created successfully.")
    else:
        print(f"Folder already exists.")
        
    framerate = 6 # save 1 image for every (framerate) frames
    cnt = 0

    # 영상 파일 열기
    cap = cv2.VideoCapture(video_path)
    
    # 영상 파일 분석
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    second = total_frames/fps
    result_frames = math.ceil(total_frames/framerate)
    print(f"Video fps : {fps}, Total {second} sec/{total_frames} frames. Expecting {result_frames} frames as result.Start image extraction...")

    # 프레임 인덱스 초기화
    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 각 프레임을 사진으로 저장
        if frame_index % framerate == 0:
            frame_filename = f'{output_directory}/frame_{cnt:04d}.jpg'
            cv2.imwrite(frame_filename, frame)
            
            cnt += 1
            print(f"{cnt}/{result_frames} done")

        frame_index += 1

    # 영상 파일 닫기
    cap.release()
    cv2.destroyAllWindows()

    # 이미지화 작업 완료 메시지 및 파일 위치 출력
    print(f"Image extraction completed. Total {cnt} images.")
    print(f"Image files saved in: {os.path.abspath(output_directory)}")
    print("")
