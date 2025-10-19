import pandas as pd

def generate_student_insights(students_df):
    try:
        print("Generating insights...")

        # Load results from CSV
        results_csv = 'generated_results/student_results.csv'
        insights_txt = 'generated_results/student_insights.txt'
        results_df = pd.read_csv(results_csv)

        # Merge with provided students DataFrame
        merged_df = pd.merge(students_df, results_df, on='StudentID')

        # Top 3 students by percentage
        top_students = merged_df.sort_values(by='Percentage', ascending=False).head(3)

        # Average marks per course
        avg_by_course = merged_df.groupby('Course')[['Maths', 'Python', 'ML', 'TotalMarks', 'Percentage']].mean()

        # Save insights to text file
        with open(insights_txt, 'w') as f:
            f.write("Top 3 Students by Percentage:\n")
            f.write(top_students[['StudentID', 'Name', 'Course', 'Percentage']].to_string(index=False))
            f.write("\n\nAverage Marks per Course:\n")
            f.write(avg_by_course.to_string())

        print(f"Insights saved to {insights_txt}")
        return {
            "message": "Insights generated successfully",
        }

    except Exception as e:
        print(f"Error generating insights: {e}")
        return {"error": str(e)}
