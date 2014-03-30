from questions import source, reference, hint, difficulty, wrong, tag, affirm, question, ignoreresult, correct, wrong, yes, no
from questions import MultipleChoice, Checkbox, Question

underscore = MultipleChoice('What does _ do at the interactive prompt?',
                   'Refers to the last non-None result printed',
                   'Counter for how many times you\'ve  enter',
                   'Something stupid'
                   )
underscore.affirmation = ("_ refers to the last non-None result returned in the REPL, but isn't "
                 "special in executed programs. It's conventionally used to refer to "
                 "variables that aren't going to be used again.")


executable = Checkbox("Which of these are required to Python program runnable form the command line?",
                      ["Add `#!/usr/bin/env python' to the top of the script",
                       "Set the unix permissions of the file to executable via `chmod u+x`",
                       "Put the script in a folder listed in the PATH environmental variable"],
                      ["Add the file to the PYTHONPATH environmental variable",
                       "Put the script in a folder listed in the PYTHONPATH environmental variable",
                       "Add the file to the PATH environmental variable"])
print question
@question
def division1():
    return 5 / 2

@question
def division2():
    return 5 // 2

@question
def division3():
    return divmod(5, 2)

exit1 = Checkbox("Which of these will exit a Python program",
                      ["quit()",
                       "exit()",
                       "raise SystemExit()",
                       "sys.exit()",
                       "os._exit(0)",
                       ],
                      ["raise BaseException()"])

exit2 = Checkbox("Which of these will exit a Python program, even if other non-daemon threads are running, and will skip running `finally` clauses?",
                      ["os._exit(0)"],
                      ["quit()",
                       "exit()",
                       "raise SystemExit()",
                       "sys.exit()",
                       "raise BaseException()"])
@correct('1 hi [3, 4]')
@wrong('syntax error')
@wrong("1, 'hi', [3, 4]")
@wrong("1, 'hi', <list instance at 0x10401ca70>")
@wrong("1 'hi' [3, 4]")
@ignoreresult
def printing():
    """What does this function display?"""
    print 1, 'hi', [3, 4]

def reassign_variables():
    """What's the value of a by the end of the function?"""
    a = 10
    a = "asdf"
    type(a)

multiple_statements = Checkbox("How do you put multiple statements on one line in Python?",
                      ["a = 1; foo(2); return 1"],
                      ["(a = 1, foo(2), return 1)",
                       "a, _, _ = 1, foo(2), return 1",
                       "[locals().__setitem__('a', 1), foo(2), __return__(1)]"])

@yes
def indentation1():
    """Is this function valid Python?"""
    print 1, 'hi', [3, 4]


if __name__ == '__main__':
    for q in Question.questions:
        print q
