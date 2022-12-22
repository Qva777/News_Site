python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
echo SECRET_KEY=YOUR_SECRET_KEY > .env
echo DEBUG=True >> .env
python manage.py migrate
python manage.py runserver