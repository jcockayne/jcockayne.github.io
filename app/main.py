#!/usr/bin/env python3
from flask import Flask, render_template
import data
import model_transformations
app = Flask("personal_website")

@app.route("/")
def main():
	grouped_papers = model_transformations.group_papers(data.papers)
	return render_template("index.html", grouped_papers=grouped_papers, talks=data.talks)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')