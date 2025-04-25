# Data Science SQL Project 

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-project-2.

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

### Hedeflerimiz:

### Görev 1

* question_1_query fonksiyonun içerisinde `DATE_TRUNC ile ay bazlı kayıt sayılarını listele` işlemini gerçekleştirecek sql querysini yazınız.
* question_2_query fonksiyonun içerisinde ` DATE_PART ile sadece kayıtların yıl bilgisini al` işlemini gerçekleştirecek sql querysini yazınız. query tüm kolonları dönmelidir.
* question_3_query fonksiyonun içerisinde `Her öğrencinin yaşına göre kategori belirle. (CASE) Sorgu first_name, age ve öğrenci kategorisini dönmelidir. öğrenci yaşı 23 ten küçükse(dahil) kategori 'Genç', 23 ile 25(dahil) arasındaysa 'Orta', diğer şartlarda 'Deneyimli'sonucu dönmelidir.` işlemini gerçekleştirecek sql querysini yazınız.
* question_4_query fonksiyonun içerisinde `En fazla öğrenciye sahip kursu bul (subquery ile)` işlemini gerçekleştirecek sql querysini yazınız.
query sadece course_id bilgisini dönmelidir.
* question_5_query fonksiyonun içerisinde `Yaşı ortalama yaştan büyük olan öğrencileri getir.` işlemini gerçekleştirecek sql querysini yazınız.
query tüm kolonları dönmelidir.
* question_6_query fonksiyonun içerisinde `Her kursun en eski kayıt tarihini bul.` işlemini gerçekleştirecek sql querysini yazınız.
query course_id ve en eski tarihi first_enrollment ismiyle dönmelidir.
* question_7_query fonksiyonun içerisinde `Her kurs için öğrencilerin ortalama yaşlarını bulun.` işlemini gerçekleştirecek sql querysini yazınız.
query course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
* question_8_query fonksiyonun içerisinde `Subquery ile en genç öğrencinin adını getir.` işlemini gerçekleştirecek sql querysini yazınız.
* question_9_query fonksiyonun içerisinde `Kayıt olduğu kurs sayısı ortalamadan fazla olan öğrencileri bul.` işlemini gerçekleştirecek sql querysini yazınız. Sorgu sadece student_id bilgisini dönmelidir.
* question_10_query fonksiyonun içerisinde `Hiç kaydı olmayan kursları getir.` işlemini gerçekleştirecek sql querysini yazınız.
query courses tablosunun tüm kolonlarını dönmelidir.
