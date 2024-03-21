import face_recognition
import cv2

# Load images
img1_path = 'Images/1.jpg'
img2_path = 'Images/2.jpg'

# Convert images to RGB
img1_rgb = cv2.cvtColor(cv2.imread(img1_path), cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(cv2.imread(img2_path), cv2.COLOR_BGR2RGB)

# Create face encodings for both images
face_encodings_img1 = face_recognition.face_encodings(img1_rgb)[0]
face_encodings_img2 = face_recognition.face_encodings(img2_rgb)[0]

# Compare face encodings
result = face_recognition.compare_faces([face_encodings_img1], face_encodings_img2)

# Print result
print("Are the faces in img1 and img2 the same person?", result)
