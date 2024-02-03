# Values, Operators and Expressions

Values and expressions are abstractions common to all programming languages.
Roughly speaking, values represent data,
while expressions represent some data you get by transforming some other data.

## What are values and expressions?

### What is a value?

Basically, a **value** is a "thing".
It could be a "simple thing" like a number or a string,
or a complex thing like a user-defined struct/class object (recall from the previous lecture).

The following are all examples of values:

- `42`
- `"hello"`
- `true`
- `[1, 2, "cute"]` (Python list)
- `{a: 1, b: 2}` (Python dictionary)
- `Student {name: "John", age: 20}` (Rust struct literal)

You might wonder, "variables are things, and values are also things, so what is the difference between variables and values?"
Well, simply speaking, variables represents **states** that can live and change for a period of time,
while values represent stateless **data**.
In compiled languages, values may not have memory allocated to them at all.
In other words, the concept of values only exist for human programmers,
and are often optimized away (i.e., eliminated) by the compiler.

Consider the following C++ code snippet:

```cpp
int x = 42, y = 35, z;
z = (x + y) * (x - y) + (3 * x) + (5 * y);
```

In this code snippet, `x, y, z` are all variables,
while `42, 35, 3, 5`, as well as that long thing `(x + y) * (x - y) + (3 * x) + (5 * y)` getting assigned to `z`,
are all values.

Notice that in the long expression `(x + y) * (x - y) + (3 * x) + (5 * y)`,
`x` and `y` represent the **valued** of the respective variables `x` and `y`
at the time when the statement `z = (x + y) * (x - y) + (3 * x) + (5 * y)` executes,
instead of the variables.

Typically, when a variable is declared or performing **mutating operations**
(mutating operations are operations that change the value of a variable),
for example, `int a;` or `a = 42;`,
it is seen as a variable;
when its value is read, it is seen as a value (e.g., in the statement `b = 3 * a`, `a` is represents the **value** of variable `a`).
The name of a variable can mean different things in different contexts.

### What is an expression?

Actually, we have already seen an expression before: `(x + y) * (x - y) + (3 * x) + (5 * y)`.
Basically, an **expression** is just a **value**, but viewed from a slightly different perspective.

Technically, **expressions** and **values** are equivalent.
However, when we talk about values,
we usually talk about "atomic values",
i.e., really simple values without any transformation or untransformed values of a variable.
When we talk about **expressions**, we usually mean more complicated values
constructed from simpler values.

Such a subtle difference is illustrated in the table below:

| Typical Values | Typical Expressions |
| -- | -- |
| `42`, `"hello"`, `a` (`a` is a variable) | `(x + y) * (x - y) + (3 * x) + (5 * y)`, `3 * 5`, `"hello" + " world"` |

It is important to note that values and expressions don't have a clear boundary and are technically the same concept.
`42` and `a` are perfectly valid expressions ("atomic expressions"), while `(x + y) * (x - y)` is a value ("compound value") as well.

### Common Terms With Expressions

#### Expression Evaluation

In programming languages, you will often come across the term "evaluate an expression".
To "evaluate" an expressions means to "compute its final value".

For example, consider the expression `3 * 5`;
evaluating this expression means to actually multiply `3` with `5`,
and get the result `15`.

??? code-lab "Code Lab: Values and Expressions"

    Run the following Rust code:

    ```Rust
    fn main() {
        let x = 42;
        let y = 35;
        let z = (x + y) * (x - y) + (3 * x) + (5 * y);

        println!("{}", z);
        println!("{}", 3 * 5);
    }
    ```

    What are the types of `x, y, z`, respectively?

