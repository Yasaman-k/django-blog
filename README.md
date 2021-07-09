# django-blog
برای ساخت یک پروژه با جنگو ابتدا باید با کد زیر وارد محیط virtualenv میشویم

 source ~/.virtualenvs/djangodev/bin/activate

با دستور زیر پروژه را میسازیم 
django-admin startproject djangoproject

برای ایجاد یک اپ که اسمشو تست گذاشتیم کد زیر را میزنیم برای کارهای مختلف میتونیم اپ های مختلف بنویسیم
 python manage.py startapp testapp

میتونیم یک سرور ایجاد کنیم که ازین جا کد هامون رو راحت دیباگ کنیم ببینیم و با هر سیو سرورمون ریلود بشه و سایت رو راحت تر ببینیم

python manage.py runserver
این دامنه پروژه مون هست:
 http://127.0.0.1:8000/

حالا میخواهیم ویو را بنوسیسم داخل فایل view.py
و سپس میخوایم url را بهش اضافه کنیم.
بعد توی url.py ادرسش رو اضافه میکنیم 
و توی setting.py هم اسم اپ رو مینویسیم.

بعد میریم سراغ دیتابیس migration
python manage.py migrate

توی سایت زیر میریم :
https://sqliteonline.com/
و sqlite داخل پروژه جنگومان رو بهش اضافه میکنیم
بعد میتوانیم مدل هامون رو بسازیم و بعد باید به دیتابیس وصل کنیم
دستور زیر به ما میگه که چه مدل هایی ساخته شده
python manage.py makemigrations
و بعد دستور رو به را میزنیم و به پروژه اضافه میشه و داخل sqlite اضافه میشه
python manage.py migrate

حالا میخوایم یک مدل را داخل بخش ادمین رجیستر کنیم
python manage.py createsuperuser
و یک سوپر یوزر ایجاد میکنیم

Username (leave blank to use 'yasaman'): 
Email address: y.k.r7713@gmail.com

حالا چگونه به صفحه ادمین دسترسی داشته باشیم :
http://127.0.0.1:8000/admin
وارد صفحه مون میشیم  و از قسمت testmodel یک محصولی وارد میکنیم.

------------------------------------------------------------------------------------
بهتره که اول با مدل ها شروع کنیم برای ایجاد پروژه

بعد از اینکه مدل را ایجاد کردیم و فولدر تمپلیت را ایجاد کردیم و داخلش ویو را اضافه کردیم باید ویو را باید به یک یو ار ال متصل کنیم که بهش دسترسی داشته باشیم.
۲ تا متد مهم داریم  action , method
و متد get , post
یک ریکو‍عست میفرستیم از نوع  get برای url
 گت : برای گرفتن اطلاعات از سرور url ویو را ران میکنه و ویو میری از سرورو دیتایی ک میخوایم میگیره و به صورت لیست نمایش میده
پست : دیتایی را به سرور بفرستیم
---------------------------------------------
داخل  پوشه static می تونیم فایل های سی اس اس و جی اس و اینارو بذاریم
--

ما یک موجودیت با رابطه یک به چند داریم که یعنی یک یوزر می تواند چندین بلاگ یا محصول اضافه کند و هر محصولی تنها توسط یک یوزر ساخته شده است.
--
کاربر می تواند در سایت ثبت نام کند و لاگ این کند.
http://127.0.0.1:8000/account/signup/ از طریق این ادرس ثبت نام میکند
http://127.0.0.1:8000/account/login/ از طریق این ادرس وارد میشود
http://127.0.0.1:8000/testappurl/ این ادرس هم پنل کاربری است که می تواند چیزی اضافه کنید ک توی همین صفحه نشون داده میشه




source :::: https://www.youtube.com/channel/UCw9CcaW7usjx--4cCIYh7rg
