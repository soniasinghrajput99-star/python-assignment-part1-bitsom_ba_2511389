# Student Grade Tracker (Python)

This project is a basic command-line Student Grade Tracker developed using fundamental Python concepts. The main objective is to handle unstructured input data, clean and organize it, and then generate meaningful outputs such as grades, averages, and summaries.

All the code is contained in a single file:
`part1_grade_tracker.py`

---

## Project Overview

The program is organized into four sections. Each section highlights a different concept, but all of them are connected through the central idea of managing and processing student data.

---

## Task 1 - Data Cleaning and Formatting

The input data is deliberately unorganized—names include extra spaces and inconsistent capitalization, roll numbers are stored as strings, and marks are given as a single comma-separated string.

To address this, a `Student` class is used to clean and structure the data.

For each student:
- unnecessary spaces are removed  
- names are converted into Title Case  
- roll numbers are converted into integers  
- marks are transformed into a list of integers  

A validation check ensures that names contain only alphabetic characters. Based on the result, the program displays either a ✓ or ✗.

After processing, each student’s information is displayed in a simple profile format. Additionally, the student with roll number 103 is selected, and their name is shown in both uppercase and lowercase.

This section reflects real-world data preprocessing tasks.

---

## Task 2 - Subject-wise Marks Analysis

This section focuses on a single student and their subject performance.

Each subject and its marks are processed using loops, and grades are assigned based on predefined ranges.

A `SubjectRecord` class is used to store subject–mark pairs and compute grades.

The program then:
- calculates total marks  
- computes the average (rounded to two decimal places)  
- identifies the highest and lowest scoring subjects  

A `while` loop allows users to add new subjects dynamically, and it continues until "done" is entered.

Input validation ensures:
- non-numeric inputs are rejected  
- marks outside the range of 0–100 are ignored  

After adding new subjects, the updated average is calculated and displayed.

---

## Task 3 - Class Performance Summary

In this section, multiple students are processed together.

Each student is represented using a `ClassRecord` class, which calculates:
- average marks  
- pass/fail status (pass if average ≥ 60)  

The results are displayed in a table showing the student’s name, average, and status.

While iterating through the data, the program also tracks:
- the number of students who passed and failed  
- the class topper  
- the overall class average  

All operations are implemented using loops to keep the logic simple and easy to follow.

---

## Task 4 - String Processing

This section works with a paragraph of text.

The text is first cleaned using `.strip()`, followed by several string operations:

- converting the text to title case  
- counting occurrences of the word "python"  
- replacing "python" with "Python 🐍"  
- splitting the paragraph into sentences  
- printing each sentence with numbering  

It also ensures that every sentence ends with a period when displayed.

---

## How to Run

Run the following command in your terminal:

> python part1_grade_tracker.py

For Task 2, the program will prompt you to enter additional subjects and marks interactively.
