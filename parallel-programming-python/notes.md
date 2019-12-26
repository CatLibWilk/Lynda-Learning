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
    - process: instance of program being executed (code, data, info about its state)
        - each independent with own address space in memory
    - threads: subelements within a larger process
        - basic unit that OS manages
        - threads can easily share data as part of same process, but sharing data across processes is more difficult
            - variables and data isolated within processes' address space
     
    - sharing data between different processes
        - requires system-provided: Inter-process communication(IPC) mechanisms
            - sockets/pipes
            - shared memory space
            - remote procedure calls
        
        - using multiple threads vs. multiple processes
            - if application distributed across several computers, will likely need multiprocessing 
            - if can structure program to take advantage of multiple threads, do so
                - threads are more `lightweight`, require less overhead
    
    - Concurrency vs parallelism
        - concurrency: ability of program to be broken into parts that can operate independently
            - in concurrency, indep. processes use same resources, so only one process can occur at a time
            - useful for I/O dependent tasks 
        - parallelism: simultaneous execution
            - useful for computationally-intensive tasks
    
    - Global Interpreter Lock
        - prevents concurrent threads from executing in parallel
        - one one thread executing at a time
        - CPython requires GIL and is default interpreter
        - can act as bottleneck to CPU-bound applications 
        - this doesnt mean don't write multi-thread programs
            - for I/O-bound tasks, GIL is not a bottleneck, because they're mostly waiting on external actions like network operations and user input

    - Threading example in folder 02_04
    
    - true parallelism requires using python multiprocessing module
        - for to work, main body of code must be wrapped in __name__ = __main__ statement
    
    - OS has scheduler module, which is OS function that assigns processes and threads to run on available CPUs
        - puts waiting processes in ready queue or I/O queue and assigns them to available CPU
            - may decide one process has had enough time on CPU and swap it out = `context switch` 
                - will store state of process or thread to resume later
                - also must load stored state of process or tread to start
        
        - scheduling not consistent across runs, or equal, should not be relied on to be so
    
    - thread lifecycle
        - can be in one of four states: new, runnable, blocked (e.g. waiting for input or etc.), terminated
    
    - two ways to create thread (see 02_09)
        - put execution code in function, pass function to thread constructed method with `target` param
        - define custom subclass that inherits from thread class and overrides its run method

        - calling .join() on the subclass within the manager class needed to prevent the manager/main class from continuing with execution until the subclass is finished.
        - can use .is_alive() method to return boolean giving active/inactive status of a thread

    - daemon threads (see 02_11)
        - if a norm child thread is spawned to do sth. like garbage collection, the main program cant end until this child is finished with its job
        - by making a daemon thread, they can be detached from main thread and put in background.
            - need to ensure it wont have any negative effects if the daemon thread closes abruptly/ungracefully
        - make daemon with `[thread varname].daemon = True`
            - must set this before starting the thread