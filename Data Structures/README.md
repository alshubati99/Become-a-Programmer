# Programming Foundations: Data Structures.
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/bedecbb4774fe5055657f4148fc7f004371e53b7bd61400de943378b96ce4477)

### Data:
- Data is information that is stored and processed by a computer. 
### Data Types:
- An attribute of data that describes the values it can have and how the data can be used. 
- Numbers.
- Letters.
- True(1)
- False(0)
### Numberical Data Types:
- Decimal Numbers:
    - double.(64 bits)
    - float.(32 bits)
- Whole Numbers:
    - short.(16 bits)
    - int.(32 bits)
    - long.(64 bits)
- Difference: is range of numberical values they can store.
- Higher ammount of bits = higher number of values. 
- Not all languages hanve the same data types. 
- Signed: Positive and negitive values.
- Unsigned: Positive numbers only. 
### Boolean Data Types:
- A boolean is a True or False value. 
### Characters Data Types:
- A character is represented by a single quotation mark. 
- A group of charachers forms a string. 
### Primitive Types in Memory:
- Boolean = one bit only either 1 or 0.
- Ints. 
- Doubles.
- Longs.
- Floats. 
- Shorts.
- Booleans.
- Chars
- All have a fixed size.
- There are data types that are build on other data types. 
### Data Structures:
- Help connect and organize data. 
- Help store and process data more effeciently.
- Ease of access to data.  
### Strings:
- Sequence of characters. 
- Build on another data type. 
- Sourounded with single or double quotations. 
- Data structure depends on: 
    - Allocated space for structure.
    - Numbers of pieces of data.
    - Size of each data piece. 
### Primitive vs. Reference Types in Memory:  
- Primitive takes a specific size. 
    - VariableName => data
    - Directly access the data. 
- Reference uses pointers
    - VariableName => MemoryAdress => Value:
    - Strings. 
    - Data Structures.
- Some languages have memory management tools to handle referenced data types. 
### Arrays:
- Array: collection of elements where each items is identified by an index or a key.
- index and data. 
- Index our of bounds error: accessing an index that does not exist. 
- Important for Organization, Storage, Access of data. 
- *2D Arrays*:
    - like Matrices. 2x2 matrix 
- *Jagged Array*:
    - Each row has a differet length. 
    - C# differentiate a jagged array from normal one. 
- *Resizable arrays*:
    - Java, C++: arrays cannot be resized.
    - Ruby, JS: basic arrays can be resized. 
    - Resizebale array= mutable arrays. 
    - Immutable: basic array data. 
    - Mutable: java class give resizable versions. 
    - ArrayList: comes with extra functionaligy.
    - Add, push => Adding to the back of the array. 
    - Remove, pop => Removing from the back of the array. 
- *Search Arrays*:
    - input: object.
    - output: true/false value. 
    - check every item in each index. 
    - if match, return true. 
    - if no match(after searching the entire structure), return false. 
    - use a foor loop for that. 
    - linear search: slow. 
        - Best case: first item. 
        - Worst case: Not in the array. 
        - Occurs behind the scenes.
        - Check every element.  
- *Sort Arrays*: 
    - Numbers: Ascending, Decending orders. 
    - Strings: Alphapitical order. 
    - Call sorting function. 
    - Pass it to a sorting functions. 
    - Expensive: because you have to do lots of computations. 
- *Big O notation*:
    - used to describe the performance or complexity of an algorithm. 
    - Operations:
        - Access. 
        - Update.
        - Insert.
        - Search.
        - Delete.
        - Sort.
    - O(1) Time: 
        - Consistent duration of algorithm execution in same time (or space) regadless of the size of the input. 
        - Also called constant time. 
        - Same amount of computational time. 
        like updating arrays. 
    - **Insertion**:
        - Best case: large enough array: O(1) => constant time.
        - Worst case: 
        Array is full: O(n) => linear time.
    - **Search**:
        - Best case: Compare two item: O(1) => constant time.
        - Worst case: Item does not exist: O(n) => linear time. 
    - **Deletion**:
        - Best case: Locate and delete item: O(1) => constant time.
        - Worst case: Search, then locate, then delete item: O(n) => linear time. 
    - **Sorting**:
        - Insertion sort.
        - Merge sort.
        - Heap sort.
        - Bubble sort.
        - Radix sort. 
