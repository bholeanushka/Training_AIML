import pandas as pd
from datetime import datetime

def run_etl(csv_path):
    print(f"ETL started for {csv_path}")
    df = pd.read_csv(csv_path)
    df['TotalMarks'] = df[['Maths', 'Python', 'ML']].sum(axis=1)
    df['Percentage'] = df['TotalMarks'] / 3
    df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

    # CSV - Generation Student_results
    df.to_csv('generated_results/student_results.csv', index=False)
    print("ETL completed. Results saved to student_results.csv")

    # timestamped file
    timestamp = datetime.now().strftime('%Y%m%d')
    filename = f'daily_etl/daily_report_{timestamp}.csv'
    df.to_csv(filename, index=False)
    print(f"ETL complete. Also saved as {filename}")