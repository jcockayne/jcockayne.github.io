from models.paper import *

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
	"junyang": Author("Junyang", "Wang", "https://www.turing.ac.uk/node/1982"),
	"dennis": Author("Dennis", "Prangle", "https://dennisprangle.github.io/"),
	"wilson": Author("Wilson", "Chen", "https://github.com/wilson-ye-chen"),
	"marina": Author("Marina", "Riabiz", "https://www.kcl.ac.uk/people/marina-riabiz"),
	"pawel": Author("Pawel", "Swietach", "https://www.dpag.ox.ac.uk/team/pawel-swietach"),
	"steve": Author("Steven", "Niederer", "https://www.kcl.ac.uk/people/steven-niederer"),
	"lester": Author("Lester", "Mackey", "https://web.stanford.edu/~lmackey/"),
	"tim_reid": Author("Tim", "Reid", "https://math.sciences.ncsu.edu/people/twreid/"),
	"andrew": Author("Andrew", "Duncan", "http://wwwf.imperial.ac.uk/~aduncan/"),
	"matt": Author("Matthew", "Graham", "https://matt-graham.github.io/"),
	"toni": Author("Toni", "Karvonen", "https://tskarvone.github.io/"),
	"filip": Author("Filip", "Tronarp", "https://scholar.google.fi/citations?user=q0rtB0EAAAAJ&hl=sv"),
	"simo": Author("Simo", "Särkkä", "https://users.aalto.fi/~ssarkka/"),
	"oksana": Author("Oksana", "Chkrebtii", "https://www.asc.ohio-state.edu/chkrebtii.1/research.html")
}

papers = [
	Paper(
		"A Probabilistic Taylor Expansion with Applications in Filtering and Differential Equations",
		[authors["toni"], authors["jon"], authors["filip"], authors["simo"]],
		2021,
		"2102.00877"
	),
	Paper(
		"Testing whether a Learning Procedure is Calibrated",
		[authors["jon"], authors["matt"], authors["chris"], authors["tim"]],
		2020,
		"2012.12670"
	),
	Paper("Probabilistic Gradients for Fast Calibration of Differential Equation Models",
		[authors["jon"], authors["andrew"]],
		2020,
		"2009.04239",
		"SIAM Review (to appear)"
	),
	Paper(
		"BayesCG As An Uncertainty Aware Version of CG",
		[authors["tim_reid"], authors["ilse"], authors["jon"], authors["chris"]],
		2021,
		"2008.03225"
	),
	PublishedPaper(
		"Probabilistic Iterative Methods for Linear Systems",
		[authors["jon"], authors["ilse"], authors["chris"], authors["tim_reid"]],
		2021,
		"2012.12615",
		"Journal of Machine Learning Research (to appear)"
	),
	PublishedPaper("Bayesian Numerical Methods for Nonlinear Partial Differential Equations",
		[authors["junyang"], authors["jon"], authors["oksana"], authors["tim"], authors["chris"]], 
		2021,
		"2104.12587",
		"Statistics and Computing",
		journal_website="https://doi.org/10.1007/s11222-021-10030-w"
	),
	PublishedPaper(
		"Optimal Thinning of MCMC Output",
		[authors["marina"], authors["wilson"], authors["jon"], authors["pawel"], authors["steve"], authors["lester"], authors["chris"]],
		2021,
		"2005.03952",
		"Journal of the Royal Statistical Society Series B (to appear)"
	),
	PublishedPaper(
		"Optimality Criteria for Probabilistic Numerical Methods",
		[authors["chris"], authors["jon"], authors["dennis"], authors["tim"], authors["mark"]],
		2020,
		"1901.04326",
		"Multivariate Algorithms and Information-Based Complexity",
		journal_website="https://www.degruyter.com/view/book/9783110635461/10.1515/9783110635461-005.xml"
	),
	PublishedPaper(
		"A Role for Symmetry in the Bayesian Solution of Differential Equations",
		[authors["junyang"], authors["jon"], authors["chris"]],
		2020,
		"1906.10564",
		"Bayesian Analysis",
		journal_website="https://projecteuclid.org/euclid.ba/1571191351"
	),
	#Paper(
	#	"Probabilistic Numerical Methods for Partial Differential Equations and Bayesian Inverse Problems",
	#	[authors["jon"], authors["chris"], authors["tim"], authors["mark"]],
	#	2017,
	#	"1605.07811"
	#),
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
		"On the Sampling Problem for Kernel Quadrature",
		[authors["fx"], authors["chris"], authors["jon"], authors["wilson"], authors["mark"]],
		2017,
		"1706.03369",
		"Proceedings of the 34th International Conference on Machine Learning",
		journal_website="http://proceedings.mlr.press/v70/briol17a.html"
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