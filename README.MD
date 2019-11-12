In the root of this repo (after installed),
- Create a new virutal environment
    - python3 -m venv env
- Activate it
    - source env/bin/activate
- Install dependencies
    - pip install django
    - pip install djangorestframework
- Make migrations
    - python manage.py makemigrations audio
    - python manage.py migrate
- Run the server
    - python manage.py runserver


Test it with a POST request:
- pip install httpie
- http --json POST http://127.0.0.1:8000/audio/ session_id="123" ts='2019-10-25 14:30:59'
- You should see the server print "Process here!"


To run Shell:
- python manage.py shell
