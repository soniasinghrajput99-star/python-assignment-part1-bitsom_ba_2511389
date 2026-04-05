class Student:
    def __init__(self, name: str, roll: str, marks_str: str):
        self.name = self.format_name(name)
        self.roll = int(roll.strip())
        self.marks = self.parse_marks(marks_str)

        self.OK = "\u2713"
        self.FAIL = "\u2717"

    def format_name(self, raw_name: str) -> str:
        cleaned = " ".join(raw_name.strip().split())
        return " ".join(part.capitalize() for part in cleaned.split())

    def parse_marks(self, marks_str: str) -> list:
        return [int(x.strip()) for x in marks_str.split(",")]

    def check_name_validity(self) -> bool:
        return all(word.isalpha() for word in self.name.split())

    def show_validation(self):
        symbol = self.OK if self.check_name_validity() else self.FAIL
        status = "Valid name" if self.check_name_validity() else "Invalid name"
        print(f"{symbol} {status}")

    def display(self):
        print("=" * 32)
        print(f"Student : {self.name}")
        print(f"Roll No : {self.roll}")
        print(f"Marks   : {self.marks}")
        print("=" * 32)


class SubjectRecord:
    def __init__(self, subject: str, marks: int):
        self.subject = subject
        self.marks = marks

    def grade(self) -> str:
        m = self.marks
        if m >= 90:
            return "A+"
        elif m >= 80:
            return "A"
        elif m >= 70:
            return "B"
        elif m >= 60:
            return "C"
        return "F"


class ClassRecord:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def average(self) -> float:
        return round(sum(self.marks) / len(self.marks), 2)

    def result(self) -> str:
        return "Pass" if self.average() >= 60 else "Fail"


def task1():
    print("\nTASK 1 - DATA CLEANING")
    print("-" * 50)

    data = [
        {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
        {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
        {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
        {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
        {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
    ]

    student_list = []

    for entry in data:
        s = Student(entry["name"], entry["roll"], entry["marks_str"])
        student_list.append(s)

        print(f"\n{s.name}")
        s.show_validation()
        s.display()

    for s in student_list:
        if s.roll == 103:
            print("\nStudent with Roll No 103")
            print(s.name.upper())
            print(s.name.lower())


def task2():
    print("\nTASK 2 - MARKS ANALYSIS")
    print("-" * 50)

    name = "Ayesha Sharma"
    subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
    marks = [88, 72, 95, 60, 78]

    records = [SubjectRecord(sub, m) for sub, m in zip(subjects, marks)]

    print(f"Student Name: {name}\n")

    for r in records:
        print(f"{r.subject:<10} -> {r.marks:<3} -> {r.grade()}")

    total = sum(r.marks for r in records)
    avg = round(total / len(records), 2)

    highest = max(records, key=lambda x: x.marks)
    lowest = min(records, key=lambda x: x.marks)

    print("\nSummary")
    print(f"Total Marks            : {total}")
    print(f"Average Marks          : {avg}")
    print(f"Highest Scoring Subject: {highest.subject} ({highest.marks})")
    print(f"Lowest Scoring Subject : {lowest.subject} ({lowest.marks})")

    added = 0

    print("\nEnter new subjects and marks")
    print("Type 'done' to stop")

    while True:
        sub = input("\nEnter subject name: ").strip()
        if sub.lower() == "done":
            break

        try:
            m = int(input("Enter marks (0-100): ").strip())
            if 0 <= m <= 100:
                records.append(SubjectRecord(sub, m))
                added += 1
            else:
                print("Marks must be 0-100")
        except ValueError:
            print("Invalid input")

    new_avg = round(sum(r.marks for r in records) / len(records), 2)

    print("\nUpdated Result")
    print(f"New subjects added: {added}")
    print(f"Updated Average  : {new_avg}")


def task3():
    print("\nTASK 3 - CLASS SUMMARY")
    print("-" * 50)

    data = [
        ("Ayesha Sharma", [88, 72, 95, 60, 78]),
        ("Rohit Verma", [55, 68, 49, 72, 61]),
        ("Priya Nair", [91, 85, 88, 94, 79]),
        ("Karan Mehta", [40, 55, 38, 62, 50]),
        ("Sneha Pillai", [75, 80, 70, 68, 85]),
    ]

    records = [ClassRecord(n, m) for n, m in data]

    print(f"{'Name':<18} | {'Average':<7} | Status")
    print("-" * 40)

    passed = failed = 0
    total_avg = 0
    topper = records[0]

    for r in records:
        avg = r.average()
        status = r.result()

        passed += status == "Pass"
        failed += status == "Fail"

        if avg > topper.average():
            topper = r

        total_avg += avg

        print(f"{r.name:<18} | {avg:<7.2f} | {status}")

    class_avg = round(total_avg / len(records), 2)

    print("\nClass Summary")
    print(f"Passed Students : {passed}")
    print(f"Failed Students : {failed}")
    print(f"Class Topper    : {topper.name} ({topper.average()})")
    print(f"Class Average   : {class_avg}")


def task4():
    print("\nTASK 4 - STRING UTILITY")
    print("-" * 50)

    text = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

    clean = text.strip()
    print("1. Stripped Essay:")
    print(clean)

    print("\n2. Title Case:")
    print(clean.title())

    print("\n3. Count of 'python':")
    print(clean.count("python"))

    print("\n4. Replaced Essay:")
    print(clean.replace("python", "Python 🐍"))

    sentences = clean.split(". ")
    print("\n5. Sentences List:")
    print(sentences)

    print("\n6. Numbered Sentences:")
    for i, s in enumerate(sentences, 1):
        if not s.endswith("."):
            s += "."
        print(f"{i}. {s}")


def main():
    task1()
    task2()
    task3()
    task4()


if __name__ == "__main__":
    main()
