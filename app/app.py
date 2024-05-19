from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    title = request.form.get('title')
    content = request.form.get('content')
    posts.append({'title': title, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
