# Programming Foundations: Memory, Pointers, and Garbage Collection.
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/16202f3f367a8e0014668328712d0845638c508e5c5f7d3d0d3685aaeb3d378d)

### Memory:
- Long/Short term memory.
- (***RAM***) = Main Memory:
    - Random-Access Memory => volatile.
    - Accessible by CPU.
    - Data and logic loaded into RAM for execution.
    - Fast access.
    - Variables and objects are stored in RAM. 
- (***ROM***): Main Memory:
    - Read-Only Memory => non-volatile.
- RAM is managed by OS, application, CPU. 
- *Memory Allocation*: assigning of a memory address and reserving it to store a certain value, program, or process.
    - Static: compile time, prior to the program execution.
    - Dynamic: run time, happens during execution of the program.
        - Adding new values to teh heap. 
> Differs from a langauage to langauge.
- *Memory Deallocation*: releasing the memory when it no longer needs to hold values. So it can be allocated again.
    - For heap deallocation: Fragmentation of the heap and it is hard to determine when a memory adress is ready for deallocation.

> Allocation and Deallocation are the memory management Types.
- Manual Memory Management (MMM): 
    - Developers has to allocate and deallocate the memory in code => C
    - Helps to understand what is going on. 
    - Can be more efficient.
    - Boilerplate code.
    - Prone to errors.
- Automatic Memory Management (AMM):
    - Memory management is build-in service of the language or interpreter.
    - Allocation and deallocation are done by the service.
    - Saves boilerplate code. 
    - Less prone to errors.
    - JS, python, perl, high-level languages.
- ***Stack***: 
    - Data structure (LIFO)
    - Stack Area is part of Memory RAM.
    - Stack records.
    - Order of function.
    - Points to stack record on a stack memory. 
    - Stack has a max number of records and records have a max size. If the limit is exceeded, "Stack overflow error" occurs.
- ***Heap***:
    - Part of RAM, used for storing values that need to be accessible through more than one function. 
    - z variable is accessed by all other functions so we store it in a heap memory. 
- ***Heaps Vs. Stacks***:
- Similarities: 
    - Both are areas on the RAM.
    - They are needed to run an application.
    - Both can hold values needed for program execution.
- Differences:
    - Heap:
        - Variables. 
        - Values and objects that need to be accessible globally.
        - Deallocated when it doen't have a connection to the stack anymore.
        - Accessing elements on heap is slower than stack.
        - Heap can be accessed by any thread.
    - Stack:
        - Order of execution.
        - Internal values of each function.
        - Deallocated when function is done.
        - Accessing elements on stack is faster than accessing heap elements. 
        - Stack record can only be accessed by its owner thread.
        - More secure.
> Concurrency: execution of multiple threads at the same time.
### Garbage Collection:
- Freeing the heap memory.
- Manual Garbage collection: C...
- Automatic Garbage collection: C#, python...
- Avoids certain errors: Dangling pointer bug and freeing up the memory twice. 
- Garbage collection expensive process. 
- *Sweeping*:
    - Normal sweeping: Memory is fragmanted.
    - Sweeping with compactng: Never leaves gaps but apply compacting.
    - Sweeping with copying: Extra peice, Performance. 
> High level languages have GC build in.
### C Memory Management:
- Memory management is visible in C.
- Memory in C consists of:
    - Stack.
    - Heap.
    - BSS: Block Starting Symbol.
    - DS: Data Segment.
    - Text.
- Local variables are stored in Stack on C.
- Stack space is limited.
- Heap allows dynamic memory allocation. 
- Heap Allocates manually in C through pointers: 
    - malloc (memory allocation) => a method for dynamically allocating blocks of memory of specific sized. 
    - calloc (contigous allocation) => a method for dynamically allocating blocks of memory and initizlizes to zero.
    - realloc(reallocation) => a method for dynamically reallocating blocks of memory. 
- Function =>Free: 
    - Starting address of the memory block.
    - Frees the memory.
    - Memory can be allocated again.
- Function => realloc:
    - Assigns a new memory blok with a new size to a variable.
    - Starting address of the old memory block and new size.
    - Doesn't free the old memory.
### Python Memory Management:
- Automatic  Memory Management (AMM):
   - Improves quality.
   - Less bugs.
   - Less performance issues.
   - Try to use language with automatic memory management.
- Differs depending on the language. 
- Python is dynamically typed => no need to write type of variable.
    - Arena has pools and pools contain blocks. 
    - Blocks are of the same size. 
    - Usable arenas.
    - Pools lists.
    - Pools have a state: full, used, empty.
    - Blocks have states: untouched, free, allocated.
    - Multithreading: multiple threads trying to access at the same time. (GIL)
### Memory Leaks:
- Memory leaks: accumulation of objects on the memory no longer needed => leads to system's slow down.
- RAM is limited resource that can get full.
- Causes of memory leaks:
    - In C: 
        - Manual memory management.
        - Forgetting to free memory.
        - Severance depends on the place where the free method is forgotten. 
    - In python:
        - Memory leaks exist because the build-in garbage collector perceives the allocated memory as needed.
        - Typically due to coding or design flaw.
- Out-of-Memory Error: Happens when system cannot allocate a requested memory block anymore.
- Memory leaks issues:
    - Restarting will free the uncessarily kept memory, but it won't solve the problem.
    - Cloud bills could become high.
    - Slow down.
- How to avoid memory leaks:
    - Memory errors are caused by:
        - Loading large files.
        - 32-bit Python on 64-bit system.
        - Keep object references unnecesserily.
    - Use Generator functions.
### Best Practices for MM in Python:
- Escaping references.
- Mutable objects.
- Deep Copy: copying the object and its mutable attributes.
- Slots in python. 
- Explore.


