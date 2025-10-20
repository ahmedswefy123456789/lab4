# Run the Django development server using the project's virtualenv python
$python = "C:/Users/iti174/Desktop/p2/look/Scripts/python.exe"
& $python c:\Users\iti174\Desktop\p2\school\manage.py makemigrations
& $python c:\Users\iti174\Desktop\p2\school\manage.py migrate
& $python c:\Users\iti174\Desktop\p2\school\manage.py runserver 0.0.0.0:8000
