## Project Zoro
Personal Django practice
</br></br>

## Goal
Implement CRUD using Django, Django Rest Framework, and sqlite3
</br></br>

## Environment
Make virtual environment first

`python -m venv ~/.virtualenv/zoro`

</br>

Install django and djangorestframework

`pip install django djangorestframework`

</br>

Activate the virtualenv

`source ~/.virtualenv/zoro/bin/activate`

</br>

Now you're ready to develop zoro
</br></br>

## Execute
Execute django with listening address you want to run with

`cd zoro_server`

`python manage.py runserver [IP]:[Port]`

</br>

You may need to migrate first using command below

`python manage.py migrate`
</br></br>

## APIs
Check DRF on http://[IP]:[Port]/devices/*

- GET
    - /devices
    - /devices/{id}

- POST
    - /devices
        - {serial, ip, priority, last_update}
- PUT
    - /devices/{id}
        - {id, serial, ip, priority, last_update}

- DELETE
    - /devices/{id}

</br>
All media types are application/json

</br></br>

## References
- https://docs.djangoproject.com/en/5.1/intro/tutorial01/
- https://modulabs.co.kr/blog/about_drf/
