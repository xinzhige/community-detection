# This program is to calculate the modularity 
# by given a matrix-like graph and a vector-like membership
# Need to install the igraph package

library(igraph)

modularity <- function(graph, membership) {
  ms <- membership
  d <- max(ms) # number of communities
  e <- matrix(0, nrow=d, ncol=1)
  a <- matrix(0, nrow=d, ncol=1)
  m <- ecount(graph)
  edges <- get.edgelist(graph)
	
  for (i in 1:m) {
    edge <- edges[i,]
	from <- edge[1]
	to <- edge[2]
	c1 <- ms[from]
	c2 <- ms[to]
	if (c1 == c2) {
	  e[c1, 1] <- e[c1, 1] + 2
	}
	a[c1, 1] <- a[c1, 1] + 1
	a[c2, 1] <- a[c2, 1] + 1
  }
	
  e <- e/2/m
  a <- a/2/m
  tmp <- crossprod(a,a)
  q <- sum(e) - sum(tmp)
  q
}
