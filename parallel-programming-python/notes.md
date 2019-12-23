# Chpt 1 Parallel Computing Hardware
- Parallel Computing Architectures
    - often described using Flynn Taxonomy, Rho-chart-like diagram of multiple vs single datastreams, and multiple vs single instruction streams, resulting in 4 possibilities (SISD, MISD, SIMD, MIMD)
        - multiple datastream = multiple processors
        - MIMD most commonly used, each processor can be working on different set of instructions and different data
        - MIMD further subdivided
            - Single Program, Multiple Data (SPMD)
                - multiple processors executing copy of same single program, each can use different data
                - processors can run async.
                - most common style of parallel programming
            - Multiple Program, Multiple Data (MPMD)
                - multiple processors execute different programs, on different data
                - one processing node acts as manager and farms out data to other nodes running other programs
- shared vs distributed memory
    - shared: all processors access same memory as part of global memory space
        - classified as either Unified Memory Access and Non-Uniform
            - UMA: all processors have equal access to memory
                - most common architecture: symmetric multiprocessing
            -NUMA: some processors have quicker access to certain parts of memory than others
    
    - distributed: each processor has own local memory and address space
        - all processors connected through network (e.g. ethernet)
        - each processor acts independently, changes not reflected in memory of other processors (automatically)
            - programmer must define how/when communication occurs between processors
            - advantage is scalibilty over shared memory system

# Chpt. 2 Threads and Processes