from flask import Flask
app = Flask(__name__)
CONTENT = 'content'


@app.route('/')
def return_content():
    return CONTENT


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    
