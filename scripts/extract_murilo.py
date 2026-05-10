import cv2
import os

video_path = "VIDEO MURILO.mp4"
output_dir = "assets/video_frames_murilo"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)
count = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save frame
    frame_name = f"frame_{count:04d}.jpg"
    cv2.imwrite(os.path.join(output_dir, frame_name), frame)
    count += 1

cap.release()
print(f"Extracted {count-1} frames.")
