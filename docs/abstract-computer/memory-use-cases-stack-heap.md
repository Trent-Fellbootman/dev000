# Memory Use Cases, Stack and Heap: Basic Memory Management

In the previous section,
we learned that in the abstraction of ISAs,
the "state" of a program is completely represented by the registers and the memory
(this is not entirely true, but you don't need to worry about that for now).
That is, their contents completely determines the behavior of a program.
And, since the memory is much, much larger than the registers,
it is the primary storage where a program stores its state.

However, ISAs didn't provide any guidance to how that memory should be used.
Although this adds flexibility, it adds complexity as well.
Typically, programs would need to know which memory address stores what value;
if it assumes that a certain address stores a certain value,
but that address was actually overwritten by a previous instructions,
it will not work as expected.

As software applications gets larger and larger,
it becomes harder and harder to track which address stores what value manually,
and to make sure that memory reading and writing works properly.
This is called the problem of memory management.

To address this problem systematically,
people have proposed many different models of "how to use memory",
such as ownership, automatic garbage collection, RAII (Resource Allocation Is Initialization), etc.
We won't describe all of them here,
but we will describe the shared concepts that almost all of them use or build upon.
These concepts are memory use cases, stack and heap.

It is important to note that these concepts are often abstracted away and don't show up explicitly in higher level languages,
especially those with garbage collectors such as Python.
However, understanding these concepts provides a good foundation of understanding how a program gets run at a low-level
(same with ISAs).

## Memory Use Cases

**Memory use cases** helps to answer the question: for a certain piece of memory
(i.e., spots in memory corresponding to a set of memory addresses),
at a certain period of time,
what are the ways that it should be used?
I.e., **what is this piece of memory for, at each point in time**?

Although it seems like an obvious idea,
memory use cases alone helps to solve a lot of problems in memory management,
as it clearly states what "should" and "shouldn't" be done to a memory address.

Before defining the use case of a piece of memory,
programmers would stare at a piece of memory and just don't know what to do with it:
can I write data to it? What is the value stored here?
Is it just some random bytes I can overwrite, or meaningful contents I should keep?
Will any instruction later make use of this piece of memory?
If I want to store some long-lasting thing here, will it get overwritten at some point?
As a program gets larger, it becomes harder and harder to answer these questions,
as that requires looking at every instruction in the program and see what it does with the memory.

Memory use cases makes it much easier.
After knowing the use case of a piece of memory,
developers can have some assumptions about the valid ways to use it and what would happen if it's used in certain ways.
For example, the developer may think:
"Okay, at this point, this piece of memory does not hold anything important,
so I can write whatever I want to it.
However, after operation A finishes,
operation B would use this memory to store it's records,
and anything I write here will be overwritten,
so I gotta make sure that I don't read this piece of memory after operation B starts."

### Some Terms Associated With Memory Use Cases

Below describes some terms associated with memory use cases,
which you're likely to encounter in the developer's world.

#### Allocate

To "allocate" a piece of memory means to find a piece of "free" memory
(i.e., a piece of memory that nobody is using)
and purpose it for some use cases.
After a piece of memory is allocated for some use case,
it is considered not okay to use it for anything else.

For example, in computer programs, it is common to allocate memory to store data, such as someone's birthday.

#### Deallocate

To "deallocate" a piece of memory means to mark the end of the current use case (whatever it is) associated with it.
After a piece of memory is deallocated, it is considered okay to be repurposed for any other use case,
and not okay to use it for the previous use case.

For example, if a piece of memory is currently storing someone's birthday and it's deallocated,
it is then okay to use it to store the result of $153 \times 13251$, etc.

The term "deallocate" is sometimes used synonymously with "free", or "destroy".
