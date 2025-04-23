import psycopg2

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="testdb",
    user="postgres",
    password="postgres")
    return conn

# DATE_TRUNC ile ay bazlı kayıt sayılarını listele
def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT DATE_TRUNC(\'month\', enrollment_date) AS month, COUNT(*) FROM enrollments GROUP BY month ORDER BY month;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# DATE_PART ile sadece kayıtların yıl bilgisini al
def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT DATE_PART(\'year\', enrollment_date) AS year FROM enrollments;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#  Her öğrencinin yaşına göre kategori belirle. (CASE) Sorgu first_name, age ve öğrenci kategorisini dönmelidir.
#  öğrenci yaşı 23 ten küçükse(dahil) kategori 'Genç', 23 ile 25(dahil) arasındaysa 'Orta', diğer şartlarda 'Deneyimli'sonucu dönmelidir.
def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT first_name, age,
            CASE
                WHEN age < 23 THEN 'Genç'
                WHEN age BETWEEN 23 AND 25 THEN 'Orta'
                ELSE 'Deneyimli'
        END AS age_group 
        FROM students;""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#En fazla öğrenciye sahip kursu bul (subquery ile)
def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT course_id 
        FROM enrollments 
        GROUP BY course_id 
        ORDER BY COUNT(*) DESC 
        LIMIT 1;
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Yaşı ortalama yaştan büyük olan öğrencileri getir
def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
       SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kursun en eski kayıt tarihini bul
def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
      SELECT course_id, MIN(enrollment_date) AS first_enrollment 
      FROM enrollments 
      GROUP BY course_id;
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kurs için öğrencilerin ortalama yaşlarını bulun. 
# Sorgu course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
     SELECT c.course_name, AVG(s.age) AS avg_age
     FROM courses c
     JOIN enrollments e ON c.course_id = e.course_id
     JOIN students s ON s.student_id = e.student_id
     GROUP BY c.course_name;
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Subquery ile en genç öğrencinin adını getir
def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
     SELECT first_name FROM students WHERE age = (SELECT MIN(age) FROM students);
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Kayıt olduğu kurs sayısı ortalamadan fazla olan öğrencileri bul.
# Sorgu sadece stuudent_id bilgisini dönmelidir.
def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT student_id
    FROM enrollments
    GROUP BY student_id
    HAVING COUNT(course_id) > (
    SELECT AVG(course_count) 
    FROM (
        SELECT COUNT(course_id) AS course_count 
        FROM enrollments 
        GROUP BY student_id
    ) AS sub
    );
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#Hiç kaydı olmayan kursları getir. Sorgu courses tablosunun tüm kolonlarını dönmelidir.
def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM courses WHERE course_id NOT IN (SELECT DISTINCT course_id FROM enrollments);
    """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data