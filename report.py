# report.py
import pandas as pd
import os
from datetime import datetime

def generate_report():
    files = [f for f in os.listdir("attendance") if f.endswith(".csv")]
    all_data = []
    for f in files:
        date = f.split("_")[1].split(".")[0]
        df = pd.read_csv(f"attendance/{f}")
        df["Date"] = date
        all_data.append(df)
    if all_data:
        full_df = pd.concat(all_data)
        summary = full_df.groupby("Name").agg(
            Total_Days=("Date", "nunique"),
            First_Seen=("Time", "min"),
            Last_Seen=("Time", "max")
        ).reset_index()
        summary.to_excel("report_summary.xlsx", index=False)
        print("Report generated: report_summary.xlsx")

if __name__ == "__main__":
    generate_report()