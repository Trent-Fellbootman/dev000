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

!!! Note "Memory Use Cases as Abstractions"

    If you recall the definition of abstraction from the previous module,
    you'll find that memory use cases are abstractions as well:
    a memory use case defines what something (the memory) is
    (something you can use for a certain use case during a certain period of time)
    to someone (the programmer), disregarding all the irrelevant details.

Although it seems like an obvious idea,
memory use cases alone helps to solve a lot of problems in memory management,
as it clearly states what "should" and "shouldn't" be done to a memory address.

Before defining the use case of a piece of memory,
programmers would stare at a piece of memory and just don't know what to do with it:
*Can I write data to it? What is the value stored here?
Is it just some random bytes I can overwrite, or meaningful contents I should keep?
Will any instruction later make use of this piece of memory?
If I want to store some long-lasting thing here, will it get overwritten at some point?*
As a program gets larger, it becomes harder and harder to answer these questions,
as that requires looking at every instruction in the program and see what it does with the memory.

Memory use cases makes it much easier.
After knowing the use case of a piece of memory,
developers can have some assumptions about the valid ways to use it and what would happen if it's used in certain ways.
For example, the developer may think:
"*Okay, at this point, this piece of memory does not hold anything important,
so I can write whatever I want to it.
However, after operation A finishes,
operation B would use this memory to store it's records,
and anything I write here will be overwritten,
so I gotta make sure that I don't read this piece of memory after operation B starts.*"

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

!!! Info "The term "deallocate" is sometimes used synonymously with "free", or "destroy"."

## Stack & Heap

Building on the concept of memory use cases,
**stack** and **heap** are two special pieces of memory that creates a more well-defined model for memory management.
Stack and heap are not for specific memory use cases (such as storing someone's birthday);
rather, they are "pools" from which memory can be allocated in a well-defined way.

You can think of the stack and heap as both being existent for the whole lifetime of a program.

!!! note "Stack & Heap as Data Structures"

    Stack and heap are also names for data structures.
    While they share some similarities with the memory objects introduced here,
    they are not the same things.

    For clarification between the "stack memory object" and the "stack data structure",
    the former is usually referred to as "stack memory", while the latter just "stack".
    Similarly, the "heap memory object" and the "heap data structure" are usually referred to as "heap memory" and just "heap".

### Stack

In terms of memory use cases,
the stack is a special, typically smaller piece of memory which is used to store (roughly)
"things that are small and need to be quickly accessed".

Stack is Last-In-First-Out **(LIFO) ordered**,
meaning that when you allocate memory from it,
the newly allocated memory is on top of (i.e., its address always precede or follows)
the last piece of previously allocated memory.
Similarly, when you deallocate memory from it,
the top most piece of memory is deallocated first.

![stack](res/stack.png)

Why is stack good for "things that are small and need to be quickly accessed"?

Since the stack is usually small,
it can only store small things.
On the other hand, stack is good for things that need to be quickly accessed because it's ordered:
as long as you know the sizes of the things after the thing you want to access,
and the memory address of the top of the stack (i.e., the address of the last thing on the stack),
you can easily compute the memory address of the thing you want to access and access it.
In compiled languages such as C++,
such memory address calculations are typically done statically at compile time,
which means when the program is run,
you get the address of anything you want to access on the stack with
(almost) no calculations at all
(for now, you don't need to understand how this works;
just keep in mind that accessing things on the stack is easy and fast).

!!! info "Fun Fact"

    Stack is small and its size is often fixed during a program's lifetime;
    when you try to use more memory than the stack can provide,
    you trigger an exception called "**stack overflow**",
    which happens to be the name of a [platform](https://stackoverflow.com/)
    on which developers talk about program errors and their fixes.

### Heap

In terms of memory use cases,
the heap is a special, typically larger piece of memory which is used to store (roughly)
"large, long-lasting things".
Heap is typically much larger than the stack.

Heap is **unordered**, which makes it harder both to allocate and access memory compared to stack.
In stack, memory is always allocated on the top;
in heap, however, you would have to first find a free piece of memory, then allocate it;
when you want to access something,
you must know its memory address, or you will have a very hard time finding it on the heap.

![heap](res/heap.png)

In computer programs,
a typical combination is to store something really large on the heap,
but keep its memory address on the stack.
This way, you can store large things (like databases, cuz the heap is large)
but also access them relatively quickly (cuz the stack is fast).

## Conclusion

In this section,
we talked about the basic models for memory management,
which are memory use cases, stack and heap.

The key takeaways:

- **Memory use cases** defines what a piece of memory is for at each point in time.
- The **stack** is a small, ordered piece of memory which is fast and easy to access and allocate memory from.
- The **heap** is a unordered piece of memory. Compared to stack, it is slower to allocate memory from the heap,
but the heap is much larger than the stack.

## AI Prompt Samples

If you're interested in the topics of this section,
feel free to consult and AI such as ChatGPT for more information.

Some sample prompts to get you started:

- Please explain the difference between stack and heap memory.
