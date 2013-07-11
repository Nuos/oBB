# Example code for oBB
from obb import obb
from numpy import sin,cos,diag,ones,zeros

# Input Settings
# Algorithm (T1, T2_individual, T2_synchronised)
alg = 'T1'

# Model type (q - norm quadratic, c - norm cubic, g/Hz/lbH/E0/Ediag - min eig. quadratic, 
# gc - gershgorin cubic)
mod = 'c'

# Tolerance
tol = 1e-2

# Heuristic lattice (0 - off, 1 - on)
heur = 0

# Tolerance type (r - relative, a - absolute)
toltype = 'r'

# Visualisation !!Requires matplotlib!! (0 - off, 1 - on)
vis = 0

# Tensor diagonal function
def diagt(v):
    T = zeros((D,D,D))
    for i in range(0,D):
	    T[i,i,i] = v[i]
    return T

# Set up sum of sins test function
# Dimension
D = 2
# Constraints
l = -1*ones(D)
u = 1*ones(D)
A = ones((1,D))
lc = -1; uc = 1
# Required functions
f = lambda x: sum(sin(x))
g = lambda x: cos(x)
H = lambda x: diag(-sin(x))
bndH = lambda l,u: (diag(-ones(D)), diag(ones(D)))
bndT = lambda l,u: (diagt(-ones(D)), diagt(ones(D)))

# Name objective function
f.__name__ = 'Sum of Sins'

# Run oBB
xs, fxs, tol, itr = obb(f, g, H, bndH, bndT, l, u, alg, mod, A=A, lc=lc, uc=uc, tol=tol, heur=heur, toltype=toltype, vis=vis)
