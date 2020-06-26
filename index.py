from flask import Flask
from flask import render_template
app = Flask (__name__)

context = {
    'site_name': 'MetaDash'
}

@app.route('/') 
def index():
    return render_template('index.html',context=context) 

@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/informatique/')
def info():
	return render_template('informatique/index.html')


@app.route('/informatique/linux_shell')
def infoLinuxShell():
	return render_template('informatique/linux_shell.html')

@app.route('/informatique/git')
def infoGit():
	return render_template('informatique/git.html')


@app.route('/informatique/python')
def infoPython():
	return render_template('informatique/python.html')


@app.route('/informatique/html')
def infoHtml():
	return render_template('informatique/html.html')


@app.route('/informatique/irc')
def infoIrc():
	return render_template('informatique/irc.html')




#cp clean_template.html informatique/index.html  informatique/linux_shell.html informatique/git.html   informatique/python.html   informatique/html.html  informatique/irc.html
