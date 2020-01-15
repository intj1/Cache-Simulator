Example command line with real trace:

python sim_424.py 403.gcc.gz 16384 16 128 1000,

where 403.gcc.gz is a trace file stored in ../Traces

16384 is the cache size in bytes

2 is the number of ways

128 is the number of bytes per block (i.e.. BlockBits = 7: 2 for byte offset, 5 for block

offset has there are 32 words)

1000 is the number of simulated lines from the trace file. Each trace file has 100s

of thousands of lines.


