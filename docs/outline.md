# DEV-000 Course Structure

Note: Some modules are not available yet.
The names of available modules are shown as links,
while unavailable modules are shown as plain text.

## [Module 0: The Developer's Mindset](developer-mindset/index.md)

This module covers the fundamental concepts that underlies all aspect of the developer's world, such as abstraction and hierarchy.

Topics include:

- Abstraction
- Hierarchy
- Standards

## [Module 1: The Abstract Computer](abstract-computer/index.md)

Prerequisite Modules:

- Module 0: The Developer's Mindset

This module explains how a computer is abstracted to developers. Topics include:

- Memory address, stack, heap, etc.
- How a program gets run: compilation, linking, etc.

## Module 2: Programming Languages

Prerequisite Modules:

- Module 0: The Developer's Mindset
- Module 1: The Abstract Computer

This module gives a panoramic introduction to programming languages. This is not a tutorial to a specific language; instead, it explains how programming languages generally work, introduces the syntactical constructs found in almost all mainstream languages and compares the styles and design choices of multiple programming languages.

This module does not assume you have any experience with coding, but it is not a programming tutorial. Instead of learning to code by reading this module exclusive, you are expected to consult GPT on how to actually code in specific languages.

After learning this module, you should have a good understanding of how modern programming languages work and why they are designed in certain ways. With the help of GPT, you should be able to get started and code in any language.

Specific topics covered in this module are listed below.

### Programming Fundamentals

- variables & types
- control flow statements
- functions
- classes
- modules

### Programming Language Taxonomy

- Compiled Languages v.s. Interpreted Languages + virtual-machine-based
- Static typing v.s. Dynamic typing
- Garbage collection v.s. manual resource management
- High-level v.s. low-level

### Common Concepts in Programming Languages

- **Abstraction**
- Interfaces & ABCs & Polymorphism
- Meta-programming
  - find-replace-based macros
  - generics
- Ownership & lifetimes
- Error Handling
  - try-catch
  - Result

### Other "Abnormal" Languages

- LISP

## Module 3: Coding Properly

Prerequisite Modules:

- Module 2: Programming Languages

This module explains the "good practices" and paradigms in programming, and more importantly, the logic behind them.

After learning this module, you should get a good idea of how to design and code up large projects with hundreds of thousands of lines of code.

### Common Coding Practices

- Code Styling
  - CODE_OF_CONDUCT
- Identifiers Naming Conventions
- Comments & docstrings
- Testing (just mention some concepts)

### Programming Principles

- Syntax & Semantics: What it can be v.s. What it should be (and usually be)
- Don't repeat yourself
- The rule of elegance
- Hierarchy
- Coupling & Cohesion
- Depend on interfaces, not implementations
- Write comments
- When the program is short, forget about all principles

### Programming Paradigms

- Object Oriented Programming
- Functional Programming

### Designing Software Systems

- Modules & APIs & Interfaces
- Coupling & Cohesion
- Other Considerations
  - Abstract your dependencies

## Module 4: Terminal & Superuser Basics

Prerequisite Modules:

- Module 2: Programming Languages (recommended)

This module introduces terminal, operating system basics and other "superuser stuff".

This module should take you from a "regular user" who interacts with a computer by dragging-dropping and pushing buttons to a "superuser" who feels comfortable using terminals and doing multi-booting.

Specific topics are listed below.

### Terminal & Shell Scripting

- What is a terminal? What is a shell? What is a shell script?
- Taxonomy of shell scripting languages: text-based (bash) v.s. data-oriented (powershell & nushell)
- Key differences between scripting languages and programming languages
- Shell scripting basics
  - Basic commands
    - cd, pwd, pushd, popd, find, ...
  - variables & control flows, etc.
  - commands
  - pipes & redirection
  - environment variables
  - Miscellaneous
    - &&, ;, $!, ...
- Terminal Tricks & Common Practices
  - Auto-completion, history, etc.
  - Shell config files
  - Prompt-customization & theming
  - Shell plugins
  - Common Tools & Commands
    - grep, cut, awk, tmux, ssh, etc.

### Package Management

- Software dependencies
- Software packages
- Package managers

### Miscellaneous

- Config files
- vim & emacs
- Virtualization & docker
- Booting
  - Hard drive partitions & (g)parted
  - Bootloaders & GRUB
  - BIOS & UEFI
  - Dual (Multi) Booting
