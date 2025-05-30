import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn

# DATE_TRUNC ile ay bazlı kayıt sayılarını listele
def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT DATE_TRUNC('month', enrollment_date) AS enrollment_month, COUNT(*) AS enrollment_count FROM enrollments GROUP BY DATE_TRUNC('month', enrollment_date);")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# DATE_PART ile sadece kayıtların yıl bilgisini al
def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT *, DATE_PART('year', enrollment_date) AS enrollment_year FROM enrollments;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm öğrencilerin yaşlarının toplamını dönen bir sql sorgusu yaz.
def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT SUM(age) AS total_age FROM students;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm kurs sayısını bul
def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(course_id) AS courses_count FROM courses;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Yaşı ortalama yaştan büyük olan öğrencileri getir
def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT ROUND(AVG(age)::numeric, 2) AS avg_age FROM students;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kursun en eski kayıt tarihini bul
def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_id, MIN(e.enrollment_date) AS first_enrollment FROM courses AS c JOIN enrollments AS e ON e.course_id = c.course_id GROUP BY c.course_id ORDER BY c.course_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kurs için öğrencilerin ortalama yaşlarını bulun. 
# Sorgu course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, ROUND(AVG(s.age)::numeric, 2) AS avg_age FROM students AS s JOIN enrollments AS e ON s.student_id = e.student_id JOIN courses AS c ON c.course_id = e.course_id GROUP BY c.course_name ORDER BY avg_age;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# En genç öğrencinin yaşını getiren sorguyu yazınız.
def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT MIN(age) AS youngest_student_age FROM students;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Her derse kayıt olmuş öğrenci sayısını bulunuz.
def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(e.course_id) AS student_count FROM students AS s JOIN enrollments AS e ON s.student_id = e.student_id JOIN courses AS c ON c.course_id = e.course_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#Tüm kayıt olunmuş derslerin sadece isimlerini getirinz.
def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name FROM students AS s JOIN enrollments AS e ON e.student_id = s.student_id JOIN courses AS c ON c.course_id = e.course_id GROUP BY c.course_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
