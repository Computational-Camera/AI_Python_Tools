import numpy as np

#Least Square Fitting, Ax=b, not necessarily linear fitting
#i.e. quadratic (non linear) fitting by extending the rows of A in the form of x*x, y*y, x*y and constant
x, err, rank, s= np.linalg.lstsq(A,b)
#still not sure why err does not work


#concrete example, 2D plane fitting using normal euqation
tmp_A = []
tmp_b = []
for i in range(len(ptx)):
    tmp_A.append([ptx[i], pty[i], 1]) # constant coefficient term should be included
    tmp_b.append(ptz[i])
b = np.matrix(tmp_b).T
A = np.matrix(tmp_A)
fit = (A.T * A).I * A.T * b
errors = b - A * fit
residual = np.linalg.norm(errors)
