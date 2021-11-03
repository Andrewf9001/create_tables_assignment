import sqlite3
from datetime import datetime

connection = sqlite3.connect('my_students.db')
cursor = connection.cursor()

def continue_func():
  print()
  print("Press <enter> to continue")
  print("-"*25)
  input()


def view_people(cursor):
  rows = cursor.execute("SELECT person_id, first_name, last_name, email, phone, address, city, state, postal_code, active FROM People WHERE active = 1")

  print("\n*** All Students and Instructors ***")

  print(f'\n{"ID":^4} {"First":<12} {"Last":<15} {"Email":<25} {"Phone":<15} {"Address":<20} {"City":<15} {"State":<11} {"Postal":<10} {"Active":<10}')
  print('----------------------------------------------------------------------------------------------------------------------------------------------')

  for row in rows:
    print(f"{row[0]:>2}.  {row[1]:<12} {row[2]:<15} {row[3]:<25} {row[4]:<15} {row[5]:<20} {row[6]:<15}  {row[7]:<11} {row[8]:<10} {row[9]:<10}")


def view_inactive_people(cursor):
  rows = cursor.execute("SELECT person_id, first_name, last_name, email, phone, address, city, state, postal_code, active FROM People WHERE active = 0")

  print("\n*** All Inactive Students and Instructors ***")

  print(f'\n{"ID":^4} {"First":<12} {"Last":<15} {"Email":<25} {"Phone":<15} {"Address":<20} {"City":<15} {"State":<11} {"Postal":<10} {"Active":<10}')
  print('----------------------------------------------------------------------------------------------------------------------------------------------')

  for row in rows:
    print(f"{row[0]:>2}.  {row[1]:<12} {row[2]:<15} {row[3]:<25} {row[4]:<15} {row[5]:<20} {row[6]:<15}  {row[7]:<11} {row[8]:<10} {row[9]:<10}")


def view_courses(cursor):
  rows = cursor.execute("SELECT course_id, name, description, active FROM Courses WHERE active = 1")

  print("\n*** All Course ***")

  print(f'\n{"ID":^4} {"Course":<15} {"Active":^10} {"Description":^10}')
  print('----------------------------------------')

  for row in rows:
    print(f"{row[0]:>2}. {row[1]:<15} {row[3]:^10} {row[2]:<25}")


def view_inactive_courses(cursor):
  rows = cursor.execute("SELECT course_id, name, description, active FROM Courses WHERE active = 0")

  print("\n*** All Inactive Course ***")

  print(f'\n{"ID":^4} {"Course":<15} {"Active":^10} {"Description":^10}')
  print('----------------------------------------')

  for row in rows:
    print(f"{row[0]:>2}. {row[1]:<15} {row[3]:^10} {row[2]:<25}")


def view_cohort(cursor):
  rows = cursor.execute("SELECT c.cohort_id, c.start_date, c.end_date, p.first_name FROM Cohort c JOIN People p ON c.instructor_id = p.person_id WHERE c.active = 1")

  print("\n*** Cohorts ***")
  print(f'\n{"ID"} {"Instructor":^15} {"Start Date":^15} {"End Date":^15}')
  print('------------------------------------------------')
  for row in rows:
    print(f"{row[0]:<4} {row[3]:<10} {row[1]:^20} {row[2]:^13}")


def view_inactive_cohort(cursor):
  rows = cursor.execute("SELECT c.cohort_id, c.start_date, c.end_date, p.first_name FROM Cohort c JOIN People p ON c.instructor_id = p.person_id WHERE c.active = 0")

  print("\n*** Inactive Cohorts ***")
  print(f'\n{"ID"} {"Instructor":^15} {"Start Date":^15} {"End Date":^15}')
  print('------------------------------------------------')
  for row in rows:
    print(f"{row[0]:<4} {row[3]:<10} {row[1]:^20} {row[2]:^13}")


def view_student_cohort_registration(cursor):
  rows = cursor.execute("SELECT scr.student_id, scr.cohort_id, scr.registration_date, p.first_name, p.last_name, c.name, c.description FROM Student_Cohort_Registration scr JOIN People p ON scr.student_id = p.person_id JOIN Courses c ON scr.cohort_id = c.course_id WHERE scr.active = 1")

  print("\n*** Student and Cohorts ***\n")
  print("*** Student ID as 'S ID', Cohort ID as 'C ID' ***")
  print(f'\n{"S ID"} {"C ID":^10}  {"Name":<25} {"Registration":^21} {"Course":<10} {"Course Description":^25}')
  print('---------------------------------------------------------------------------------------------------')
  for row in rows:
    full_name = row[3] + " " + row[4]
    print(f"{row[0]:^3} {row[1]:^11} {full_name:<25} {row[2]:^21} {row[5]:<15} {row[6]:<15}")


# view_student_cohort_registration(cursor)


