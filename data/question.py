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
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# DATE_PART ile sadece kayıtların yıl bilgisini al
def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#  Her öğrencinin yaşına göre kategori belirle. (CASE) Sorgu first_name, age ve öğrenci kategorisini dönmelidir.
#  öğrenci yaşı 23 ten küçükse(dahil) kategori 'Genç', 23 ile 25(dahil) arasındaysa 'Orta', diğer şartlarda 'Deneyimli'sonucu dönmelidir.
def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#En fazla öğrenciye sahip kursu bul (subquery ile)
def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Yaşı ortalama yaştan büyük olan öğrencileri getir
def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kursun en eski kayıt tarihini bul
def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kurs için öğrencilerin ortalama yaşlarını bulun. 
# Sorgu course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Subquery ile en genç öğrencinin adını getir
def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Kayıt olduğu kurs sayısı ortalamadan fazla olan öğrencileri bul.
# Sorgu sadece student_id bilgisini dönmelidir.
def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#Hiç kaydı olmayan kursları getir. Sorgu courses tablosunun tüm kolonlarını dönmelidir.
def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
