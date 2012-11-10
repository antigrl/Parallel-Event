import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello(name="Chris"):
    return render_template('main.html', name=name)

@app.route('/foo/')
def fello():
        return 'Foo Parallelevent!!'

@app.route('/bar/')
def bello():
        return 'Bar Parallelevent!!'
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