def view_inactive_registration(cursor):
  rows = cursor.execute("SELECT scr.student_id, scr.cohort_id, scr.registration_date, p.first_name, p.last_name, c.name, c.description FROM Student_Cohort_Registration scr JOIN People p ON scr.student_id = p.person_id JOIN Courses c ON scr.cohort_id = c.course_id WHERE scr.active = 0")

  print("\n*** Inactive Student and Cohorts ***\n")
  print("*** Student ID as 'S ID', Cohort ID as 'C ID' ***")
  print(f'\n{"S ID"} {"C ID":^10}  {"First Name":^14} {"Last Name":^14} {"Registration":^20} {"Course":^15} {"Course Description":^15}')
  print('------------------------------------------------')
  for row in rows:
    print(f"{row[0]:^3} {row[1]:^11} {row[3]:^14} {row[4]:^14} {row[2]:^21} {row[5]:^15} {row[6]:^15}")


def new_person(cursor):
  first_name = input("Enter the First Name: ")
  last_name = input("Enter the Last Name: ")
  email = input("Enter the Email Address: ")
  phone = input("Enter the Phone Number: ")
  password = input("Enter a new Password: ")
  address = input("Enter the address: ")
  city = input("Enter the City: ")
  state = input("Enter the State: ")
  postal_code = input("Enter the Postal Code: ")


  query = "INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code) VALUES (?, ?, ?, ?, ?, ? ,?, ?, ?)"
  values = (first_name, last_name, email, phone, password, address, city, state, postal_code)

  cursor.execute(query, values)
  connection.commit()
  print(f"Successfully added: {first_name} {last_name}")


def new_course(cursor):
  name = input("Enter Course Name: ")
  description = input("Enter Course Description: ")


  query = "INSERT INTO Courses (name, description) VALUES (?, ?)"
  values = (name, description)

  cursor.execute(query, values)
  connection.commit()
  print(f"{name.title()} has been added as a new course")


def new_cohort(cursor):
  query_count = "SELECT COUNT(*) FROM Cohort WHERE active = 1"

  cursor.execute(query_count)
  count = cursor.fetchall()

  if count[0][0] == 0:
    print("There are no courses yet")
  else:
    print("\nWhich course is the cohort for?")
    print("\n[1] Hakuda\n[2] Zanjutsu\n[3] Hoho\n[4] Kido\n[5] Soul Burial\n[6] Zanpakuto")
    course_input = input()
    print("\nWho is the instructor for the cohort?")
    print("\n[1] Kisuke Urahara\n[2] Yachiru Unohana\n[3] Kaien Shiba\n[4] Shunsui Kyoraku\n[5] Yoruichi Shihoin")
    person_input = input()
    print("\nPlease enter the start and end dates for the cohort")
    start = input("Start Date: ")
    end = input("End Date: ")

    query = "INSERT INTO Cohort (instructor_id, course_id, start_date, end_date) VALUES (?, ?, ?, ?)"
    values = (person_input, course_input, start, end)

    cursor.execute(query, values)
    connection.commit()
    print("New cohort added!")


def student_assign_cohort(cursor):
  view_people(cursor)
  view_courses(cursor)
  student_input = input("Please enter the student ID: ")
  course_input = input("Please enter the Course ID: ")
  registration_input = input("Please enter the date: ")

  query = "INSERT INTO Student_Cohort_Registration (student_id, cohort_id, registration_date) VALUES (?, ?, ?)"
  values = (student_input, course_input, registration_input)

  cursor.execute(query, values)
  connection.commit()
  print("New student assigned to cohort")


def deactivate(cursor):
  print("\nPlease choose between Person, Course, Cohort, or Registration for deactivation")
  print("\n[1] Person\n[2] Course\n[3] Cohort\n[4] Registration")
  user_input = input()

  if user_input == '1':
    view_people(cursor)
    print("\nPlease select ID of the Person to be deactivated")
    person_input = input()

    cursor.execute("UPDATE People SET active = 0 WHERE person_id = ?", (person_input, ))

    connection.commit()
    print("Student or Instructor successfully deactivated")

  elif user_input == '2':
    view_courses(cursor)
    print("\nPlease select ID of the Course to be deactivated")
    course_input = input()

    cursor.execute("UPDATE Courses SET active = 0 WHERE course_id = ?", (course_input, ))

    connection.commit()
    print("\nCourse successfully deactivated")

  elif user_input == '3':
    view_cohort(cursor)
    print("\nPlease select ID of Cohort to be deactivated")
    cohort_input = input()

    cursor.execute("UPDATE Cohort SET active = 0 WHERE cohort_id = ?", (cohort_input, ))

    connection.commit()
    print("\nCohort successfully deactivated")

  elif user_input == '4':
    view_student_cohort_registration(cursor)
    print("\nPlease select the ID of the Student to be removed")
    student_input = input()
    print("\nPlease select the ID of the cohort to be removed")
    cohort_input = input()
    date = datetime.now().date()

    cursor.execute("UPDATE Student_Cohort_Registration SET active = 0, drop_date = ? WHERE student_id = ? AND cohort_id = ?", (date, student_input, cohort_input))

    connection.commit()
    print("\nStudent Registration successfully deactivated")

