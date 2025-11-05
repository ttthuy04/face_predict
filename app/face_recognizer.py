# face_recognizer.py
import face_recognition
import pickle
import cv2
import os

def load_encodings():
    """Load face encodings from pickle file"""
    encodings_file = "encodings/known_faces.pkl"
    if not os.path.exists(encodings_file):
        return [], []
    
    try:
        with open(encodings_file, "rb") as f:
            data = pickle.load(f)
        return data["encodings"], data["names"]
    except Exception as e:
        print(f"Error loading encodings: {e}")
        return [], []

def recognize_face(frame, known_encodings, known_names, tolerance=0.6):
    """
    Recognize faces in a frame
    
    Args:
        frame: OpenCV frame (BGR format)
        known_encodings: List of known face encodings
        known_names: List of names corresponding to encodings
        tolerance: Matching tolerance (lower = more strict)
    
    Returns:
        List of tuples: ((top, right, bottom, left), name)
    """
    if not known_encodings or not known_names:
        return []
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Find face locations and encodings
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    results = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare with known faces
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance)
        name = "Unknown"
        
        # Find best match
        if True in matches:
            # Use face distance for better accuracy
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = face_distances.argmin()
            
            if matches[best_match_index]:
                name = known_names[best_match_index]
        
        results.append(((top, right, bottom, left), name))
    
    return results