# 7. Use Python for the application functionality

Date: 2023-04-07

## Status

Accepted

## Context

We need to make a decision about what language will be used to develop the core application functionality. There are many possible workable choices.
For purposes of this application, a general purpose language like Python, Go, and Java would all also be good potential choices.
Our project includes data analysis.

## Decision

We will use Python for the main application functionality, Python for tests, and Poetry for build and dependency automation.
We are supporting Python 3.9 and 3.10 in order to use modern type hinting.

## Rationale

Python is a versatile programming language that is widely used in the area of data analysis.
It is an interpreted language, which means that it does not need to be compiled, and it has an easy-to-read and understand
syntax. Other important factors for our decision include the following:

1. **Availability of libraries:** Python has a huge collection of libraries and frameworks, such as NumPy and Pandas,
   which makes it easier for developers to implement data analysis.

1. **Community support:** Python has a large and active community of developers who contribute to its development and provide
   support and guidance on various forums and websites. This makes it easier for beginners to find help and learn the language.

1. **Scalability:** Python is scalable, which means that it can handle large datasets and complex applications. It can
   also be used for rapid prototyping or building small applications with minimal effort, making it easier for us to start
   our project and iterate quickly.

1**Flexibility:** Python can be used for various types of projects, including web development, scientific computing,
machine learning, etc. It is also compatible with other programming languages, such as Java and C++, which makes it easier
to integrate with other systems.

## Consequences

1. **Performance:** Python can be slower than compiled languages like C++ when it comes to executing certain algorithms,
   but this can be mitigated by using optimized libraries or writing critical code in C++ and interfacing with it using Python.

1. **Version compatibility:** Different versions of Python can have different syntax and capabilities, which can make it
   difficult to maintain and update projects. It is important to choose a version of Python that is widely supported and
   compatible with our project requirements. When possible, we try to support multiple versions of Python to support the widest set of users.

## Conclusion

After considering the pros and cons of using Python as our programming language, we have decided that it is the best choice
for our project. We believe that it will provide us with the most flexibility, availability of libraries, and community
support, while also being scalable and adaptable to our changing needs.
