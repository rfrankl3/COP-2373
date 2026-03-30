import csv


def write_grades_to_csv():
    num_students = int(input())

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for _ in range(num_students):
            first_name = input()
            last_name = input()
            exam1 = int(input())
            exam2 = int(input())
            exam3 = int(input())

            writer.writerow([first_name, last_name, exam1, exam2, exam3])


def read_grades_from_csv():
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))


def main():
    write_grades_to_csv()
    read_grades_from_csv()


if __name__ == "__main__":
    main()