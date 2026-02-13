def get_grade_input(prompt, min_val=0.0, max_val=100.0):
    """
    Prompts the user for a numeric grade input.
    Validates that the value is within the acceptable range (0 to 100).
    Keeps asking until a valid number is provided.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")


def get_int_input(prompt, min_val=1, max_val=20):
    """
    Prompts the user for a whole number input (e.g., number of quizzes).
    Validates that the value is within an acceptable integer range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a whole number between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


# ---- COMPUTATION FUNCTIONS ----

def compute_attendance_grade(attendance_score):
    """
    Computes the weighted attendance grade.
    Formula: Attendance Score × 10%
    """
    return attendance_score * 0.10


def compute_assignment_grade(assignment_score):
    """
    Computes the weighted assignment grade.
    Formula: Assignment Score × 10%
    """
    return assignment_score * 0.10


def compute_quiz_grade(num_quizzes):
    """
    Accepts individual quiz scores from the user,
    computes the average, then applies the 50% weight.
    Formula: (Sum of Quizzes / Number of Quizzes) × 50%
    Returns both the quiz average and the weighted quiz grade.
    """
    total_score = 0.0

    # Collect each quiz score from the user
    for i in range(1, num_quizzes + 1):
        score = get_grade_input(f"    Enter Quiz {i} score : ")
        total_score += score

    quiz_average = total_score / num_quizzes
    weighted_quiz = quiz_average * 0.50
    return quiz_average, weighted_quiz


def compute_project_grade(project_score):
    """
    Computes the weighted project grade.
    Formula: Project Score × 30%
    """
    return project_score * 0.30


def compute_class_standing(attendance_grade, assignment_grade, quiz_grade, project_grade):
    """
    Computes the overall Class Standing Grade (70% of total).
    Formula: (Attendance + Assignment + Quiz + Project Grades) × 70%
    """
    raw_total = attendance_grade + assignment_grade + quiz_grade + project_grade
    return raw_total * 0.70


def compute_prelim_exam_component(prelim_exam_score):
    """
    Computes the Prelim Exam component of the final grade.
    Formula: Prelim Exam Score × 30%
    """
    return prelim_exam_score * 0.30


def compute_final_prelim_grade(class_standing_grade, prelim_exam_component):
    """
    Computes the Final Prelim Grade.
    Formula: Class Standing Grade + Prelim Exam Component
    """
    return class_standing_grade + prelim_exam_component


# ---- DISPLAY FUNCTION ----

def display_results(student_name, attendance, assignment, num_quizzes,
                    quiz_avg, attendance_grade, assignment_grade,
                    quiz_grade, project_grade, class_standing,
                    prelim_exam, prelim_component, final_grade):
    """
    Displays a formatted summary of all computed grades for the student.
    """
    separator = "=" * 45
    thin_line = "-" * 45

    print(f"\n{separator}")
    print(f"  GRADE SUMMARY FOR: {student_name}")
    print(separator)

    # --- Class Standing Breakdown ---
    print("  CLASS STANDING COMPONENTS (70%)")
    print(thin_line)
    print(f"  Attendance Score       : {attendance:.2f}")
    print(f"  Attendance Grade (10%) : {attendance_grade:.2f}")
    print()
    print(f"  Assignment Score       : {assignment:.2f}")
    print(f"  Assignment Grade (10%) : {assignment_grade:.2f}")
    print()
    print(f"  Number of Quizzes      : {num_quizzes}")
    print(f"  Quiz Average           : {quiz_avg:.2f}")
    print(f"  Quiz Grade (50%)       : {quiz_grade:.2f}")
    print()
    print(f"  Project Grade (30%)    : {project_grade:.2f}")
    print(thin_line)
    print(f"  Class Standing (70%)   : {class_standing:.2f}")

    # --- Major Exam Component ---
    print()
    print("  MAJOR EXAM COMPONENT (30%)")
    print(thin_line)
    print(f"  Prelim Exam Score      : {prelim_exam:.2f}")
    print(f"  Prelim Component (30%) : {prelim_component:.2f}")

    # --- Final Grade ---
    print()
    print(separator)
    print(f"  FINAL PRELIM GRADE     : {final_grade:.2f}")
    print(separator)

    # Provide a simple remark based on the final grade
    if final_grade >= 90:
        remark = "Excellent!"
    elif final_grade >= 80:
        remark = "Very Good"
    elif final_grade >= 75:
        remark = "Passed"
    else:
        remark = "Below Passing - Needs Improvement"

    print(f"  Remark: {remark}")
    print(separator)


# ---- MAIN PROGRAM ----

def main():
    """
    Main function that drives the Prelim Grade Calculator.
    Allows the user to compute grades for one or multiple students.
    """
    print("=" * 45)
    print("       PRELIM GRADE CALCULATOR")
    print("=" * 45)

    another = True  # Controls whether to compute for another student

    while another:
        print()
        # Get student name
        student_name = input("  Enter Student Name: ").strip().upper()
        if not student_name:
            student_name = "STUDENT"

        print()
        print("  --- Enter Grade Components ---")

        # --- Collect all inputs ---
        attendance_score = get_grade_input("  Attendance Score (0-100): ")
        assignment_score = get_grade_input("  Assignment Score (0-100): ")

        num_quizzes = get_int_input("  Number of Quizzes (1-20): ")
        print("  Enter individual quiz scores:")
        quiz_avg, quiz_grade = compute_quiz_grade(num_quizzes)

        project_score = get_grade_input("  Project Score (0-100): ")
        prelim_exam_score = get_grade_input("  Prelim Exam Score (0-100): ")

        # --- Perform all computations ---
        attendance_grade  = compute_attendance_grade(attendance_score)
        assignment_grade  = compute_assignment_grade(assignment_score)
        project_grade     = compute_project_grade(project_score)
        class_standing    = compute_class_standing(
                                attendance_grade,
                                assignment_grade,
                                quiz_grade,
                                project_grade
                            )
        prelim_component  = compute_prelim_exam_component(prelim_exam_score)
        final_grade       = compute_final_prelim_grade(class_standing, prelim_component)

        # --- Show all results ---
        display_results(
            student_name,
            attendance_score, assignment_score,
            num_quizzes, quiz_avg,
            attendance_grade, assignment_grade,
            quiz_grade, project_grade,
            class_standing, prelim_exam_score,
            prelim_component, final_grade
        )

        # Ask if user wants to compute for another student
        print()
        again = input("  Compute for another student? (yes/no): ").strip().lower()
        another = again in ("yes", "y")

    # Closing message
    print()
    print("=" * 45)
    print("  Thank you for using the Grade Calculator!")
    print("=" * 45)
    print()


# Entry point
if __name__ == "__main__":
    main()