??? code-lab "Code Lab: Intermediate Results"

    Here's some C++ code for reading in the number of days and converting it to seconds
    (if you don't understand what it does, ask an AI):

    ```C++
    #include <iostream>

    int main() {
        int days;
        std::cin >> days;
        int secondsPerHour = 3600;
        int secondsPerDay = secondsPerHour * 24;
        int seconds = days * secondsPerDay;
        std::cout << seconds << std::endl;
        return 0;
    }
    ```

    Compile the code to assembly, making sure to pass the `-O2` flag
    (which means "do compiler optimizations"),
    then find the section corresponding to the `main` function.
    You should see something similar to the following, assuming you're on an x86 machine:

    ```
    (omitted)
    main:
    .LFB1812:
        .cfi_startproc
        endbr64
        pushq	%r12
        .cfi_def_cfa_offset 16
        .cfi_offset 12, -16
        leaq	_ZSt3cin(%rip), %rdi
        pushq	%rbp
        .cfi_def_cfa_offset 24
        .cfi_offset 6, -24
        subq	$24, %rsp
        .cfi_def_cfa_offset 48
        movq	%fs:40, %rax
        movq	%rax, 8(%rsp)
        xorl	%eax, %eax
        leaq	4(%rsp), %rsi
        call	_ZNSirsERi@PLT
        imull	$86400, 4(%rsp), %esi
        leaq	_ZSt4cout(%rip), %rdi
        call	_ZNSolsEi@PLT
        movq	%rax, %rbp
        movq	(%rax), %rax
        movq	-24(%rax), %rax
        movq	240(%rbp,%rax), %r12
        testq	%r12, %r12
        je	.L10
        cmpb	$0, 56(%r12)
        je	.L5
        movsbl	67(%r12), %esi
    (omitted)
    ```

    Look at this.
    Where are the variables `secondsPerHour` and `secondsPerDay`?
    What did the compiler do to optimize, and why won't it affect proper execution of the code?

    *(Hint: This is a trick question.
    What is the product of 3600 and 24?
    This question is very hard for beginners,
    so it's okay to ask an AI for help.)*

    Judging from what you saw,
    is it better to write a really long expression,
    or break it into multiple expressions each assigned to a variable holding it?
    Will the latter have a negative effect on memory usage with the `-O0` flag?
    What if you pass in the `-O2` flag instead of `-O0`?

    *(Hint: Ask an AI about `-O2` and `-O0`).*

!!! question "Question: Lvalues and Rvalues"

    Ask an AI about "lvalues" and "rvalues".

## Operators

Look at the following Rust code:

```Rust
let a = 3;
let b = 4;
println!("{}", a + b);
```

Even though we have not talk about the `+` operator,
you probably already know what the code will output: `7`.
`a + b` will look intuitive even if you haven't learned about operators before,
as long as you know primary school math;
indeed, operators in programming languages are designed to closely mimic math expressions.

### What is an operator and why do we need them?

Formally, an **operator** defines a mapping which transform some value(s) into another value.
For example, the `+` operator maps two values to their addition,
while the `/` operator maps two values to their division.

An operator can take a number of input values called **operand** and produces an output value.
For example, in the expression `3 + 4`, `3` is called the **left operand** and `4` is called the **right operand**.
The `+` operator takes the two operands and produces the sum: `7`.

The reason why we need operators is to make data transformation easy and intuitive.
As we will learn later,
it is possible to transform data without operators at all by using functions (and operators are just functions in essence);
however, doing that will not be very human-friendly,
while using operators allows us to transform data in an intuitive way that resembles math.

Consider the following expressions that does the same thing:

| With Operators | With Functions |
| -- | -- |
| `(3 + 4) ** 5` | pow(add(3, 4), 5) |

Obviously, it is much easier to read and write expressions using operators, compared to doing the same thing with functions.

!!! info "Operator Overriding"
    It is possible to customize what an operator does.
    For example, you can create a custom type and define `+` to work as multiplication, and vise-versa.
    However, the common practice is to define the operator to be "what it naturally should do"
    (e.g., `+` should be addition, not subtraction).
    This is to improve code readability and avoid confusion.

### Operator Taxonomy

Operators can be classified into several categories based on the number of operands they take.
The most common ones are **unary operators**, **binary operators** and **ternary operators**.
**Unary operators** take one operand;
**binary operators** take two operands;
and **ternary operators** take three operands.

!!! info "n-ary operators where n > 3?"
    Operators that take more than 3 operands are very uncommon, if they exist at all.
    Personally speaking, I have never seen such an operator in any programming language.

    The reason for this is that operators (and programming languages in general)
    are meant to make things easy and intuitive, instead of hard and anti-human
    (although a lot of Chinese universities tend to forget that by teaching stuff like `i += (i++ * ++i) ? (++i & i++) : (i++ | ++i), i == (i = i++) * ++i + i++`).
    Operators with more than 3 operands, on the other hand, are hard to understand and cause confusion.
    In fact, ternary operators are also very uncommon;
    as far as I know, the only commonly used ternary operator is the conditional operator `? :`.
    Binary operators are the most common, as they have their counterparts in math.

Operators can also be classified by what they do.
Generally speaking, there are data processing operators and comparison operators.

Data processing operators are operators that do "normal data processing",
like addition, subtraction, multiplication, division, and so on.

Some examples of data processing operators:
`+`, `-`, `*`, `/`, `**` (power operator, e.g., `2 ** 3 == 8`),
logical operators (`&&`, `||`, `!`, `&`, `|`, `^`, `<<`, `>>`).

Comparison operators are operators that "compare" the operands and output a boolean result;
for example, `2 <= 3` evaluates to `true`, while `3 <= 2` evaluates to `false`.
except for very few, uncommon operators (e.g., spaceship operator introduced in newer C++ standards),
the output of these operators are always boolean, i.e., either true or false.

As far as I know, comparison operators are always binary operators.

Some examples of comparison operators:

- `==` (equal to)
- `!=` (not equal to)
- `>` (greater than)
- `>=` (greater than or equal to)
- `<` (less than)
- `<=` (less than or equal to)

There is one operator that falls outside of comparison operator and data processing operators:
the conditional operator `? :`.
We will discuss what it does in the next subsection.

### Basic Operators

Operators are mostly the same in virtually all modern programming languages (that excludes LISP),
and they are typically designed to closely mimic their mathematical counterparts (when applicable).
In this subsection, we discuss the common operators.

#### Arithmetic Operators

These operators represent mathematical operations such as addition and subtraction.

| Operator | Explanation | C++ Example | Python Example | Rust Example |
| -------- | ----------- | ----------- | -------------- | ------------ |
| `+` | `a + b` evaluates to the sum of `a` and `b` | `3 == 1 + 2` | `3 == 1 + 2` | `3 == 1 + 2` |
| `-` | `a - b` evaluates to the difference of `a` and `b` | `-1 == 1 - 2` | `-1 == 1 - 2` | `-1 == 1 - 2` |
| `*` | `a * b` evaluates to the product of `a` and `b` | `6 == 2 * 3` | `6 == 2 * 3` | `6 == 2 * 3` |
| `/` | `a / b` evaluates to the quotient of `a` and `b` | `2 == 6 / 3` | `2 == 6 / 3` | `2 == 6 / 3` |
| `**` | `a ** b` evaluates to the result of raising `a` to the power of `b` | Not Supported | `27 == 3 ** 3` | Not Supported |
| `%` | `a % b` evaluates to the remainder of `a` divided by `b` | `1 == 101 % 2` | `1 == 101 % 2` | `1 == 101 % 2` |

!!! question "Question: The Power Operator"
    Is it more common for compiled languages to implement the power operator or not to implement it?
    What about interpreted languages?
    Why is there such a difference?

    *Hint: This question may involve algorithms and is hard for beginners, so feel free to ask an AI.*

!!! note "Operator Conventions"
    The notations for common operations like addition and subtraction are mostly consistent across languages,
    but there is less consensus when it comes to less common arithmetic operators.

    For example, the power operator is represented as `^` instead of `**` in MATLAB;
    also in MATLAB, `%` is not for modulo, but used to indicate comments.

!!! info "Return Types and Operator Behavior"
    Arithmetic operators work in mostly the same way, but there are some subtle differences across languages
    (especially between compiled & interpreted languages).

    The output type of an arithmetic operator, when its operands are numerical values,
    is usually the same with its operands.
    In C/C++, for example, the output type of `+`, `-`, `*`, and `/` is always the same as its operands,
    when operands are language-defined numerical types like `int`, `float`, `double`, `uint8_t`, etc.
    Even if you try to compute `5 / 3`, the output type will be `1`, instead of `1.6667`.

    However, this is not the case for Python.
    In Python, the behavior of `+`, `-` and `*` are the same, but the behavior of `/` is different:
    if the first operand is divisible by the second, the output type will be `int`;
    otherwise, the output type will be `float`.
    So for example, `5 / 3` returns `1.666...` in Python,
    while `6 / 3` returns `2`.

!!! note "The Order Counts"
    Although operators are designed to closely mimic their mathematical counterparts,
    there are some important differences, especially for binary operators.

    The order of operands may matter, especially when the operator is overridden.
    For example, `a + b` and `b + a` may evaluate to different values on non-numerical types,
    or when the behavior of `+` is overridden.

??? code-lab "Code Lab: Arithmetic Operators"
    Write a simple program that consumes two integers from user input and outputs their sum, difference, division (decimal) and product.

    Ask an AI for how to take input from the console and print to it.

    *Hint: Output decimal, not integer for division.*

??? code-lab "Code Lab: Overflow"
    Compile and run the following C/C++ code:

    ```C++
    #include <iostream>
    #include <limits>

    int main() {
        int a = std::numeric_limits<int>::max();
        int b = a;

        std::cout << a << ' ' << b << std::endl;
        std::cout << a + b << std::endl;

        return 0;
    }
    ```

    What do you observe?
    Can you explain why this happened?

    *Hint: Ask an AI to explain the code for you.*

#### Basic Boolean Algebra and Boolean Operators

!!! note "Note"
    Boolean algebra and boolean operators are a large topic.
    In this section, you will likely find a lot of unfamiliar things,
    both in programming and in mathematics.
    Therefore, you should have an AI by your side
    and ask him/her whenever you see something you don't know and that I do not explain.

##### Basic Boolean Algebra

You may already know that a **boolean** value is one that can be either `true` or `false` from the previous lecture.

!!! info "Other notations of `true` and `false`"
    There are other notations for `true` and `false`.

    Common aliases for `true`: `1`, `TRUE`, `True`.
    Common aliases for `false`: `0`, `FALSE`, `False`.

There are certain algebraic operations defined on boolean values;
they form the basics of boolean algebra.

The most common boolean operations are:

- AND: The AND of two booleans `a` and `b` is true only if both `a` and `b` are true.
Otherwise, it is false.
- OR: The OR of two booleans `a` and `b` is true if either `a` or `b` is true.
Otherwise, it is false.
- NOT: The NOT of a boolean `a` is true if `a` is false and false if `a` is true.
- XOR: The XOR of two booleans `a` and `b` is true if `a` and `b` are different.
For example, $true \operatorname{XOR} true = false; true \operatorname{XOR} false = true$.

##### Boolean Operators

Similar to arithmetic operators, boolean operators are typically the same across different languages.

Here are some examples:

| Operator | Example in C/C++, Java, Rust, C#, Dart | Example in Python |
| -- | -- | -- |
| AND | `true && true == true` | `true and true == true` |
| OR | `true || false == true` | `true or false == true` |
| NOT | `!true == false` | `not true == false` |
| XOR | `true ^ true == false` | `true ^ true == false` |

!!! question "Question: Design Choices"
    Do you think the design of notations of boolean operators in Python is better than that in C/C++,
    or vice versa?

!!! question "Question: Booleans variables"
    Typically, an `int` takes 4 bytes (32 bits), and its range is from $-2^{31}$ to $2^{31} - 1$.
    How many bits does a `bool` take?

    *Hint: This is a trick question.
    It's not just a math question.
    You might want to do it yourself first, then ask an AI.
    Your answer and the AI's are likely different.*

##### Bitwise Operators

Almost all modern computers uses binary to represent data.
As a result, virtually anything from integers to floats, boils down to zeros and ones in memory.

For example, a `uint32_t` type `4` is represented as 4 bytes, or 32 bits `00000000 00000000 00000000 00000100`.

!!! question "Question: Binary Representations of Numbers"
    Consult an AI to learn about how numbers are represented in binary.

    *Hint: For beginners, it is sufficient to learn about integer representations.
    Don't bother with floating point numbers for now.*

As a result, virtually any value can be seen as a collection of booleans
(one boolean for each bit, `0` for `false`, `1` for `true`).
If we have two values, we can perform some boolean operation bit-by-bit.
This is called "bitwise operation".
For example, if we have a `uint32_t` 4 (`00000000 00000000 00000000 00000100`),
and a `uint32_t` 5 (`00000000 00000000 00000000 00000101`),
we can do the bitwise XOR operation;
the first 24 bits of the result will all be `0`,
as each pair of the corresponding bits are both `0`;
similarly, the last 8 bits will be `00000001`.
So, the result is `00000000 00000000 00000000 00000001`,
which can be interpreted as a `uint32_t` `1`.

Bitwise operations are used for various purposes,
like masking a certain part of the bits of a value,
or doing a large number of boolean operations in one go.

Here are the most common bitwise operators:

| Operator | Example in C/C++, Java, Rust, C#, Dart | Example in Python |
| -- | -- | -- |
| Bitwise AND | `4 & 5 == 1` | `4 & 5 == 1` |
| Bitwise OR | `4 | 5 == 5` | `4 | 5 == 5` |
| Bitwise NOT | `~4 == -5` | `~4 == -5` |
| Bitwise XOR | `4 ^ 5 == 1` | `4 ^ 5 == 1` |
| Shift left | `4 << 2 == 16` | `4 << 2 == 16` |
| Shift right | `4 >> 2 == 1` | `4 >> 2 == 1` |

Note that in addition to AND, OR, NOT, and XOR,
we have two new operations: shift left and shift right.

Shift left means to "move the bits to the left";
the bits that are moved out of the leftmost bit are discarded,
while the new bits appearing on the right are filled with zeros.

Shift right does the similar thing, only that the bits are shifted to the right instead of the left.

As an example, `0101` shifted right by 2 bits is `0001`;
`0101` shifted left by 1 bit is `1010`.

#### Comparison Operators

A comparison operator "compares" two values and outputs a boolean.
They are designed to closely mimic their counterparts in mathematics.

Here are the most common comparison operators:

| Operator | Example in C/C++, Java, Rust, C#, Dart, Python |
| -- | -- |
| Equal to | `4 == 5` evaluates to `false` |
| Not equal to | `4 != 5` evaluates to `true` |
| Greater than | `4 > 4` evaluates to `false` |
| Greater than or equal to | `4 >= 4` evaluates to `true` |
| Less than | `4 < 4` evaluates to `false` |
| Less than or equal to | `4 <= 4` evaluates to `true` |

#### Special Operators

Besides the common operators we've seen before, there are some special operators.

##### Increment & Decrement Operators

Some languages such as C/C++ support 4 unary increment & decrement operators for integer-like variables,
denoted by two symbols `++` and `--`.
Strictly speaking, these operators are not really `operators` because they must operate on variables,
and that they mutate the value of the variable.

`++` is called the increment operator,
and there are two variants: `++x` and `x++`,
where `x` is the variable operand.

Both of these variants increments the variable `x` by 1;
however, denote $x_0$ as the value of `x` before the operator is applied,
then `++x` evaluates to $x_0 + 1$, while `x++` evaluates to $x_0$.

For example, if `a` holds the value `42` initially,
then `++a` evaluates to `43`,
while `a++` evaluates to `42`.
After the operator is applied, `a` holds the value `43` in both cases.

Similarly, `--` is called the decrement operator,
and there are two variants: `--x` and `x--`,
where `x` is the variable operand.

Both of these variants decrements the variable `x` by 1;
however, denote $x_0$ as the value of `x` before the operator is applied,
then `--x` evaluates to $x_0 - 1$, while `x--` evaluates to $x_0$.

!!! info "The Semantics of Increment & Decrement Operators"
    There are language-defined behavior of `++` and `--` on integer-like types only.
    However, you can define what `++` and `--` does on custom types by operator overriding.

!!! info ""Legitimate" Usage of Increment & Decrement Operators"
    There has been some discussions on whether increment & decrement operators are a feature or a flaw in the modern world,
    as the non-stateless nature (meaning that they mutate their operand) of these operators can lead to both brevity and confusion.
    
    In fact, many modern programming languages (like Rust) have decided not to support these operators at all.
    Even in languages that does support them (e.g., C/C++),
    people tend to use these operators only in a few well-defined, template-like and very limited cases
    where using `++` or `--` has almost become a standard (e.g., loop counters).

    Although many Chinese universities teach the "advanced usage" of `++` and `--`,
    such as `i += (i *= ++i, i /= i++, ++i ? ++i : i++ % i++ + (++i ? ++i : i++))`,
    such "advanced usage" is generally considered **VERY BAD** practice
    because they serve for no purpose other than complicating the readers.
    As such, they should always be avoided.

!!! question "The Origin of Increment & Decrement Operators"
    If most programming languages decide not to support increment & decrement operators,
    why were they created in the first place?
    Why does C/C++ support them, while Rust does not?

    *Hint: This is a very hard question for beginners.
    For the first question, try searching for "pre-indexing" and "post-indexing" (in context of assembly languages).
    For the second question, search for how old is C/C++, and how old is Rust.
    Then, think about compiler optimizations.
    Feel free to ask an AI for help.*

##### Conditional Operator

The conditional operator `? :` is the only commonly-used ternary operator in modern programming languages.
Basically, `a ? b : c` evaluates to `b` if `a` is true, and to `c` if `a` is false.

For example, `2 < 3 ? 1 : 2` evaluates to `1`.

### Operator Precedence

**Operator precedence** defines the **logical order** in which operators are applied and sub-expressions are evaluated.
Given an expression `a + b * c` for example, it defines whether it is evaluated to $a + (b * c)$ or $(a + b) * c$.

!!! info "Logical Order, Not Physical Order"
    Operator precedence only defines the **logical order**, but there is no guarantee on the actual order in which sub-expressions are evaluated.
    That means, the value of an expression is well-defined
    (guaranteed to be the same as if the sub-expressions were evaluated in the order specified by operator precedence),
    but the actual order in which evaluation happens is not well-defined
    (some evaluations may even happen concurrently).

If one operator has a **higher precedence** than another,
the corresponding sub-expression is evaluated first (logically);
if it has a **lower precedence** than another, the corresponding sub-expression is evaluated later (physically).
For example, if `*` has a higher precedence than `+`, then `a + b * c` evaluates to $a + (b * c)$;
if `*` has a lower precedence, it evaluates to $(a + b) * c$.

When two operators have the **same precedence**, the evaluation typically happens from left to right.
For example, if `+` and `-` have the same precedence, then `a - b + c` evaluates to $(a - b) + c$, not $a - (b + c)$.

Sub-expressions enclosed within braces `()` are evaluated first (logically).
For example, `(a + b) * c` evaluates to $(a + b) * c$, not $a + (b * c)$.

In most cases, operator precedence closely mimics its mathematical counterparts and is consistent across programming languages.
For example, `*` and `/` have the same precedence, higher than `+` and `-` which also have the same precedence.
Among logical operators, `!` have high precedence than `&&` and `||`.
When it comes to other cases, the good practice is to use braces `()` to explicitly state which sub-expressions are evaluated first (logically),
in order to avoid ambiguity.
For example, `a && b || c && d` and `(a && b) || (c && d)` are equivalent,
but it is better to write the latter.

??? code-lab "Code Lab: Putting it Together (Part 1)"
    Without compiling and running, infer the output of the following Rust program:

    ```Rust
    fn main() {
        let mut x = 5;
        let mut y = 6;
        let mut z = x * y + 3;
        println!("x = {}, y = {}, z = {}", x, y, z);
        x = y;
        z = x * y + 3;
        println!("x = {}, y = {}, z = {}", x, y, z);
    }
    ```

    Then, run the code to verify your answer.

    *Hint: Ask an AI to explain what `println!` does.*

??? code-lab "Code Lab: Putting it Together (Part 2)"
    Write a Rust program that converts Celsius to Fahrenheit.

    *Hint: Ask an AI to help you read and print things to the console.*

Congratulations!
You have learned about values, expressions and operators.
Next, we will talk about control flow.
