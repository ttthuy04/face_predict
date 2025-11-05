# app/__init__.py
from app.face_recognizer import load_encodings, recognize_face
from app.utils import (
    get_attendance_data, 
    get_attendance_stats,
    get_attendance_by_period,
    export_attendance_csv
)

__all__ = [
    'load_encodings',
    'recognize_face',
    'get_attendance_data',
    'get_attendance_stats',
    'get_attendance_by_period',
    'export_attendance_csv'
]

