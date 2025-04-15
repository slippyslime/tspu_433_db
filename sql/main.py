import sqlite3
import csv


def get_connection():
    """Устанавливает подключение к локальной базе данных."""
    return sqlite3.connect('students.db')


def setup_database():
    """Создает таблицы: факультеты, группы, студенты."""
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS faculties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                course INTEGER NOT NULL,
                specialty TEXT NOT NULL,
                phone TEXT NOT NULL,
                gender TEXT NOT NULL,
                faculty_id INTEGER,
                group_id INTEGER,
                FOREIGN KEY (faculty_id) REFERENCES faculties(id),
                FOREIGN KEY (group_id) REFERENCES groups(id)
            );
        """)
        print("✅ Таблицы успешно созданы.")


def import_students_from_csv(csv_path='БД - Студент.csv'):
    """Импортирует данные студентов из CSV файла."""
    with get_connection() as conn:
        cur = conn.cursor()

        with open(csv_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row = {k.strip().lower(): v.strip() for k, v in row.items()}

                faculty = row['факультет']
                group = row['группа']

                # Добавление факультета
                cur.execute("SELECT id FROM faculties WHERE name = ?", (faculty,))
                faculty_data = cur.fetchone()
                faculty_id = faculty_data[0] if faculty_data else cur.execute(
                    "INSERT INTO faculties (name) VALUES (?)", (faculty,)
                ).lastrowid

                # Добавление группы
                cur.execute("SELECT id FROM groups WHERE name = ?", (group,))
                group_data = cur.fetchone()
                group_id = group_data[0] if group_data else cur.execute(
                    "INSERT INTO groups (name) VALUES (?)", (group,)
                ).lastrowid

                # Добавление студента
                cur.execute("""
                    INSERT INTO students (
                        full_name, birth_date, course, specialty, phone, gender, faculty_id, group_id
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    row['фио'],
                    row['дата рождения'],
                    int(row['курс']),
                    row['специальность'],
                    row['номер тел.'].replace(' ', ''),
                    row['пол'],
                    faculty_id,
                    group_id
                ))

        print(f"📥 Импорт завершен из файла: {csv_path}")


if __name__ == '__main__':
    setup_database()
    import_students_from_csv('students.csv')
