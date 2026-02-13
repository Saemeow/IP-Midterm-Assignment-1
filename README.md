# Prelim Grade Calculator

A Python command line program that computes a student's Final Prelim Grade based on Class Standing and a Major Exam component.

---

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python student_prelim_midterm.py
```

---

## Grading System

### Class Standing (70%)

| Component       | Weight |
|----------------|--------|
| Attendance      | 10%    |
| Assignment      | 10%    |
| Quiz Average    | 50%    |
| Project         | 30%    |

**Class Standing Grade** = (Attendance + Assignment + Quiz + Project Grades) × 70%

### Major Exam (30%)

**Prelim Exam Component** = Prelim Exam Score × 30%

### Final Prelim Grade

**Final Prelim Grade** = Class Standing Grade + Prelim Exam Component

---

## Features

- Accepts grades for one or multiple students in a single session
- Collects individual quiz scores and computes the average automatically
- Validates all inputs — rejects non-numeric values and scores outside 0–100
- Displays a fully formatted grade summary with all computed components
- Shows a remark based on the final grade (Excellent, Very Good, Passed, or Below Passing)

---

## Sample Output

```
=============================================
       PRELIM GRADE CALCULATOR
=============================================

  Enter Student Name: Juan Dela Cruz
  --- Enter Grade Components ---
  Attendance Score (0-100): 85
  Assignment Score (0-100): 90
  Number of Quizzes (1-20): 3
  Enter individual quiz scores:
    Enter Quiz 1 score : 78
    Enter Quiz 2 score : 82
    Enter Quiz 3 score : 88
  Project Score (0-100): 75
  Prelim Exam Score (0-100): 80

=============================================
  GRADE SUMMARY FOR: JUAN DELA CRUZ
=============================================
  CLASS STANDING COMPONENTS (70%)
---------------------------------------------
  Attendance Score       : 85.00
  Attendance Grade (10%) : 8.50

  Assignment Score       : 90.00
  Assignment Grade (10%) : 9.00

  Number of Quizzes      : 3
  Quiz Average           : 82.67
  Quiz Grade (50%)       : 41.33

  Project Grade (30%)    : 22.50
---------------------------------------------
  Class Standing (70%)   : 56.93

  MAJOR EXAM COMPONENT (30%)
---------------------------------------------
  Prelim Exam Score      : 80.00
  Prelim Component (30%) : 24.00

=============================================
  FINAL PRELIM GRADE     : 80.93
=============================================
  Remark: Very Good
=============================================
```

---

## Error Handling

The program validates every input before proceeding:

- **Non-numeric input** — prompts the user to enter a valid number
- **Out-of-range input** — rejects any score below 0 or above 100
- **Invalid quiz count** — only accepts whole numbers between 1 and 20
- **Empty student name** — defaults to "STUDENT" if left blank

---

## Requirements

- Python 3.x
- No external libraries required