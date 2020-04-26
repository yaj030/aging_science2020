## Phase plane
The file "phaseplanecalculation.m" is used for calculating the phase plane diagrams in Fig.3 . After calculation, the calculated results are plotted with the Python code "quiverplot.py"(instead of MATLAB) for a better appearance. The kinetic parameters are given at the beginning of the .m file and can be changed accordingly depending on the mutant strain. All parameters are provided in the Supplemental Materials of the paper.
## Potential Landscape
The potential landscape in Fig.3 is calculated with a CUDA program. The source code is given in "fokker-planck_2n.cu". It takes the parameters listed in the "params.dat" file. It must be compiled before use with the following command "*nvcc fokker-planck_2d.cu -lcuda -lcufft -lcublas -O3 -arch sm_20 -o fp2d*" and the output "fp2d" can be used for solving the PDE by simply running the command "*./fp2d*". One example of the output is given, "*n_00100.dat*" , which is the 100th time point result, which is used in the paper. And it can be plotted as landscape with the MATLAB code "plotsurf4.m".
## Hardware and software specifics
Hardware we used for solving the PDE: NVIDIA GeForce GTX 480. CUDA version: 7.5. Note that the CUDA version(nvcc version) has to be compatible with your own hardware, which is the NVIDIA graphic card model. 
MATLAB version: 2015b. Python Version: Python 3.7 coming with Anaconda
