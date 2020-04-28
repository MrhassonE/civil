from flask import Flask, render_template, redirect, request
from sqlalchemy import create_engine
from db import db_url
app = Flask(__name__)

engine = create_engine(db_url)
conn = engine.connect()


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


# ARABIC
@app.route('/a')
def indexA():
    return render_template('index2.html')


@app.route('/a/asia', methods=["GET", "POST"])
def asiaA():
    if request.method == "GET":
        return render_template('asia2.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilA WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page2.html", information=result)

@app.route('/a/america', methods=["GET", "POST"])
def americaA():
    if request.method == "GET":
        return render_template('america2.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilA WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page2.html", information=result)

@app.route('/a/africa', methods=["GET", "POST"])
def africaA():
    if request.method == "GET":
        return render_template('africa2.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilA WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page2.html", information=result)

@app.route('/a/europe', methods=["GET", "POST"])
def europeA():
    if request.method == "GET":
        return render_template('europe2.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilA WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page2.html", information=result)



# ENGLISH
@app.route('/e')
def indexE():
    return render_template('index.html')

@app.route('/e/asia', methods=["GET", "POST"])
def asiaE():
    if request.method == "GET":
        return render_template('asia.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilE WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page.html", information=result)

@app.route('/e/america', methods=["GET", "POST"])
def americaE():
    if request.method == "GET":
        return render_template('america.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilE WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page.html", information=result)

@app.route('/e/africa', methods=["GET", "POST"])
def africaE():
    if request.method == "GET":
        return render_template('africa.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilE WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page.html", information=result)

@app.route('/e/europe', methods=["GET", "POST"])
def europeE():
    if request.method == "GET":
        return render_template('europe.html')
    else:
        country = request.form.get('country')
        era = request.form.get('era')
        result = engine.execute('SELECT * FROM civilE WHERE country=? AND era=?', (country, era,))
        result = result.fetchone()
        return render_template("civil_page.html", information=result)

@app.route('/e/map', methods=["GET", "POST"])
def map():
    if request.method == "GET":
        return render_template("civils-page.html")
    else:
        lines = request.form.get('submit').split("||")
        return render_template("civils-page.html", lines=lines)



if __name__ == "__main__":
    
    app.run()