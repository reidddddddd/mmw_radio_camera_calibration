import numpy as np

p = np.array([[1,2,3,1],[2,3,3,1], [3,4,4,1], [4,5,4,1], [5,6,5,1],[6,2,3,1],[7,3,3,1], [8,4,4,1], [9,5,4,1], [10,6,5,1]])
u = np.array([[2,4,6,8,10,12,14,16,18,19]])
v = np.array([[3,4,5,6,7,3,4,5,6,7]])
w =  np.array([[3,3,4,4,5,3,3,4,4,5]])

i = np.ones([1,10])
T1 =(np.linalg.inv(p.T.dot(p)).dot(p.T).dot(u.T)).T
T2 =(np.linalg.inv(p.T.dot(p)).dot(p.T).dot(v.T)).T
T3 =  (np.linalg.inv(p.T.dot(p)).dot(p.T).dot(w.T)).T
T4 =  (np.linalg.inv(p.T.dot(p)).dot(p.T).dot(i.T)).T
T = np.vstack((T1,T2,T3,T4))

anser = p.dot(T.T)
