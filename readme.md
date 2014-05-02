questions.py
-----------

DSL for writing Python quizes in Python

Example quiz: http://ballingt.com/python_essential_reference_intro_quiz.html

Post: http://ballingt.com/2014/05/02/pyquiz-intro-quiz.html

Construct Question objects, create interactive quizes in the terminal or browser!

`python pyquiz intro.py -o test.html`

creates an html quiz called test.html.

At the Python prompt:

    >>> chicken = Question("Why did the chicken cross the road?",
    ...     correct="to get to the other side",
    ...     wrong=["it just did it", "for fun", "no reason really"])
    >>> chicken.ask()
    Why did the chicken cross the road?
    # user types "for fun"
    incorrect
    >>> 


I'm not planning for much collection of data, stats, etc. Just another way to learn material.

Details
-------

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

Todo
----

* make pip installable

* Beautiful web view (write some CSS!)

* Add source, hint, etc. annotations on questions and display them

* Score-keeping mode in html

* elimination of duplicate answers

* if all answers are numbers, don't use numbers in the terminal (maybe letters instead?)

* assert that true / false decorators are applied correctly, or make them both @bool
  (what's the point of these anyway? To make otherwise fill-in-the-blank questions multiple choice)

* ensure mixing and matching works properly, and well-document which decorators can be used when

Content Todo
------------

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

other question ideas:

* how to make multiple expression lambdas?
* how to run Python code directly from the command line?
* how to exit a program despite having non-daemon threads running? (os._exit())
* draw out an object graph (OPT-style) of something complicated
* what python statements have else clauses
* other useful builtin iterators from Ned's talk: os.path
* draw some object graphs with lists #TODO come back to this, need image

Python Essential Reference Intro section Quiz
---------------------------------------------

If you're already pretty familiar with another programming language, and
you're going to use Python for just one project, and don't want to read
anything else, you should read pages 5 to 25 of
pages of Python Essential Reference. Intro.py is a quiz to go along with that.

Also consider the official Python tutorial, Dive Into Python, and the rest of
Python Essential Reference.

Questions in `intro.py`.
