![](https://img.shields.io/badge/stars%20⭐-32-yellow)
![](https://img.shields.io/badge/days%20completed-16-blue)
# AdventOfCode2022
This year I decided to solve AdventOfCode using Python before I am going to put myself through the pain of doing it with C++ or Rust next year :)

## Structure
* ``helpers`` contains a default-template for new days and helper-functions. 
I will probably add more generic functions there, as the days get more difficult.
``ImportHelpers.getInput()`` is the default-import function input. It reads the day # from the fileName (``...#.py``) and returns the content of ``inputs.input#.txt`` as String
* ``inputs`` contains all inputs in numbered files (``input#.py``).
* The ``days`` are stored in the base-directory as ``Day#.py``.

## Run
The code can be cloned to any folder and be run immediately without any parameters. Each day will print the results to the console.
