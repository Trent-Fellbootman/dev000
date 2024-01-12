# Variables

Variables is probably the most broadly-applicable concept in programming languages.
In fact, every programming language I've seen employs the concept of variables (except for DSLs).

So what is a variable?
Simply speaking, a "variable" is "a thing that exists".
In programming languages,
**variables comprise the state of a program**.
Variables can be anything, from a simple integer or a string,
to a file on disk or a network socket.
From the perspective of ISA though,
a variable is typically an abstraction over a piece of memory.

??? code-lab "Code lab: Variable Basics"

    Let's create some basic variables in Python and in C++!

    Enter the following contents in a Python script:

    ```Python
    a = 5
    b = "Koalas are so cute!"
    c = {
        "a": 1,
        "b": [
            1, {3, 5, 7}
        ]
    }

    print(a, b, c, sep='\n')
    ```

    Run the script and observe the output.
    If you don't have Python yet or you don't know how to run Python scripts, ask an AI.
    (Hint: Consider using an environment manager such as Anaconda to avoid messing up your operating system.)

    In this above code, `a`, `b` and `c` are variables,
    and the last `print` statement prints their contents to the console.

    Now, let's see how variables work in C++.

    Enter the following content in a C++ source file:

    ```C++
    #include <iostream>
    #include <string>

    int main() {
        int a = 5;
        std::string b = "Koalas are so cute!";
        std::cout << a << "\n" << b << std::endl;
        return 0;
    }
    ```

    Compile the file and run the executable.
    Again, if you don't know how to do this, ask an AI.

    Compare the Python code and C/C++ code.
    Can you see the difference between the ways Python/C++ handles variable creation?
    Why is there such a difference?
    (Hint: Python is an interpreted language and C++ is a compiled language.
    This question is a bit hard if you're just getting started with coding.
    If you can't figure out the answer, ask an AI about this question and see how he/she/it answers it.)

## Variable Types

One common concept associated with a variable is its **type**.
The type of a variable answers the following questions:

- What kind of thing is this variable?
- What can I do with it?

Essentially, types give meanings to variables.
Without a known type, a variable is just a meaningless piece of memory;
you stare at it and don't know what you can do with it.
You can also think of types as abstractions for variables.
Even though variables are just pieces of memory under the hood,
few developer actually think in that way:
obviously, it is much easier to think in terms of integers, strings and files,
instead of a piece of memory containing binary value 0xffee37.

At the same time, it is important to note that types (and also variables)
are just abstractions, not physical objects.
When you use C++ to code an application,
there are no types and variables in the compiled application,
only memory operations and ISA-defined binary machine code.

## Basic Variable Syntax

The exact variable syntax defined in different programming languages can differ,
but there are many commonalities,
as explained in this subsection.

### Variable Assignment

Almost all languages use a single equal sign "=" for assigning values to variables.

Assigning a new value to a variable changes its content to that value;
From the perspective of ISA, assigning a value to a variable is equivalent to writing the piece of memory corresponding to the variable.

The following table shows how to assign the value `5` to an integer type variable named `a` in a few languages:

| Python | C/C++ | Rust | Java | C# |
|-|-|-|-|-|
| `a = 5` | `a = 5;` | `a = 5;` | `a = 5;` | `a = 5;` |

### Variable Declaration

Compiled languages typically require you to **declare** a variable before you assign a value to it or read it.
The **declaration** of a variable is basically a placeholder that "declares that this variable exists".

For example, in C/C++ you use "int a;" to declare an `int` (i.e., integer type) variable named `a`;
in Rust, you do the same thing with `let a = 5;`.

Since it would be too lengthy to write declaration first, then assign value, most compiled languages allow you to combine declaring and assigning an initial value to a variable.

The following table shows how to declare an `int` variable and assign it to `5`
in a few languages:

| C/C++ | Rust | Java | C# |
|-|-|-|-|
| `int a = 5;` | `let a = 5;` | `int a = 5;` | `int a = 5;` |

!!! info "Type Inference & Type Annotation"

    Notice that Rust does not require you to annotate explicitly that you're declaring an integer variable,
    even though it is a compiled, statically typed language.
    This is because the Rust compiler can infer the type of the variable
    by looking at the initial value you assign to it (`5` in this case).

    The ability of the compiler to infer variable types is called **type inference**.
    Type inference is supported in many programming languages,
    and can be very useful when the type name is long,
    or that you don't know the exact type of a variable.

    Type inference shows that "not having to annotate the type is not equal to dynamic typing".

    On the contrary, annotating types is not equal to static typing, either.
    For example, Python allows but does not require you to annotate the type of variables,
    and it is generally a good practice to annotate variable types in code that interfaces with users (such as library function signatures).

!!! question "Question: Variable Declarations"

    Why do compiled languages require declarations,
    while interpreted languages do not?

    *Hint: Think about static & dynamic typing,
    as well as how compiled/interpreted languages gets run.
    If you still can't figure it out, ask an AI.*

### Primitive Types

Almost every programming language have a set of predefined primitive types.
These types are typically atomic,
small (in terms of memory usage of the variables of these types),
and cannot be decomposed into smaller parts.

The following table lists some of the primitive types that almost all programming languages support
(an "Identifier" of a variable type is the name of that type in a certain language).

| Type | Identifier (Python) | Identifier (C++) | Identifier (Rust) |
|-|-|-|-|
| Integer | `int` | `int` (basic), `unsigned int`, `int32_t`, `long`, `long long`, `size_t` (other flavors) | `usize`, `i32`, `u32`, `i64`, `u64` |
| Decimal Numbers | `float` | `float`, `double` | `f32`, `f64` |
| Boolean | `bool` | `bool` | `bool` |
| Character | N/A | `char` | `char` |
| Pointer | N/A | `<type>*`, like `int*`, `float*`, `void*` | `&<type>`, like `&i32`, `&f32`, `&bool` |

!!! question "Questions"
    There are some interesting questions you can ask by observing the above table:

    - What does `u` and `i` mean in the above Rust type identifiers?
    - What does the numbers `32`, `64`, etc. in the above type identifiers?
    - Is it better to use `int` or `int32_t`?
    - Why are decimal numbers called `float` instead of `decimal`?
    - What is the semantic of a "boolean"?
    - What is the semantic of a "pointer"? Why does Python not have pointer?
    - Why does C++ and Rust have so many different types for integers / decimals?

    Can you answer these questions?
    (Feel free to ask an AI if you can't figure out the answer;
    some questions are a bit hard for beginners.)

??? code-lab "Code lab: Type Conversion"

    The following C++ code assigns a decimal number to an integer variable,
    and displays the value of the integer variable:

    ```C++
    #include <iostream>

    int main() {
        int a = 5.6;
        std::cout << a << std::endl;
        return 0;
    }
    ```

    Compile and run the code.
    What do you observe? Why does this happen?

    Now, let's try to do the same thing in Rust:

    ```Rust
    fn main() {
        let a: i32 = 5.6; // annotate i32 explicitly to avoid the compiler from inferring it as f64
        println!("{}", a);
    }
    ```

    Try to compile the code.
    What do you observe?

    Judging from the behavior of the C++ v.s. Rust compilers,
    do you think the design of C++ is better than that of Rust,
    or the other way around?
    Why?
    
    (*Hint: Search for "silent bugs"*.)

??? code-lab "Code Lab: Do Types & Variable Names Exist?"

    Here's a simple C++ code:

    ```C++
    int main() {
        int koalas_are_so_cute = 5;
        return 0;
    }
    ```

    Compile this code to assembly (ASM),
    making sure to turn off optimization options
    (again, ask an AI if you don't know how to do that).

    You will likely get something like this:

    ```asm
    	.file	"test.cpp"
        .text
        .globl	main
        .type	main, @function
    main:
    .LFB0:
        .cfi_startproc
        endbr64
        pushq	%rbp
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        movq	%rsp, %rbp
        .cfi_def_cfa_register 6
        movl	$5, -4(%rbp)
        movl	$0, %eax
        popq	%rbp
        .cfi_def_cfa 7, 8
        ret
        .cfi_endproc
    .LFE0:
        .size	main, .-main
        .ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
        .section	.note.GNU-stack,"",@progbits
        .section	.note.gnu.property,"a"
        .align 8
        .long	1f - 0f
        .long	4f - 1f
        .long	5
    0:
        .string	"GNU"
    1:
        .align 8
        .long	0xc0000002
        .long	3f - 2f
    2:
        .long	0x3
    3:
        .align 8
    4:
    ```

    Do you see the name of the variable or `int` in the above compiled ASM?
    Can you identify where the variable `koalas_are_so_cute` is in the above ASM?
    Based on this observation,
    do variable names or types exist in compiled executables?
    Why is this?

    *Hint: These questions are very hard for beginners.
    You should provide the C++ source code and the ASM to an AI and ask him/her/it to explain what each line of the ASM does.*

??? code-lab "Code Lab: Large Numbers"

    Try to write some code to find out the largest possible number that an integer can represent in C++.
    Do the same for Rust and Python.
    (Use `int` in C++, `i32` in Rust and `int` in Python.)

    Observe the program outputs and do some search on the internet.
    Can you explain how Python represents integers in a way different from C++ or Rust?

### Composed Types

Most programming languages allow you to define your own **composed types**.

A composed type is a type composed of **fields** of other types.
For example, the following Rust code defines a `Student` type (composed type)
with a decimal number field named `score` and a string field named `name`:

```Rust
struct Student {
    score: f32,
    name: String
}
```

Notice that fields can be composed types as well.

You can define equivalent `Student` type in C++ via:

```C++
struct Student {
    float score;
    std::string name;
};
```

In Python:

```Python
@dataclass
class Student:
    score: float
    name: str
```

!!! info "Typical Identifiers for Composed Types"

    Programming languages have virtually the same syntax for defining composed types;
    a composed type is usually called a `struct` or a `class`, depending on the specific language.
    So, if you're getting started with a language and want to know the syntax for composed types,
    try searching for `struct` or `class`.
    For example, you can ask an AI "How to define a struct in Go?"

!!! code-lab "Code lab: Composed Types"

    Try to define your own composed type in Rust.
    Then, ask an AI to help you create a variable of this type and display it properly to the console.

### Enum

Almost every programming language supports defining **enum types**.
An **enum**, which is short for **enumeration**, is a type that can take on one of a finite number of values; each of these values is called an **enum variant**.

For example, the following C++ code defines an `enum` type named `Color` that can be either `RED`, `GREEN`, or `BLUE`:

```C++
enum Color {
    RED,
    GREEN,
    BLUE
};
```

Then, you can declare a `Color` variable named `a` and assign it to `RED`:

```C++
Color a = RED;
```

!!! info "Extended Enums"

    The enum feature of some programming languages is more powerful than simply defining a finite set of enum variant values.

    For example, Rust allows you to associate different fields with different enum variants, like:

    ```Rust
    enum Person {
        Student(f32), // `f32` field represents the score
        Teacher(String), // `String` field represents the name
        Soldier // no field
    }
    ```



## Common Concepts & Design Choices Related to Variables

### Static v.s. Dynamic Typing

One common design choice associated with variables is whether to use static or dynamic typing.

Static typing means that the type of a variable cannot change during its lifetime;
dynamic typing, on the other hand, allows you to change the type of a variable at run-time.

Typically (but not always), compiled languages use static typing,
while interpreted languages use dynamic typing.

!!! question "Question: Static vs. Dynamic Typing"

    Why do compiled languages typically use static typing,
    while interpreted languages use dynamic typing?

    *Hint: Think about what happens when the program is run.
    This question can be a bit hard for beginners;
    you can ask an AI for help.*

### Stack & Heap Variables

In lower-level languages, especially those without garbage collectors
(such as C++ and Rust),
it is important to distinguish between stack and heap variables.

As their names suggest,
the memory corresponding to a stack variable is allocated on the stack,
while the memory corresponding to a heap variable is allocated on the heap
(but heap variables may also have pointers or metadata stored on the stack).

Typically, stack variables are small and their lifetimes are short;
while heap variables are large and their lifetimes are longer.

!!! question "Question: Stack v.s. Heap Variables"
    With the help from AI and the internet,
    try to answer the following questions:

    - Why do stack variables have shorter lifetimes?
    - Is it faster to access a stack or a heap variable? Why?
    - When should you use stack variables? What about heap variables?
    - Do you distinguish between stack & heap variables in Python? Why?

### Variable Mutability & Default Mutability

**Mutability** is another important concept associated with variables.
Typically, **variables** can be either **mutable** or **immutable**.

If a variable is mutable, that means you can assign another value to it
after you have assigned an initial value.
If it is immutable, you can't assign it another value
once it's set to an initial value.

Many programming languages have the concept of mutability
and allow you to mark a variable as either mutable or immutable.

However, there is less consensus when it comes to whether a variable
should be mutable or immutable by default
(i.e., when the user does not specify mutability).
For example, variables are mutable by default in C/C++,
but immutable in Rust.

!!! question "Question: Default Mutability"

    Is it a better design choice to make variables mutable or immutable by default?
    Why does C/C++ make variables mutable by default, while Rust makes them immutable?

    *Hint: Answering these questions does require some experience with coding,
    so if you're a beginner, feel free to ask an AI.*

### Lifetimes

The **lifetime** of a variable is the scope in which
a variable is valid and existent.

The concept of lifetimes applies to almost every programming languages,
but few languages have special syntax for annotating lifetimes explicitly.
One such language is Rust.

!!! question "Question: Lifetimes"

    Why is it helpful to know the lifetime of a variable?

??? code-lab "Code Lab: Lifetimes in Action"

    Look at the following Rust code:

    ```Rust
    fn main() {
        let a = 5;

        {
            let b = 1;
        }

        println!("{}, {}", a, b);
    }
    ```

    What is the lifetime of `a`?
    What about `b`?

    Feel free to ask an AI for help.

### Ownership

**Ownership** is both an important concept and a model for resource management.
Basically, the ownership system specifies one or more **owner variables** for a piece of resource;
When all the owners are gone, the resource is freed.

Ownership is a bit out of scope for the purpose of this beginner's section,
so I won't go into the details here.
If you're interested, try searching for "Rust ownership", "RAII" and special "smart pointers" in C++ such as `std::unique_ptr` and `std::shared_ptr`.

## Conclusion

Phew, that was a lot of material!
Now that you've gone through all the materials,
questions and code labs,
you should have a basic understanding of variables
as well as how to use them in writing code.
More importantly,
you have learned how to consult AI and the internet
to find the things you need!

We covered a lot of things in this section:

- Variables represent "things".
- Variables have **types**.
- Common syntax associated with variables:
variable **assignment**, variable **declarations**,
**primitive** and composed types,
**enum** types.
- Common concepts and design choices associated with variables:
**static** and **dynamic** typing,
**stack** and **heap** variables,
variable **mutability**, lifetime, ownership.
