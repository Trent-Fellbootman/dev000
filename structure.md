# DEV-000 Course Structure

Preface: Course goal? What do you need to know to be a "true developer"? How to learn this course?

- Don't try to learn a "specific language"; consult GPT when you have difficulties.

## Module 0: The Abstraction of a Computer

- Address space & memory
- Machine code & compiling

## Module 1: Programming

### How do programming languages work?

#### Programming Fundamentals (Also mention common semantics & coding practices)

- variables & types
- control flow statements
- functions
- classes
- modules

#### Programming Language Taxonomy

- Compiled Languages v.s. Interpreted Languages + virtual-machine-based
- Static typing v.s. Dynamic typing
- Garbage collection v.s. manual resource management
- High-level v.s. low-level

#### Common Concepts in Programming Languages

- **Abstraction**
- Interfaces & ABCs & Polymorphism
- Meta-programming
  - find-replace-based macros
  - generics
- Ownership & lifetimes
- Error Handling
  - try-catch
  - Result

#### Other "Abnormal" Languages

- LISP

### How to code properly?

#### Common Coding Practices

- Code Styling
  - CODE_OF_CONDUCT
- Identifiers Naming Conventions
- Comments & docstrings
- Testing (just mention some concepts)

#### Programming Principles

- Syntax & Semantics: What it can be v.s. What it should be (and usually be)
- Don't repeat yourself
- The rule of elegance
- Hierarchy
- Coupling & Cohesion
- Depend on interfaces, not implementations
- Write comments
- When the program is short, forget about all principles

#### Programming Paradigms

- Object Oriented Programming
- Functional Programming

#### Designing Software Systems (preliminary)

- Modules & APIs
- Coupling & Cohesion

#### How do computer programs run under the hood?

## Module 2: Terminal & Unix Basics

### Terminal & Shell Scripting

- What is a terminal? What is a shell? What is a shell script?
- Taxomony of shell scripting languages: text-based (bash) v.s. data-oriented (powershell & nushell)
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
  - Prompt-custimization & theming
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

## Module 3: Software Systems Development

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

### Designing Software Systems

- Modules & APIs & Interfaces
- Coupling & Cohesion
- Software System Design Principles (In addition to programming principles)
  - Abstract your dependencies

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

## Module 4: Concurrent Programming (Tentative Structure)

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

## Module 5: Computer Architecture Fundamentals

### CPUs

- Pipelines
- Memory Hierarchy
- Branch Prediction & Speculative Execution
- Out of order processing
- Vector instructions & SIMD

### GPUs & Accelerators

## Module 6: Miscellaneous Topics in the Developer's World

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

## Module 7: AI Aided Development & AI Software Development

### Artificial Intelligence Basics

- Deep learning fundamentals
- Abstracting deep neural networks & AI services for developers

### AI Aided Development

- Code-completion
- AI Code Generation (logic code, unit tests, documentation, etc.)
- Auto internationlization
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