- Linux potpourri
  - kernel modules

## Module 5: Software Development

Prerequisite Modules:

- Module 2: Programming Languages
- Module 3: Coding Properly

This module explains the common concepts and tools involved with software development.

After learning this module, you should feel comfortable starting a large project, coding it up with a team, and publishing it to the public.

Specific topics are listed below.

### Common Concepts in Software Systems

- Versioning & Dependencies
  - Semantic Versioning
- Interfaces & APIs & Libraries
- Remote Procedure Call (RPC)
- Serialization & Deserialization
- Inter-process communication (IPC)
- Frameworks
  - What is a framework? Why framework?
  - Framework v.s. Library
  - Examples: Flutter (UI), PyTorch (deep learning) & Unity (game development)
- Specification & Standards (Use examples to illustrate the concept)
  - Why standards?
  - Examples
    - CPU Instruction Set Architectures (ISAs)
    - GPU specifications (OpenGL & Vulkan)
    - Data Representation Standards (JSON, TOML, YAML, XML, HTML)

### Testing

- Unit testing

### Documentation

- Docstrings
- API Docs
- Tutorials
- Doctests
- Common documentation frameworks & languages
  - Sphinx & mkdocs (just mention)
  - Markdown & RST

### Building & Deployment (tentative)

- Build systems

### Version Control

- Version control & git

### Standardization & Collaboration

- The need for standardization across contributors
- CODE_OF_CONDUCT

### CI/CD

### Miscellaneous

- PRs & Issues
- README, CONTRIBUTE, LICENSE
- TODOs & FIXMEs

## Module 6: Concurrent Programming

Prerequisite Modules:

- Module 2: Programming Languages
- Module 3: Coding Properly (recommended)

This is a relatively stand-alone module that explains the concepts involved with concurrent programming.

Topics are listed below.

### Introduction to Concurrency

#### Concurrency Model

- Concurrency v.s. parallelism

#### Problems with Concurrency

- Data races

### Low-level concurrent programming

#### Synchronization primitives

- Locks (Mutexes)
- Semaphores
- Read-Write Locks

### Concurrent Programming Paradigms

#### Channels

#### Producer & Consumer

#### Asynchronous Programming

- Futures & poll
- async & await

## Module 7: Computer Architecture Fundamentals

Prerequisite Modules:

- Module 1: The Abstract Computer
- Module 2: Programming Languages (strongly recommended)

This module introduces the very basics of how computers work in hardware.

After learning this module, you should have a deeper understanding of computers and be able to code programs that utilize the hardware in an optimized way.

Topics are listed below.

### CPUs

- Pipelines
- Memory Hierarchy
- Branch Prediction & Speculative Execution
- Out of order processing
- Vector instructions & SIMD

### GPUs & Accelerators

## Module 8: Miscellaneous Topics in the Developer's World

Prerequisite Modules:

- Module 2: Programming Languages (strongly recommended)
- Module 3: Coding Properly (recommended)

This section discusses the various fields and common tools in the developer's world.

Topics are listed below.

### UI & App Development

- Declarative UI v.s. Imperative U

### Game Development

- Entity Component System (ECS)

### GPU Programming

- High-level: OpenGL
- Low-level: Vulkan

### Miscellaneous

- Stackoverflow
- GitHub
- IDEs
- LSPs
- Hugging Face

## Module 9: AI Aided Development & AI Software Development

Prerequisite Modules:

- Module 2: Programming Languages
- Module 3: Coding Properly (Recommended)

This module discusses how to use AI to develop better, and how to develop applications that take advantage of AI.

Topics are listed below.

### Artificial Intelligence Basics

- Deep learning fundamentals
- Abstracting deep neural networks & AI services for developers

### AI Aided Development

- Code-completion
- AI Code Generation (logic code, unit tests, documentation, etc.)
- Auto internationalization
- AI as an augmented Google

### AI Software Development

#### A Change of Mindset: How is this different from "traditional software development"?

- Determinism -> Non-deterministic behavior
- Structured Data -> Natural Language
- AI involved control flows
- Short latency -> long-running operations
- Error Handling & How to ensure robustness when there is AI

#### Paradigms & Common Practices at Present

- AI Agents
- Retrieval Augmented Generation (RAG) & Vector Databases
- Prompt Engineering & Prompt templates
