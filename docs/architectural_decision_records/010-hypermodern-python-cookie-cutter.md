# 10. Using the Hypermodern Python Project Cookie Cutter for Better Python Projects

Date: 2023-06-14

## Status

Accepted

## Decision

We have decided to use the
[Hypermodern Python Project Cookie Cutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
as our project template for Python projects. Here's why:

### Best Practices and Standards

The cookie cutter follows the best practices and industry standards for Python projects. It encourages us to organize
our code in a modular way, write tests before writing code, and continuously integrate and deploy our projects.
By using these conventions, our projects will be easier to understand, work on, and maintain.

### Modern Tools

The Hypermodern Python Project Cookie Cutter includes several modern tools that enhance Python project development:

- Setuptools: Simplifies the distribution of Python packages.
- Pytest: A testing framework for efficient and effective testing of Python code.
- Tox: Automates testing across different Python environments to ensure compatibility.
- Sphinx: Generates comprehensive and user-friendly documentation for Python projects.
- Black: Automatically formats Python code according to a consistent style for improved readability.
- Isort: Organizes import statements in Python code for increased clarity and consistency.

These tools work together to streamline development, automate tasks, and maintain high code quality in Python projects.
By using these tools, we can save time and ensure our code is of high quality.

### Code Quality

The Hypermodern Python Project Cookie Cutter helps us write better code.
It encourages us to use type hints to catch errors early and improve code quality.
It also includes tools that automatically check our code for style and format it consistently.
This leads to fewer bugs and makes our code more readable and maintainable.

### Community Support and Contributions

The cookie cutter has an active community of developers who contribute to its development.
By using this project template, we can benefit from the knowledge and contributions of the community.
This collaboration helps us stay up-to-date with the latest practices and improve our projects.

## Alternatives Considered

Before deciding on the Hypermodern Python Project Cookie Cutter, we evaluated alternative project templates and approaches
for our Python projects. Here are a few alternatives considered:

### Custom Project Structure

We could have created a custom project structure based on our specific requirements.
While this approach offers flexibility, it requires more effort to establish and maintain consistent practices across projects.
It may also lack the extensive tooling and community support provided by established project templates.

### Minimalistic Project Templates

There are minimalist project templates available that provide a bare-bones structure without many additional tools or conventions.
While these templates offer simplicity, they may not cover all aspects of modern Python development, such as automated
testing, code formatting, or documentation generation. Adopting a minimalist template would require us to manually
configure and integrate these tools, potentially leading to inconsistencies across projects.

### Other Project Templates

Several other project templates exist in the Python ecosystem, each with its own set of conventions and tooling.
We considered alternatives like the "Python Packaging Authority" (PyPA) template and the "Cookiecutter Data Science"
template. However, the Hypermodern Python Project Cookie Cutter stood out due to its comprehensive approach, community
support, and alignment with modern Python development practices.

## Risks and Mitigations

While using the Hypermodern Python Project Cookie Cutter brings many benefits, there are some risks to consider:

### Learning Curve

Contributors who are not familiar with the cookie cutter may need time to understand its structure and tools.
We will provide documentation and training to help our team members learn how to use it efficiently.

### Compatibility

The cookie cutter may have dependencies or tooling requirements that conflict with our existing project setup.
Before adopting the cookie cutter, we will evaluate its
compatibility with our current stack and make necessary adjustments. This may involve resolving dependency conflicts or
adapting the project structure to fit our specific needs.

## Conclusion

After careful consideration of alternatives, we have decided to use the Hypermodern Python Project Cookie Cutter for our
Python projects. Its adherence to best practices, inclusion of modern tools, and active community support make it a
strong choice. While there may be a learning curve and potential compatibility issues, the benefits of improved project
organization, code quality, and efficiency outweigh these risks. By adopting this project template, we can establish
consistent development practices, leverage automation tools, and stay connected to a vibrant community of Python developers.
