questions.py
-----------

DSL for writing Python quizes in Python

Python Quiz
-----------

    >>> chicken = Question("Why did the chicken cross the road?",
    ...     correct="to get to the other side",
    ...     wrong=["it just did it", "for fun", "no reason really"])
    >>> chicken.ask()
    Why did the chicken cross the road?
    # user types "for fun"
    incorrect
    >>> 

Construct Question objects, create interactive quizes in the terminal or browser!

I'm not planning for much collection of data, stats, etc. Just another way to learn material.

There are three kinds of questions:

 * multiple choice
 * checkboxes
 * fill in the blank

Questions have correct and incorrect answers associated with them.

Questions can be annotated with information like sources, references,
hints, and difficulty rating. Questions and answers contain formatting
information in metadata, like whether the answer is code.

Answers can be annotated with information like explanations.

Questions can be constructed directly with Question classes, or 
with decorators on a function whose source is the question.
Questions from functions can be run automatically to find their
correct answer, by recording what the function returns and prints
to stdout.

Autodiscovery
-------------

When you create a question, it's added to the Questions.questions class attribute dictionary under the module in which the question was created.

TODO

* Question class usable for multiple choice

* command line interactive quiz for each question type
  * multiple choice
  * checkbox
  * file in the blank

* special case multiple choice where choices are true and false (like yes/no, no shuffle, t/f one letter)

* Autodiscovery - what module was the top level decorator or constructor called from?

* exciting decorator interface

* create interactive vs all-together modes (ask() vs <name?>())

* HTML rendering of questions!

* JavaScript for interactive learning

* JavaScript for full quizzes

* elimination of duplicate answers
* if all answers are numbers, don't use numbers in the terminal (maybe letters instead?)

* assert that true / false decorators are applied correctly, or make them both @bool
  (what's the point of these anyway? To make otherwise fill-in-the-blank questions multiple choice)

* ensure mixing and matching works properly, and well-document which decorators can be used when


Content Todo
------------

* finish intro questions
  * generators, coroutines
  * objects, classes, methods
  * exceptions, briefly context managers
  * imports
  * dir, help, __doc__, __file__, 

* Do quizzes for rest of Python Essential Reference book

* make a "being careful" quiz, with questions from https://alexbers.com/python_quiz/

* annotate questions with answers, make them better for learning

* make a quiz based on questions people ask when reading code (like bpython)



references:

* http://docs.python-guide.org/en/latest/ - contribute something to it!
* http://stackoverflow.com/questions/101268/hidden-features-of-python
* Raymond Hettinger Idiomatic Python https://www.youtube.com/watch?v=OSGv2VnC0go


Could just make this the quiz companion to 
The Python Essential Reference 4th edition
(but will need to check that this is ok with ddabeaz if I crib anything more)

other:

how to make multiple expression lambdas?

how to run Python code directly from the command line?

how to exit a program despite having non-daemon threads running? (os._exit())

draw out an object graph (OPT-style) of something complicated

what python statements have else clauses

other useful builtin iterators from Ned's talk: os.path

draw some object graphs with lists #TODO come back to this, need image


I think you should know a lot of this stuff within a month of learning Python,
but maybe longer if Python is your first programming language


Following the outline of Python Essential reference:
====================================================

Everything in the next section:  you should know it!

cursory introduction

Tutorial Introduction
---------------------

If you're going to use Python for just one project, learn these things.

Left to do:

* objects and classes
* list methods etc. with dir
* know what type with type
* know the + -> __add__ correspondence
* write a method
* staticmethods
* Exceptions
* with file
* with lock
* why withs are useful for exceptions?
* all the different imports
* dir again
* help(obj)
* .__doc__
* pydoc command line tool


