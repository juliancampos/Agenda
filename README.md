Python
versão: 3

Framework: Django

Passo a passo:

1) django-admin startproject Agenda
2) pip install django-tastypie
3) python manage.py startapp api
4) inclusão de 'api' na configuração de agenda/settings.py no array INSTALLED_APPS
5) criar o arquivos models.py na pasta 'api'
6) python manage.py makemigrations
7) python manage.py migrate
8) populate database
    python manage.py shell
    >>> from api.models import Note
    >>> note = Note(title="First Note", body="This is certainly noteworthy")
    >>> note.save()
    >>> Note.objects.all()
    <QuerySet [<Note: First Note This is certainly noteworthy>]>
    >>> exit()
9) criar arquivo api/resources.py
10) python manage.py runserver
