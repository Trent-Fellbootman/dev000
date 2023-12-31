# Module 2: Programming Languages

![programming-languages](res/programming-language-icons.png)

It's finally time we get into "real" developer stuff!
In this module,
we're going to talk about programming languages systematically.
In other words, we'll discuss:

- What is a programming language? Why do we need programming languages?
- What are the types of programming languages out there? What are the characteristics of each type?
- What are the common concepts, syntax and characteristics found in modern programming languages?
What are the rationales behind such design?

In addition, there will be some
"mini coding labs" that get your hands dirty on coding,
and at the end of this tutorial,
there will be a final project that showcases how to create software with programming languages.

## How to learn this module?

This module is designed to be beginner-friendly,
but that doesn't mean it's a language tutorial.
Since the design philosophy of this course is
"omit everything that can be easily found with AI (in 2023) or a search engine",
**I will not get into details of the actual syntax of specific programming languages**,
either when explaining concepts or in the code labs.
Instead, I will assume you have access to an AI consultant (such as ChatGPT)
and **you should always ask him/her (or Google) to explain such things for you**.
Looking for answers on the Internet (and with AI, starting from the end of 2022)
is a very important ability for developers,
and I strongly encourage you to start developing that ability right at the beginning.

Here is an example of how you can ask ChatGPT for help:

```markdown
You:
Could you please explain the primitive variable types and their sizes (in bytes) in C++?
Please be as concise as possible.

ChatGPT:
Sure, here's a concise explanation of the primitive variable types and their sizes in C++:

1. **char**: Typically 1 byte. Used to represent single characters.
2. **int**: Typically 4 bytes. Used for integers.
3. **float**: Typically 4 bytes. Used for single-precision floating-point numbers.
4. **double**: Typically 8 bytes. Used for double-precision floating-point numbers.
5. **bool**: Typically 1 byte. Used for Boolean values (`true` or `false`).
6. **short int** (short): Typically 2 bytes. Used for smaller integers.
7. **long int** (long): Typically 4 bytes (but can be 8 bytes on some systems). Used for larger integers.
8. **long long int**: Typically 8 bytes. Used for even larger integers.
9. **unsigned int**: Typically 4 bytes. Like `int` but only positive values.
10. **long double**: Typically 12 or 16 bytes. Used for extended precision floating-point numbers.

It's important to note that the exact size of these types can vary based on the compiler and the architecture of the machine.
The sizes mentioned above are common, but not guaranteed for all environments.
The C++ standard defines minimum sizes for these types but allows compilers to use larger sizes.

You:
Thank you!

ChatGPT:
You're welcome! If you have any more questions, whether about C++ or anything else, feel free to ask. Happy coding!
```

Throughout learning this module, it is also very important to do a lot of programming.
**As of 2023, coding a lot is still indispensable in learning to code**.
"Practice makes perfect" holds true for coding too.

If you don't know what to code, a good starting point is to learn a framework.
For example, you can learn [Unity](https://unity.com/),
which is a game engine that allows to create awesome games while learning programming;
or you can learn [Flutter](https://flutter.dev/),
which allows you to create beautiful apps with ease.
You can ask an AI to suggest other frameworks as well.

## Switch to Linux as soon as possible!

Additionally, I strongly recommend you to install a Linux operating system (OS) and get familiar with the terminal
(if you don't know what a terminal is, ask AI) as soon as possible.
If you're really, really concerned with messing up your computer, you can start with a virtual machine, docker or WSL at the moment,
but I would recommend that you switch to a "native" installation (like dual booting) when you're ready.
The reasons to use a Linux OS are:

- Linux allows you to better understand how computer hardware, operating system and software work.
This is because Linux is, by design, for developers, while Windows is designed for non-developer, "regular" users.
As a result, Windows abstracts away too many details of operating systems, software, hardware, etc.,
including those that developers should understand,
while Linux-based operating systems typically don't.
For example, you can easily control the frequency of your CPU cores on Linux,
but you can't do it easily on Windows.
- The development ecosystem is much better on Linux.
Many frameworks and software support Linux only;
even if it's not the case, it is almost always much easier to configure development environments
(i.e., suites of software for development) on Linux.
On the other hand, it is notoriously hard to configure virtually any developer stuff on Windows.
This holds true even for Visual Studio Code, an Integrated Development Environment (IDE) from Microsoft itself.

You may have noticed that I used the term "Linux-based operating systems" above.
That's right, Linux is not an operating system itself;
instead, there are many operating systems that are "based" on Linux,
like Debian, Ubuntu, Arch Linux and Deepin.

Personally, I would recommend beginners to use the latest LTS (long-term-support) version of [Ubuntu](https://ubuntu.com/), because:

1. It's easy to install and beginner-friendly
(don't be over-confident to try arch; you'll attempt suicide during installation).
2. It has a great ecosystem.
In most cases, if a developer thing doesn't support Ubuntu, you can't expect it to work on anything else.

Some resources to get you started with Linux:

- The [first](https://missing.csail.mit.edu/2020/course-shell/) and
[second](https://missing.csail.mit.edu/2020/shell-tools/)
lecture of [MIT Missing Semester](https://missing.csail.mit.edu/):
these lectures are good getting-started tutorials with shells.
(If you find these too lengthy, you can also ask an AI to tutor you.)
- [Nushell](https://www.nushell.sh/): a modern shell (again, ask an AI if you don't know what it is).
Personally, I have replaced bash with nushell,
and I believe data-oriented shells like nushell will inevitably replace text-oriented ones like bash,
which the de-facto standard at present (2023).
However, **nushell is still nascent at present (2023), lacking a mature ecosystem**,
and I would recommend that you get familiar with bash before trying it out.
- [Oh My Posh](https://ohmyposh.dev/): You can use this to make your terminal look more beautiful.
Works with many shells, including nushell (may need some tuning).
If you use other shells, there are other members of the "oh-my-" family as well,
such as ["oh-my-bash"](https://github.com/ohmybash/oh-my-bash) and
["oh-my-zsh"](https://ohmyz.sh/).
- [Customize your Ubuntu into macOS Monterey](https://youtu.be/4LWh9LnXlj0?si=sYmJg1g6yR314bR2):
A tutorial which tells you how to make Ubuntu look like mac
(yep, I made that video).
You may want to try this out if you like mac-style aesthetics.

Next, we're going to talk about what a programming language is,
and the major families of programming languages out there.
