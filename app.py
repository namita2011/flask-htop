from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getenv('USER') or os.getenv('USERNAME')  # Get system username
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    # Get 'top' output (or 'htop' if installed)
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True).decode('utf-8')
    except Exception as e:
        top_output = f"Error getting top output: {e}"

    # Format the output
    html = f"""
    <html>
        <body>
            <h1>/htop Endpoint</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
