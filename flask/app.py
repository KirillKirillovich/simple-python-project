from flask import Flask, send_from_directory, abort
import os
app = Flask(__name__)


@app.route('/')
def return_content():
    start_page = './files/html'
    file_path = os.path.join(start_page, 'index.html')

    if os.path.exists(file_path):
        return send_from_directory(start_page, 'index.html')
    else:
        abort(404, description="File not found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
