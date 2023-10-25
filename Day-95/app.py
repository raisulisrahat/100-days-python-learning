# Here I am showing DavOps Project Day 5

from flask import Flask, render_template

app = Flask(__name__)

# Mock data (replace with real data sources)
data = {
    'server1': {
        'cpu_usage': 80,
        'memory_usage': 60,
    },
    'server2': {
        'cpu_usage': 45,
        'memory_usage': 75,
    },
    # Add more servers and metrics as needed
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
