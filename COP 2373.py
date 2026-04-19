import csv
import numpy as np


def write_grades_to_csv():
    num_students = int(input("Enter the number of students (minimum 10): "))

    while num_students < 10:
        print("You must enter at least 10 students.")
        num_students = int(input("Enter the number of students (minimum 10): "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam1", "Exam2", "Exam3"])

        for i in range(num_students):
            print(f"\nEnter data for student {i + 1}")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            exam1 = int(input("Exam 1 score: "))
            exam2 = int(input("Exam 2 score: "))
            exam3 = int(input("Exam 3 score: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])


def read_grades_from_csv():
    print("\n--- Student Grades ---\n")

    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def analyze_grades():
    data = []

    with open("grades.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            data.append([int(row[2]), int(row[3]), int(row[4])])

    grades_array = np.array(data)

    print("\n--- First Few Rows of Dataset ---")
    print(grades_array[:5])  # preview first 5 rows

    print("\n--- Statistics for Each Exam ---")
    for i in range(3):
        exam_scores = grades_array[:, i]
        print(f"\nExam {i + 1}:")
        print(f"Mean: {np.mean(exam_scores):.2f}")
        print(f"Median: {np.median(exam_scores):.2f}")
        print(f"Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"Minimum: {np.min(exam_scores)}")
        print(f"Maximum: {np.max(exam_scores)}")

    # Overall statistics
    all_scores = grades_array.flatten()

    print("\n--- Overall Statistics (All Exams Combined) ---")
    print(f"Mean: {np.mean(all_scores):.2f}")
    print(f"Median: {np.median(all_scores):.2f}")
    print(f"Standard Deviation: {np.std(all_scores):.2f}")
    print(f"Minimum: {np.min(all_scores)}")
    print(f"Maximum: {np.max(all_scores)}")

    # Pass/Fail analysis
    print("\n--- Pass/Fail Counts Per Exam ---")
    total_pass = 0
    total_scores = all_scores.size

    for i in range(3):
        exam_scores = grades_array[:, i]
        passed = np.sum(exam_scores >= 60)
        failed = np.sum(exam_scores < 60)

        total_pass += passed

        print(f"Exam {i + 1}: Passed = {passed}, Failed = {failed}")

    pass_percentage = (total_pass / total_scores) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")


def main():
    write_grades_to_csv()
    read_grades_from_csv()
    analyze_grades()


if __name__ == "__main__":
    main()