from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

server = 'saitejaserver12.database.windows.net'
database = 'saitejadatabase12'
username = 'saiteja12'
password = 'Tennis...123'
driver= '{SQL Server}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        min_pop = int(request.form['min_pop'])
        max_pop = int(request.form['max_pop'])
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        query = "SELECT city, state FROM dbo.data WHERE population >= ? AND population <= ?"
        params = (min_pop, max_pop)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cnxn.commit()
        cnxn.close()
        return render_template('results.html', cities=results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
