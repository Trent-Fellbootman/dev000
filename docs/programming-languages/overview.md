# Programming Languages: A High Level Overview

In this section, we are going to talk about
the purpose of programming languages and their general taxonomy.

## What are programming languages? Why do we need them?

Generally speaking,
a programming language is
**an abstraction of computers, designed to
make designing, representing, building and understanding computer programs easier for beings with a human-like mindset**.

Notice that programming languages are sometimes defined in a more liberal way, counting in assembly languages as well;
in this module, however, we define "programming language" to include only modern, "human-oriented" programming languages
such as C/C++, Python, Rust, Java, JavaScript, etc.;
we do not include languages that are not meant for use by humans (except in very few special cases),
such as assembly languages and binary machine codes.

Recall from the previous module that the lowest level
(closest to hardware) abstraction of a computer is and Instruction Set Architecture (ISA),
but programming with ISAs is very unintuitive for humans.
As a result, people decided to build higher-level abstractions that are easier to understand for humans;
this is exactly what programming languages are for.

Since programming languages are high-level abstractions designed to be human-friendly,
their programming models are typically far away from the actual computer hardware (compared to ISAs).
For example, registers, a hardware detail found in almost every ISA, is abstracted away in almost every programming language.

!!! info "About registers"

    In modern CPUs, registers defined in ISAs are typically not actual hardware components,
    but they are not just abstractions either.

    There are "physical registers" in CPUs.
    However, they do not map to ISA-defined "architectural registers" directly.
    Instead, the typical case is that there are many more physical registers than architectural registers;
    the latter are mapped to the former in a many-to-many way at run-time via a technique called "register renaming".

Here are some commonly found concepts in programming languages,
compared with their "lower-level implementations" in ISAs (which are still abstractions over hardware):

| Programming Language Concept | ISA Implementation | Description |
| -------------------------- | ----------------- | ----------- |
| variable/constant | a chunk of memory which holds data | A "thing", like the string "Hello, World!", number 1.22, or a tree of data |
| function | typically a chunk of memory which holds ISA instructions (in compiled languages) | A tool which can do a certain thing |
| struct | not present at run-time (in compiled languages) | a definition for structured data, like "a student struct has name, age, and scores" |

## The General Taxonomy of Programming Languages

There are a large number of programming languages at present;
each of them has its own features, abstractions, tradeoffs and is fit for a specific set of use cases;
however, there are some commonalities between them,
and programming languages can be generally divided into large groups from multiple perspectives.

In this subsection, we will talk about some of the common ways to categorize programming languages,
and the general characteristics of languages in each category.

!!! info "The term "tradeoff""

    "Tradeoff" is a basic concept in both software and hardware development.
    Generally speaking, it means **to "trade" (sacrifice) the quality in one aspect for that of another**.

    For example, many programming languages (like Python) sacrifice speed and hardware efficiency for ease of use;
    others like C/C++, on the other hand, sacrifice ease of use and learning for better control over hardware and faster execution.

### Execution Model: Compiled v.s. Interpreted

One common way to categorize programming languages is by the execution model,
which can be either "compiled", "interpreted" or a hybrid between the two.

#### Compiled Languages

Recall from the previous section that
the run-time (i.e., the time when a program is run)
execution of virtually every computer programs boils down to
executing ISA-defined instructions on the hardware.

However, programming languages are designed for humans, not computer hardware;
so there has to be some way to convert software written in a programming language into machine-executable code,
either before or when the program is run.

**Compiled languages** choose the former.
In a compiled language, code that a developer writes (to form a full program or part of a program) in a programming language
is converted into machine-executable code by a piece of software called the **"compiler"**,
before the program is run.
Then, that software application in machine code form can run on hardware directly.

There are some terms associated with compiled languages:

- **Source code**: Code that a developer writes in a programming language.
- **Machine code**: Code that can run on hardware directly.
- **Compilation**: The process of converting source code into machine code.
- **Compiled application**: A piece of software that has been compiled (from source code), typically in machine-code form.
- **Compile**: The verb form of "compilation".
- **Compiler**: A piece of software that does compilation.
- **Compile-time**: The time when the compilation is performed.
- **Run-time**: The time when the program is run.

!!! info "Decompilation"

    You might wonder whether it is possible to convert machine code back to source code.
    Yes, that is indeed possible.
    Such a process is called **decompilation**,
    and there are a lot of **decompilers** out there which do decompilation.

The advantages of compiled languages are:

- Fast and hardware-efficient:
The biggest advantage of compiled languages is that they are fast and hardware-efficient.
The process of compilation makes sure that
**every instruction in the compiled application does useful job in the most efficient way possible**.
Many people would awe at the the wide range of optimizations that modern compilers can do,
from identifying and eliminating useless code in the source code,
to "rewriting" source code in a way that works better with the hardware.
Additionally, since compiled applications interface with the hardware directly
without introducing an intermediate layer (as in the case of interpreted languages),
they run much faster and use much less memory.
- (Sometimes) better bug-extermination:
In many cases (such as with variable types, as we'll introduce later),
the static nature of compiled languages means that many errors in the source code
can be detected at compile time, rather than resulting in glitches that users experience at run time.

The disadvantages:

- (Typically) harder to learn and use:
Since compiled languages are typically closer to hardware,
it takes more efforts to learn them.
It is usually harder to use them as well,
as being close to hardware means that you have to manage many things (especially memory) yourself,
instead of delegating that responsibility to a piece of software (as with most interpreted languages).
In addition, it often takes more code to write the same application in a compiled language than in an interpreted one.
- Less flexibility:
The static nature of compiled languages means it is harder to do certain things with it,
such as modifying the type of a variable at run-time.

Some popular compiled languages:

- C/C++: Although created many, many years ago, C/C++ is still one of the most popular compiled languages in the world.
It offers the most control over hardware and unrivaled performance (if used in the right way).
However, it has a steeper learning curve,
and memory management is notoriously hard
(can be relieved by using stuff like smart pointers and RAII though).
- Rust: A modern, relatively new programming language.
It is one of the most difficult-to-learn languages in the world,
but once you get familiar with it, you will benefit a lot from its memory safety guarantees,
as well as its modern syntax and design which makes it very intuitive and concise.