### Lists:
- Linked lists = Linear data structure.
- Node: contains data and a pointer to next level. 
- We can access every next item through a pointer. 
- Accessing an item in a list doesn't need an index like arrays, use pointers. 
- Foundations of linked-lists data structures are the operations: Add, Search, Delete, Access. 
- Singly vs. doubly linked lists.
- java list is not a data type=> java.util package. 
    - Array lists. 
    - LinkedLists. => doubly linked. 
    - Array Lists:
        - Has a behavior of a list on the surface. 
        - Stored as an array under the hood. 
- C# => Systems.Collections
    - LinkedLists.
- Swift, Ruby and JS no Build-in Linkedlists. 
- In python => Lists are resizable arrays and no built-in linked lists implementation. 
- C++ => has list container in the standard template library. 
- Big O Notation:
    - Access: linear time in worst case O(n) 
    - Update: O(n).
    - Insert: O(1).
    - Search: O(n).
    - Delete: O(n).
    - Sorting: depends on the algorithms. 
### Stacks:
- LIFO: Last in First Out. 
- FIFO: First in First Out.
- Stack: LIFO.
- Push: O(1).
- Pop: O(1).
- Runtime stack keeps track of variables so as to track errors. 
- pop to empty stack will cause error because there is no items already.
- Use stack when:
    - Reverse things.
    - Keep track of state.
    - Add/remove from back of structure.
### Queues:
- Queue: FIFO
- Enqueue: add item to queue.
- Dequeue: remove item from queue. 
- Store order of thigs to happen. 
- Use tools from the language. 
- C#:
    - Queue class: Enqueue and dequeue.
- Python:
    - use put(), get().
- Ruby and JS:
    - Dynamic arrays
- C++:
    - push_back() and pop_front. 
- Priority queue:
    - java has a proirity class.
    - C++ has a proirity container.
- Double-ended queue. 
- java has interface for deck. 
- C++ has a container. 
- Python has a class. 
- No option in Ruby or .NET, use linked lists or dynamic arrays as alternatives. 
### Associative arrays:
- key -> Value.
- Collection of key- value pairs. 
- Associated array rules:
    - key-vlaue pairs are bound together.
    - each key mush be unique.
    - order is not important.
    - values are accessed with the key.
    - values do not need to be unique.
- Dictionaries, maps, hashes.
- *Hash Functions*:
    - Hashing:data conversion process.
    - Hash inputs: characters, numbers, objects. 
    - Hash output: integer.
    - Not reversibal: cannot get the same data back. 
    - How hashing works:
        - Numberical representation in ASCII value. 
        - Complicated.
        - Collision: two inputs produce the same value for outputs. 
        - you cannot unhash the hashed value. 
    - Hash tables:
        - put, add, insert to add key-value to the hash function. 
        - separate chaining to resolvve collision. 
- Python = Dictionaries.  
- Java = any class have a hash code fucntion.
- Swift = hash value property.
- .Net = GetHash Code funcion.
- Ruby = GetHash Code function.
- JavaScript = Implement custom code.
- JS with Node.js = npm install appropriate module.
- Java = hash table and hash collections. 
- Searching is much faster. 
- Hash Map Operations:
    - Search: O(1).
    - Insertion: O(1).
    - Deletion: O(1).
    - Differ if there are collisions. 
    - No sorting. 
### Trees and Graphs:
> **Sets**:
- Check if an object is in a set (membership). 
- Implemenation:
    - Array(linear search).
    - Linked list(traverse).
    - Associative array (specific key).
- Sets take an object, hash it, store it using index. 
- Sets are unlimited. 
> **Trees**:
- Root node contains data and a link to next nods. 
- Parent nodes. 
- Child nodes.
- Leaf node: node with no childern. 
- Siblings: Children of the same parent node. 
- Node can have many children or one or none.
- Balanced tree: O(log(n)).
- Unbalanced tree: O(n).
- Requires some overhead and maintenance. 
> **Binary Search Trees**:
- left node and right node. 
- it must be ordered. 
- Left child node < than its parent. 
- Right child node > than its parent. 
- To retrieve the nodes: compare. 
- C++: sets are implemented with BSTs.
- C#, .NET: sorted dictionaries are implemented with BSTs.
- Java: TreeMap implemented with a red-black tree.
- JavaScript, Ruby, Python: third-party implementaion available. 
> **Heap**:
- It is a binary tree.
- Collections of objects.
- Care about the min or max value: depends on data. 
- Not a fully sorted data structure. 
- Priority Queue:
    - Order doesn't matter. 
    - Heaps used to implement priority queues.
- Find min/max: O(1).
- Insert: O(log(n)). 
- Search, Delete: O(n).

**Choosing a data structure depends on What you want to store, how you want to store it and how you want to access it**



    























