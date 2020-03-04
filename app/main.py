#!/usr/bin/env python3
from flask import Flask, render_template
from models.paper import *
import model_transformations
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
		"A Role for Symmetry in the Bayesian Solution of Differential Equations",
		[authors["junyang"], authors["jon"], authors["chris"]],
		2019,
		"1906.10564",
		"Bayesian Analysis",
		note="to appear"
	),
	Paper(
		"Probabilistic Numerical Methods for Partial Differential Equations and Bayesian Inverse Problems",
		[authors["jon"], authors["chris"], authors["tim"], authors["mark"]],
		2017,
		"1605.07811"
	),
	PublishedPaper(
		"A Bayesian Conjugate Gradient Method",
		[authors["jon"], authors["chris"], authors["ilse"], authors["mark"]],
		2019,
		"1801.05242",
		"Bayesian Analysis",
		journal_website="https://projecteuclid.org/euclid.ba/1558144846",
		note="with discussion and rejoinder",
		other_links=[
			PaperLink("https://www.youtube.com/watch?v=RDTOaPtxAXU", "BA Webinar", "fab fa-youtube")
		]
	),
	PublishedPaper(
		"Bayesian Probabilistic Numerical Methods",
		[authors["jon"], authors["chris"], authors["tim"], authors["mark"]],
		2019,
		"1702.03673",
		"SIAM Review",
		journal_website="https://epubs.siam.org/doi/abs/10.1137/17M1139357",
	),
	PublishedPaper(
		"Bayesian Probabilistic Numerical Methods in Time-Dependent State Estimation for Industrial Hydrocyclone Equipment",
		[authors["chris"], authors["jon"], authors["robert"], authors["mark"]],
		2019,
		"1707.06107",
		"Journal of the American Statistical Association",
		journal_website="https://www.tandfonline.com/doi/full/10.1080/01621459.2019.1574583"
	),
	PublishedPaper(
		"Probabilistic Linear Solvers: A Unifying View",
		[authors["simon"], authors["jon"], authors["ilse"], authors["philipp"]],
		2019,
		"1810.03398",
		"Statistics and Computing",
		journal_website="https://link.springer.com/article/10.1007/s11222-019-09897-7"
	),
	PublishedPaper(
		"Convergence Rates for a Class of Estimators Based on Stein's Method",
		[authors["chris"], authors["jon"], authors["fx"], authors["mark"]],
		2019,
		"1603.03220",
		"Bernoulli",
		journal_website="https://projecteuclid.org/euclid.bj/1551862846"
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
		"Proceedings of the 38th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering",
		journal_website="https://aip.scitation.org/doi/abs/10.1063/1.4985359"
	)
]

talks = [
	Talk(where="RSS 2020", when="7-10 September 2020")
]


@app.route("/")
def main():
	grouped_papers = model_transformations.group_papers(papers)
	return render_template("index.html", grouped_papers=grouped_papers, talks=talks)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')