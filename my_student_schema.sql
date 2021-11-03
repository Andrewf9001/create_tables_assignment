CREATE TABLE IF NOT EXISTS People (
  person_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT,
  email TEXT NOT NULL,
  phone TEXT,
  password TEXT NOT NULL,
  address TEXT,
  city TEXT,
  state TEXT,
  postal_code TEXT,
  active INTEGER DEFAULT 1,
  UNIQUE (person_id, email)
);


CREATE TABLE IF NOT EXISTS Courses (
  course_id INTEGER PRIMARY KEY UNIQUE,
  name TEXT NOT NULL,
  description TEXT,
  active INTEGER DEFAULT 1
);


CREATE TABLE IF NOT EXISTS Cohort (
  cohort_id INTEGER PRIMARY KEY,
  instructor_id INTEGER,
  course_id INTEGER,
  start_date TEXT,
  end_date TEXT,
  active INTEGER DEFAULT 1,
  UNIQUE (cohort_id, instructor_id, course_id),
  FOREIGN KEY (instructor_id)
    REFERENCES People (person_id),
  FOREIGN KEY (course_id)
    REFERENCES Courses (course_id)
);


CREATE TABLE IF NOT EXISTS Student_Cohort_Registration (
  student_id INTEGER NOT NULL,
  cohort_id INTEGER NOT NULL,
  registration_date TEXT NOT NULL,
  completion_date TEXT,
  drop_date TEXT,
  active INTEGER DEFAULT 1,
  PRIMARY KEY(student_id, cohort_id),
  UNIQUE (student_id, cohort_id),
  FOREIGN KEY (student_id)
    REFERENCES People (person_id),
  FOREIGN KEY (cohort_id)
    REFERENCES Cohort (cohort_id)
);

-- INSERT INTO Cohort (instructor_id, course_id, start_date, end_date)
-- VALUES (5, 1, "2021-11-20", "2022-06-05")

-- INSERT INTO Student_Cohort_Registration (student_id, cohort_id, registration_date)
-- VALUES (8, 1, "2021-11-14")