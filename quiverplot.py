import tables 
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

# load data calculated using MATLAB
file = tables.open_file('data3.mat')
X = file.root.X[:]
Y = file.root.Y[:]
dh = file.root.dh[:]
ds = file.root.ds[:]
s_line = file.root.s_line
numb_lines = s_line.shape[0]
h_line = file.root.h_line

s_line2 = file.root.s_line2
h_line2 = file.root.h_line2
numb_lines2 = h_line2.shape[0]

# plotting
fig = plt.figure()
for ii in range(numb_lines):
    plt.plot(h_line, s_line[ii,:],'b-')
for ii in range(numb_lines2):
    plt.plot(h_line2[ii,:], s_line2,'r-')

# change title and labels, depend on what is plotted
#plt.title('Sir2 Double expression/Hap overexpression')
#plt.title('Sir2 Double expression')
#plt.title('WT')
#plt.title('No Mutual Inhibition')
#plt.title('hap deletion')
#plt.title('sir2 deletion')
plt.xlabel('hap4/hem')
plt.ylabel('sir2')

# plot quivers
Q = plt.quiver(X, Y, 0.2*dh, ds, units='width', color='gray', alpha = 1)

# save figure as eps
fig.savefig('/home/yanfei/Dropbox/shared data_aging/Hap_deletion.eps')
plt.show()
