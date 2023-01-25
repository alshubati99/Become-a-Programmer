# Programming Foundations: Real-World Examples
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/7d31e20bfb2049a67cbfed49443aeecab24bf12d60543bae7f529e5eddf81346)
### Why to create functions?
- To handle repeatitive tasks. 
- Compine more steps into one function
- Reuse code: using the same code elements more than once. 
- If using same steps. 
- Functions may or may not return value. 
### Functionalizing Code:
- Reuse code for similar tasks.
- Change code in one place. 
### Parameters:
- Variables names used inside of the function to access input passed to the function. 
### Arguments:
- The value passed to the function: omelette('Cheese')
- **Prameter != Argument**
- Input Parameteres:
    - Must be uniquely named. 
    - Must pass exact number defined
### Local Variables:
- Parameteres
- Variable created inside of a funcion. 
- In python, Local  variable is checked before global variable. 
### OOP:
- Object: nouns(that, this) people, things, places. 
- Attributes: adjectives to descripe the object. 
- Methods: Actions performed on the object. 
- Class: Blueprint to define objects. 
- List = mutable data type. 
- String = immutable data type. 
### Inheritance:
- When a class inherits from another class its features. 
- Keep large programs simple. 
- Easy to maintain code. 
### Modules:
- From statement:
    - Helpful when using one or two tools in a module
    - Easy to create name confilicts. 
- You can import module and name it using (as)
- Packages contain a collection of modules => urllib package. 
### Lists:
- Group of objects listed. 
- Lists are mutable unlike tuples which are immutable. 
### Queues and Stacks:
- Queues: FIFO => first in first out. 
- Stack: LIFO => last in first out.
- Queue acts as a buffer in some situation. 
- Not build in data types.  
- It is easy to add and remove items from end since it is LIFO. 
### Sets Data structures:
- Unordered collection of unique items. 
- Different from lists because no ordering or indexing in sets. 
- union() operator=> to merge 2 sets. 
- Store group of like objects.
- difference() remove the common items in two sets. 
### Dictionaries:
- Index = Value
- Uses hash funcions to return indexes. 
- can be called: hashes, maps, collections according to the programming language used. 
- Don't allow duplicate keys.
### Conditional Statements:
- Cases that come first have higher priority.
- In python there is no switch structure like other languages, but it can use dictionaries instead. 
- Since a dictionary uses hashing it is often better to use than long if/elif chain. 
### Loops:
- In while loop, you don't know exactly how many times the loop is going to run unlike (for) which is certain to know the exact times to run the loop. 
- Problems often occur when adding or removing items from a list with a for loop. 
### Error Catching:
- Set conditions.
- Validate data against conditions
- implement Error Checking:
    - Input from a user or external method.
    - Methods with logic that relias on conditions being true.
- Types of Errors:
    - Errors built into language. 
    - Modules and packages often include related errors.
    - Programmer can  create custom errors with new class definitions.
- Error Handling:
    - Important for creating robust code.
    - Often overlooked.
    - Can be trickier than syntax issues.
- Error handling allows code to excute properly when unexpected events occur. 
- Sticky Situations:
    - Missing an error.
    - Finding an error, without knowing the cause. 
### Polling:
- Program actively checking for performance.
- Not efficient. 
- open loop, uses much cpu resourses. 
- add a timer to make the program sleep for some seconds so as not to overwhelm the cpu resources. 
### Event Driven Programming:
- Handle one event at a time in order of when event occurs.  
- tkinter:
    - Python module for creating graphical user interface. 
    - Easy way to demo event-driven programming. 
- Event handlers => code that is executed when an event occurs. 






