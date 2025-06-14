from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tcw')
def tcw():
    return render_template('tcw.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True) 