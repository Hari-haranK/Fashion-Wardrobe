import mediapipe as mp
import cv2

# Load image
image_path = "img.jpeg"  # Replace with your image path
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

# Get keypoints
results = pose.process(img_rgb)

# Draw pose landmarks
if results.pose_landmarks:
    mp_drawing = mp.solutions.drawing_utils
    annotated = img.copy()
    mp_drawing.draw_landmarks(
        annotated, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Save or display
    cv2.imwrite("pose_output.jpg", annotated)
    print("✅ Pose estimation completed and saved as pose_output.jpg")
else:
    print("❌ No pose landmarks found.")
