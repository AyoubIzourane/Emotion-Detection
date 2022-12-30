from deepface import DeepFace

face_analysis = DeepFace.analyze(img_path = "man.jpg")

print(face_analysis["emotion"])
print(face_analysis["dominant_emotion"])
