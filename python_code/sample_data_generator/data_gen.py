from sklearn import cluster, datasets
n_samples = 150000
circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
fn = "data.txt"
fd = open(fn, "w")
for i in range(len(circles[0])):
	fd.write(circles[0][i][0].__str__() + " " + circles[0][i][1].__str__() + " " + circles[1][i].__str__() + "\n")
fd.close()
