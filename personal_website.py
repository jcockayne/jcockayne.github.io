#!/usr/bin/env python3
from flask import Flask, render_template
from models.paper import *
app = Flask("personal_website")

authors = {
	"jon": Author("Jon", "Cockayne", is_me=True),
	"chris": Author("Chris", "Oates", "https://oates.work"),
	"ilse": Author("Ilse", "Ipsen", "https://ipsen.math.ncsu.edu"),
	"mark": Author("Mark", "Girolami", "https://www.turing.ac.uk/people/programme-directors/mark-girolami"),
	"tim" : Author("Tim", "Sullivan", "http://www.tjsullivan.org.uk/"),
	"robert" : Author("Robert", "Aykroyd", "http://www1.maths.leeds.ac.uk/~robert/"),
	"simon" : Author("Simon", "Bartels", "https://pn.is.tuebingen.mpg.de/person/sbartels"),
	"philipp": Author("Philipp", "Hennig", "https://pn.is.tuebingen.mpg.de/person/phennig"),
	"fx": Author("Francois-Xavier", "Briol", "https://fxbriol.github.io/"),
	"junyang": Author("Junyang", "Wang", "https://www.turing.ac.uk/node/1982")
}
papers = [
	PublishedPaper(
		"A Bayesian Conjugate Gradient Method",
		[authors["jon"], authors["chris"], authors["ilse"], authors["mark"]],
		2019,
		"1801.05242",
		"Bayesian Analysis",
		note="to appear with rejoinder",
	),
	PublishedPaper(
		"Bayesian Probabilistic Numerical Methods",
		[authors["jon"], authors["chris"], authors["tim"], authors["mark"]],
		2019,
		"1702.03673",
		"SIAM Review",
		note="to appear",
	),
	PublishedPaper(
		"Bayesian Probabilistic Numerical Methods in Time-Dependent State Estimation for Industrial Hydrocyclone Equipment",
		[authors["chris"], authors["jon"], authors["robert"], authors["mark"]],
		2019,
		"1707.06107",
		"Journal of the American Statistical Association"
	),
	PublishedPaper(
		"Probabilistic Linear Solvers: A Unifying View",
		[authors["simon"], authors["jon"], authors["ilse"], authors["philipp"]],
		2019,
		"1810.03398",
		"Statistics and Computing",
		note="to appear"
	),
	PublishedPaper(
		"Convergence Rates for a Class of Estimators Based on Stein's Method",
		[authors["chris"], authors["jon"], authors["fx"], authors["mark"]],
		2019,
		"1603.03220",
		"Bernoulli"
	),
	PublishedPaper(
		"On the Bayesian Solution of Differential Equations",
		[authors["junyang"], authors["jon"], authors["chris"]],
		2017,
		"1805.07109",
		"Proceedings of the 38th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering"
	),
	PublishedPaper(
		"Probabilistic Numerical Methods for PDE-Constrained Bayesian Inverse Problems",
		[authors["jon"], authors["chris"], authors["tim"], authors["mark"]],
		2016,
		"1701.04006",
		"Proceedings of the 38th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering"
	)
]

talks = [
	Talk(where="James H. Wilkinson Workshop, Manchester University", when="29-30 May 2019"),
	Talk(where="Potsdam University", when="21 June 2019"),
	Talk(where="SciCADE 2019", when="22-26 July 2019")
]


@app.route("/")
def main():
	return render_template("index.html", papers=papers, talks=talks)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')