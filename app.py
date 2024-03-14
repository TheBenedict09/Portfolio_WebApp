from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('main.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')

if __name__ == "__main__":
    app.run(debug=True)