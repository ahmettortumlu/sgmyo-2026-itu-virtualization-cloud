from flask import Flask, request, render_template_string
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        cur.execute('INSERT INTO names (name) VALUES (%s)', (name,))
        conn.commit()

    cur.execute('SELECT name FROM names;')
    rows = cur.fetchall()
    cur.close()
    conn.close()

    html = '''
        <h1>Kayıt Paneli</h1>
        <form method="post">
            İsim: <input type="text" name="name">
            <input type="submit" value="Kaydet">
        </form>
        <ul>
        {% for row in rows %}
            <li>{{ row[0] }}</li>
        {% endfor %}
        </ul>
    '''
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)