# deactivate(cursor)

def reactivate(cursor):
  print("\nPlease choose between Person, Course, Cohort, or Registration for deactivation")
  print("\n[1] Person\n[2] Course\n[3] Cohort\n[4] Registration")
  user_input = input()

  if user_input == '1':
    view_inactive_people(cursor)
    print("\nPlease select ID of the Person to be reactivated")
    person_input = input()

    cursor.execute("UPDATE People SET active = 1 WHERE person_id = ?", (person_input, ))

    connection.commit()
    print("\nStudent or Instructor successfully reactivated")

  elif user_input == '2':
    view_inactive_courses(cursor)
    print("\nPlease select ID of the Course to be reactivated")
    course_input = input()

    cursor.execute("UPDATE Courses SET active = 1 WHERE course_id = ?", (course_input, ))

    connection.commit()
    print("\nCourse successfully reactivated")

  elif user_input == '3':
    view_inactive_cohort(cursor)
    print("\nPlease select ID of the Cohort to be reactivated")
    cohort_input = input()

    cursor.execute("UPDATE Cohort SET active = 1 WHERE cohort_id = ?", (cohort_input, ))

    connection.commit()
    print("\nCohort successfully reactivated")

  elif user_input == '4':
    view_inactive_registration(cursor)
    print("\nPlease select the Student ID to be reactivated")
    student_reg_input = input()
    print("\nPlease select the Cohort ID")
    cohort_reg_input = input()

    cursor.execute("UPDATE Student_Cohort_Registration SET active = 1 WHERE student_id = ? AND cohort_id = ?", (student_reg_input, cohort_reg_input))

    connection.commit()
    print("\nStudent Registration successfully reactivated")

# reactivate(cursor)

def completed_course(cursor):
  view_student_cohort_registration(cursor)
  print("\nPlease select the ID of the Student that has completed the course")
  student_input = input()
  print("\nPlease select the ID of the Cohort the student is in that has completed the course")
  cohort_input = input()
  date = datetime.now().date()

  cursor.execute("UPDATE Student_Cohort_Registration SET completion_date = ? WHERE student_id = ? AND cohort_id = ?", (date, student_input, cohort_input))

  connection.commit()

  print("Congratulations on completing the course!")


def main():
  print("Welcome to the Bleach Verse for Shinigami Academy")

  while True:
    print("\nPlease Select an option")
    print("\n[1] View Tables\n[2] Add New Entry\n[3] Deactivate Options\n[4] Reactivate Options\n[5] Completed Course\n[Q] Quit")
    initial_input = input()

    if initial_input.lower() == 'q':
      quit()

    elif initial_input == '1':
      print("\nWhich would you like to view?")
      print("\n[1] Active\n[2] Inactive")
      act_inact_input = input()

      if act_inact_input == '1':
        print("\nWhat would you like to view?")
        print("\n[1] Instructors and Students\n[2] Courses\n[3] Cohorts\n[4] Student Registration")
        view_input = input()

        if view_input == '1':
          view_people(cursor)
          continue_func()
        elif view_input == '2':
          view_courses(cursor)
          continue_func()
        elif view_input == '3':
          view_cohort(cursor)
          continue_func()
        elif view_input == '4':
          view_student_cohort_registration(cursor)
          continue_func()

      elif act_inact_input == '2':
        print("\nWhat would you like to view?")
        print("\n[1] Instructors and Students\n[2] Courses\n[3] Cohorts\n[4] Student Registration")
        view_input = input()

        if view_input == '1':
          view_inactive_people(cursor)
          continue_func()
        elif view_input == '2':
          view_inactive_courses(cursor)
          continue_func()
        elif view_input == '3':
          view_inactive_cohort(cursor)
          continue_func()
        elif view_input == '4':
          view_inactive_registration(cursor)
          continue_func()

    elif initial_input == '2':
      print("\nWhich field would you like to add to?")
      print("\n[1] Instructors and Students\n[2] Courses\n[3] Cohorts\n[4] Student Registration")
      add_input = input()

      if add_input == '1':
        new_person(cursor)
        continue_func()
      elif add_input == '2':
        new_course(cursor)
        continue_func()
      elif add_input == '3':
        new_cohort(cursor)
        continue_func()
      elif add_input == '4':
        student_assign_cohort(cursor)
        continue_func()
      
    elif initial_input == '3':
      deactivate(cursor)
      continue_func()

    elif initial_input == '4':
      reactivate(cursor)
      continue_func()

    elif initial_input == '5':
      completed_course(cursor)
      continue_func()
    else:
      print("Invalid Option, please try again")

main()