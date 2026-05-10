import cv2
import os

video_path = 'assets/raw_files/video2.mp4'
output_dir = 'assets/video_frames'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    out_path = os.path.join(output_dir, f'frame_{count:04d}.jpg')
    cv2.imwrite(out_path, frame)

cap.release()
print(f'Extracted {count} frames.')
