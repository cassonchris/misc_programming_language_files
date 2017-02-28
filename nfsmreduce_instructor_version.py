def nfsmtrim(edges, accepting):
	# Gather up all of the states, possibly with duplicates.
	states = [ ]
	for e in edges:
		states = states + [e[0]] + edges[e]
	# A state is live if there is some way to accept starting from it.
	live = [ ]
	for s in states:
		if nfsmaccepts(s,edges,accepting,[]) != None:
			live = live + [s]
	# Now that we know what is live, build up the output.
	new_edges = { }
	for e in edges:
		if e[0] in live:
			new_destinations = [ ]
			for destination in edges[e]:
				if destination in live:
					new_destinations = new_destinations + [destination]
			if new_destinations != []:
				new_edges[e] = new_destinations
	new_accepting = [ ]
	for s in accepting:
		if s in live:
			new_accepting = new_accepting + [s]
	return (new_edges, new_accepting)