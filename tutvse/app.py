from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'username': 'abay', 'email': 'genyi@mail.ru'},
        {'username': 'yerkanat', 'email': 'luchshiy@mail.ru'},
        {'username': 'otsenka', 'email': 'dvenadtsatballovpls@mail.ru'}
    ]
    return render_template('home.html', users=users)

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)
