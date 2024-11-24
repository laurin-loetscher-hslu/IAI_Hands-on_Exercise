# IAI Hands-on Exercise

This repository contains a hands-on exercise for the "Introduction to AI" module at HSLU.

## Overview

In this mini-project, you'll build a command-line calculator in Python that performs basic arithmetic operations. The goal is to create a modular and extendable application while practicing the following concepts:

1. **`pyenv` and `pyenv-virtualenv`**: Learn to create and manage Python environments.
2. **Python Modules**: Organize code into reusable modules and packages.
3. **Command-Line Arguments**: Process system arguments to interact with the program.
4. **Environment Variables**: Configure the application using environment variables.
5. **Makefiles and Testing**: Automate tasks with `make` and run tests using `pytest` or `unittest` within a Makefile.
6. **Debugging**: Use debugging tools to identify and fix issues in your code.

## Getting Started
1. **Clone the repository**:
   ```bash
    git clone https://github.com/laurin-loetscher-hslu/IAI_Hands-on_Exercise.git
    cd IAI_Hands-on_Exercise
   ```

2. **Set up a Python environment**:
   ```bash
   pyenv install 3.9.1    # Skip if already installed
   pyenv virtualenv 3.9.1
   calc-env pyenv activate calc-env
   ```

3. **Run the calculator in the Command-Line**:
   ```bash
    # Available operations: add, subtract, multiply, divide, exponentiate
    python main.py <operation> <a> <b>
   ```
