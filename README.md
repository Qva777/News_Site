<h1>📍How to install: </h1>

<details><summary><h2>🧾Automatic command execution for the first run</h2></summary><br>
<ul>
  <li>🔧for Windows:     <b>first_start.bat</b></li>
  <li>⚙ for Linux/MacOS: <b>sh first_start.sh</b></li>
</ul>
</details>

<details><summary><h2>⚙Manual start for Windows</h2></summary><br>
<h4>1 - Connect venv:</h4> 
<pre>python -m venv venv</pre>
<h4>2 - Activate it:</h4> 
<pre>.\venv\Scripts\activate</pre>
<h4>3 - Install libraries:</h4>
<pre>pip install -r requirements.txt</pre>
<h4>4 - Set secret_key for start:</h4>
<pre>echo SECRET_KEY=YOUR_SECRET_KEY > .env</pre>
<h4>5 - Set debug for start:</h4>
<pre>echo DEBUG=True >> .env</pre>
<h4>6 - Apply migration:</h4> 
<pre>python manage.py migrate</pre>
<h4>7 - Run server:</h4> 
<pre>python manage.py runserver</pre>
</details>


<details><summary><h2>🍏Manual start for MacOS</h2></summary><br>
<h4>1 - Connect venv:</h4> 
<pre>python3 -m venv venv</pre>
<h4>2 - Activate it:</h4> 
<pre>source venv/bin/activate</pre>
<h4>3 - Install libraries:</h4>
<pre>pip install -r requirements.txt</pre>
<h4>4 - Set secret_key for start:</h4>
<pre>echo SECRET_KEY=YOUR_SECRET_KEY > .env</pre>
<h4>5 - Set debug for start:</h4>
<pre>echo DEBUG=True >> .env</pre>
<h4>6 - Apply migration:</h4>
<pre>python3 manage.py migrate</pre>
<h4>7 - Run server:</h4> 
<pre>python3 manage.py runserver</pre>
</details>

