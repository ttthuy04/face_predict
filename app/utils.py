# utils.py
import os
import csv
from datetime import datetime, timedelta
from collections import defaultdict

ATTENDANCE_DIR = "attendance"

def get_attendance_data(date):
    """
    Get attendance data for a specific date
    
    Args:
        date: Date string in format YYYY-MM-DD
    
    Returns:
        List of dictionaries with attendance records
    """
    filename = f"{ATTENDANCE_DIR}/attendance_{date}.csv"
    attendance_data = []
    
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                attendance_data.append({
                    'name': row.get('Name', ''),
                    'time': row.get('Time', '')
                })
    
    # Sort by time
    attendance_data.sort(key=lambda x: x['time'])
    return attendance_data

def get_attendance_stats():
    """
    Get statistics about attendance
    
    Returns:
        Dictionary with attendance statistics
    """
    stats = {
        'today': datetime.now().strftime("%Y-%m-%d"),
        'total_students': 0,
        'present_today': 0,
        'attendance_files': []
    }
    
    # Get today's attendance
    today_data = get_attendance_data(stats['today'])
    unique_students = set(record['name'] for record in today_data)
    stats['present_today'] = len(unique_students)
    
    # Get all attendance files
    if os.path.exists(ATTENDANCE_DIR):
        files = [f for f in os.listdir(ATTENDANCE_DIR) if f.endswith('.csv')]
        stats['attendance_files'] = sorted(files, reverse=True)
    
    # Count total students from dataset
    dataset_dir = "dataset"
    if os.path.exists(dataset_dir):
        stats['total_students'] = len([d for d in os.listdir(dataset_dir) 
                                       if os.path.isdir(os.path.join(dataset_dir, d))])
    
    return stats

def get_attendance_by_period(start_date, end_date):
    """
    Get attendance data for a date range
    
    Args:
        start_date: Start date string (YYYY-MM-DD)
        end_date: End date string (YYYY-MM-DD)
    
    Returns:
        Dictionary mapping dates to attendance records
    """
    result = {}
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    current = start
    while current <= end:
        date_str = current.strftime("%Y-%m-%d")
        result[date_str] = get_attendance_data(date_str)
        current += timedelta(days=1)
    
    return result

def export_attendance_csv(date, output_path=None):
    """
    Export attendance data to CSV file
    
    Args:
        date: Date string (YYYY-MM-DD)
        output_path: Optional output file path
    
    Returns:
        Path to exported file
    """
    if output_path is None:
        output_path = f"{ATTENDANCE_DIR}/export_{date}.csv"
    
    attendance_data = get_attendance_data(date)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Time'])
        for record in attendance_data:
            writer.writerow([record['name'], record['time']])
    
    return output_path

