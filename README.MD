## Phase plane
The phaseplanecalculation.m is used for calculated the phase plane diagram. After the calculation, the calculated data is plotted with the Python code quiverplot.py(instead of MATLAB) for better appearance. The kinetic parameters are given at the beginning of the .m file and can be changed accordingly depending on the mutant strain. All parameters are listed in the original paper. 
## Potential Lanscape
The potential landscape is calculated with a CUDA program. The source code is given in *fokker-planck_2n.cu*. It takes the parameters listed in the params.dat file. It must be compiled before use with the following command *nvcc fokker-planck_2d.cu -lcuda -lcufft -lcublas -O3 -arch sm_20 -o fp2d* and the output fp2d can be used for solving the PDE by simply run the command *./fp2d*. One example output is given, *n_00100.dat* , which is the 100th time point result. And it can be plotted as landscape with the MATLAB code plotsurf4.m.
## Hardware and software specifics
Hardware we used for solving the PDE: NVIDIA GeForce GTX 480. CUDA version: 7.5. 
MATLAB version: 2015b. Python Version: Python 3.7 coming with Anaconda
