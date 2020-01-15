# Cache-Simulator
Example command line with real trace
python sim_424.py 403.gcc.gz 16384 16 128 1000,
where 403.gcc.gz is a trace file stored in ../Traces
16384 is the cache size in bytes
2 is the number of ways
128 is the number of bytes per block (i.e.. BlockBits = 7: 2 for byte offset, 5 for block
offset has there are 32 words)
1000 is the number of simulated lines from the trace file. Each trace file has 100s
of thousands of lines.



400.perlbench	C	PERL Programming Language
401.bzip2	C	Compression
403.gcc	C	C Compiler
429.mcf	C	Combinatorial Optimization
445.gobmk	C	Artificial Intelligence: go
456.hmmer	C	Search Gene Sequence
458.sjeng	C	Artificial Intelligence: chess
462.libquantum	C	Physics: Quantum Computing
464.h264ref	C	Video Compression
471.omnetpp	C++	Discrete Event Simulation
473.astar	C++	Path-finding Algorithms
483.xalancbmk	C++	XML Processing
CFP2006 has 17 benchmarks: 4 use C++, 3 use C, 6 use Fortran, and 4 use a mixture of C and Fortran. The benchmarks are:

410.bwaves	Fortran	Fluid Dynamics
416.gamess	Fortran	Quantum Chemistry
433.milc	C	Physics: Quantum Chromodynamics
434.zeusmp	Fortran	Physics/CFD
435.gromacs	C/Fortran	Biochemistry/Molecular Dynamics
436.cactusADM	C/Fortran	Physics/General Relativity
437.leslie3d	Fortran	Fluid Dynamics
444.namd	C++	Biology/Molecular Dynamics
447.dealII	C++	Finite Element Analysis
450.soplex	C++	Linear Programming, Optimization
453.povray	C++	Image Ray-tracing
454.calculix	C/Fortran	Structural Mechanics
459.GemsFDTD	Fortran	Computational Electromagnetics
465.tonto	Fortran	Quantum Chemistry
470.lbm	C	Fluid Dynamics
481.wrf	C/Fortran	Weather Prediction
482.sphinx3	C	Speech recognition

https://www.spec.org/cpu2006/Docs/readme1st.html
https://www.spec.org/cpu2006/:
