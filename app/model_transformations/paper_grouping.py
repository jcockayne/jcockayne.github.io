def group_papers(papers):
	years = []
	_ = [years.append(p.year) for p in papers if p.year not in years]
	years.sort(reverse=True)

	working = [('Working Papers', [p for p in papers if not p.is_published])]
	by_year = [(y, [p for p in papers if p.is_published and p.year == y]) for y in years]

	return working + by_year