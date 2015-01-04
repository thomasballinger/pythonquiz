from pyquiz import MultipleChoice, Checkbox, question, ask_all, yes, no, wrong, display_answer, true, false, yeahok, correct, wrongtxt, ignorereturn

underscore = MultipleChoice('What does _ do at the interactive prompt?',
                   'Refers to the last non-None expression result',
                   'Counter for how many times you\'ve hit enter')
underscore.explanation = ("_ refers to the last non-None result returned in the REPL, but isn't "
                 "special in executed programs. It's conventionally used to refer to "
                 "variables that aren't going to be used again.")

@question
def division1():
    """Assume Python 2.7"""
    return 5 / 2

@question
def division2():
    return 5 // 2

@question
def division3():
    return divmod(5, 2)

exit1 = Checkbox("Which of these will exit a Python program without printing a stack trace?",
                      ["quit()",
                       "exit()",
                       "raise SystemExit()",
                       "sys.exit()",
                       "os._exit(0)",
                       ],
                      ["raise BaseException()"],
                      answers_are_code=True)

exit2 = Checkbox("Which of these will exit a Python program, even if other non-daemon threads are running, and will skip running `finally` clauses?",
                      ["os._exit(0)"],
                      ["quit()",
                       "exit()",
                       "raise SystemExit()",
                       "sys.exit()",
                       "raise BaseException()"],
                      answers_are_code=True)

multiple_statements = Checkbox("Which of these is a syntactically valid way to put multiple statements on one line?",
                      ["a = 1; foo(2); return 1"],
                      ["(a = 1, foo(2), return 1)",
                       "a, _, _ = 1, foo(2), return 1",
                       "[locals().__setitem__('a', 1), foo(2), __return__(1)]"],
                      answers_are_code=True)

@yes
def indentation1():
 """Is this function valid Python?"""
 if True:
          a = 1
 else:
   a = 10
 return a

@yes
def indentation2():
 """Is this function valid Python?"""
 if True: a = 1
 else: a = 10
 return a

@no
def indentation3():
    """Is this function valid Python?"""
    if True:
        a = 1
    else:
        a = 10
    return a
lines = indentation3.question.split('\n')
lines[1] = ' '+lines[1]
indentation3.question = '\n'.join(lines)

@no
def indentation4():
    """Is this function valid Python?"""
    if True:
        a = 1
    else:
        a = 10
    return a
lines = indentation4.question.split('\n')
lines[4] = ' '+lines[4]
lines[6] = ' '+lines[6]
indentation4.question = '\n'.join(lines)

@wrong("'014 123.45'")
@wrong("' 14 0.456'")
@wrong("'14 0123.456'")
def format1():
    return format(14,"3d") + ' ' + format(123.456,"0.2f")

@wrong('syntax error', is_code=False)
@wrong("1, 'hi', [3, 4]")
@wrong("1, 'hi', <list instance at 0x10401ca70>")
@wrong("1 'hi' [3, 4]")
@display_answer
def printing():
    """What does this function display?"""
    print 1, 'hi', [3, 4]

@wrong(int)
def reassign_variables():
    """What's the value of a by the end of the function?"""
    a = 10
    a = "asdf"
    return type(a)

@wrong("'014 123.45'")
@wrong("' 14 0.456'")
@wrong("'14 0123.456'")
def format2():
    return "{0:3d} {1:0.2f}".format(14,123.456)

file1 = Checkbox("Which of these are methods of file objects",
                      [".readlines()",
                       ".close()",
                       ".seek()",
                       ".read()",
                       ".write()",
                       ".next()",
                       ],
                      [".count()",
                       ".format()",
                       ".encode()"], answers_are_code=True)

file2 = Checkbox("Which of these objects share many methods with file objects?",
                      ["socket.socket()",
                       "sys.stdin",
                       "sys.stderr",
                       "sys.stdout",
                       "StringIO.StringIO",
                       ],
                      ["1"], answers_are_code=True)

file2 = Checkbox("Which of these expressions evaluates to a reversed string? (where the initial string is s)",
                      ["s[::-1]",
                       "''.join(reversed(s))",
                       ],
                      ["s.reverse()",
                       "reversed(s)",
                       "str(reversed(s))",
                       "s[-1]",
                       "s[0:len(s):-1]",
                       "s[-1:0:-1]",
                       "s[len(s):0:-1]"], answers_are_code=True)
@wrong('<int 1>')
@wrong('\'\"1\"\'')
def repr1():
    return repr(1)

@wrong(3)
@wrong(7)
def repr2():
    return len(repr('abc'))

@wrong(5)
@wrong(7)
def repr3():
    return len(str('abc'))

comprehensions = Checkbox("Which of these comprehensions will run without errors in a fresh Python interpreter session?",
                      ["(x for x in 'ab')",
                       "[x+y for x, y in zip('adsf', 'zvxc')]",
                       "{x:y for x, y in zip(range(10), 'abc')}",
                       "{x for x in range(10) if x%2 == 0}",
                       ],
                      ["[1 if x for x in [True, False, True]]",
                       "(x:y for x, y in [[1,2], [3, 4], [5, 6]])",
                       "[ord(c) for c in word for word in ['abc', 'def', 'ghi']]",
                       "(x for x in range(10), range(10)"],
                      answers_are_code=True)

tuples = Checkbox("Which are valid tuples in Python?",
                      ["()",
                       "1,",
                       "(1,2)",
                       "1, 2",
                       "tuple()",
                       "tuple([1,2,3])",
                       ],
                      ["(,)",
                       "tuple(1,2)",
                       "tuple(1)",
                       "(1)",
                       "1 + 1"],
                      answers_are_code=True)

@true
def memory1():
    return [].__sizeof__() > ().__sizeof__()

@true
def memory2():
    l = []
    l.append(1)
    return l.__sizeof__() == [1,2,3,4].__sizeof__()

@false
def memory3():
    l = []
    l.append(1)
    return l.__sizeof__() == [1,2,3,4,5].__sizeof__()

@true
def memory4():
    l1 = ['asdfasdlfk jas;ldfsd;lkfj as;ldkfj asl;dkfj asl;kfj ']
    l2 = ['']
    return l1.__sizeof__() == l2.__sizeof__()

@wrong(set([2,3]))
def sets1():
    return set([1,2,3]) | {2,3,4}

@wrong(set([1,2,3,4]))
def sets2():
    return {1,2,3} & {2,3,4}

@wrong(set([-1, -1, -1]))
def sets3():
    return {1,2,3} - {2,3,4}

@wrong(set([2, 4, 6]))
@wrong(set([1, 2, 3, 4]))
def sets4():
    return {1,2,3} ^ {2,3,4}

@yeahok
def dicts1():
    return dict({'a':1}, b=2, c=3)

@wrong([6, 7])
@wrong(repr('something'))
@wrong(6)
def dicts2():
    """What does the dicts2 return?"""
    d = {1:'a', 'b':2, (4, 5):[6, 7]}
    d.get(4, 'something')

@wrong(2)
@wrong(3)
@wrong(4)
def dicts3():
    for k in {1:2, 3:4}:
        return k

@wrong([2, 4])
@wrong([(1, 2), (3, 4)])
def dicts4():
    return list({1:2, 3:4})

@true
def dicts():
    return 1 in {1:2, 3:4}


iteration1 = Checkbox("Which of the following can be used as iterators in a for loop?",
                      ["open('filename', 'r')",
                       "os.walk('os.path(os.path.expanduser('~')))",
                       "(1,2)",
                       "1,2,3",
                       "{1,2,3}",
                       "xrange(10000000000)",
                       repr("the quick brown fox"),
                       "(x*x for x in range(10) if x%3 == 1)"
                       ],
                      ["open('filename', 'w')",
                       "None",
                       "1 + 1 + 2 + 3"],
                      answers_are_code=True)

@question
def iteration2():
    l = [0,1,2,3,4]
    for i in iter(l.pop, 0):
        l.insert(0, 0)
    return l

@false
def iteration3():
    return hasattr([1,2], 'next')

@true
def iteration4():
    return hasattr(iter([1,2]), 'next')

@false
def iteration5():
    return hasattr('abc', 'next')

@true
def iteration6():
    return hasattr((x for x in 'abc'), 'next')

@wrong(repr('blast off'))
@wrong(1)
@wrong(3)
@wrong(4)
def generators1():
    "placeholder for more generator quesitons to come"
    def countdown(n):
        while n > 0:
            yield n
            n -= 1
        yield 'blast off'
    c = countdown(4)
    c.next()
    c.next()
    return c.next()

@wrong(11 + 22 + 33)
@wrong(11 + 33)
@wrong(11 + 22 + 33 + 44 + 55)
def generators2():
    def odd(iterable):
        for x in iterable:
            if x % 2 == 1:
                yield x
    def elevens():
        for i in xrange(1000):
            yield i * 11
    return sum(x for i, x in zip(range(3), odd(elevens())))

@true
def generators3():
    return range(20).__sizeof__() > xrange(1000).__sizeof__()

@wrong([1, 2, 3, 4])
@wrong([1, 2, 5, 6])
@wrong([1, 2, 6, 7])
@wrong([1, 5, 2, 3])
@wrong([1, 6, 7, 8])
@wrong([1, 2, 6, 7])
def coroutines1():
    def counter(n):
        while True:
            passed_in = yield n
            if passed_in is None:
                n += 1
            else:
                n = passed_in
    c = counter(1)
    return [c.next(), c.send(5), c.next(), c.next()]

f = lambda: None
class Foo(object):
    def __repr__(self):
        return "<type 'char'>"
@wrong((type(1), type('a'), type(None), type(())))
@wrong((type(1), Foo(), type(f), type(())))
@wrong((type(1), type('a'), type(None), type([])))
def type1():
    return type(1), type('a'), type(lambda: None), type([])

def classes1():
    class Foo(object):
        """Very basic classes, whatever the intro covers"""


classes1 = Checkbox("Which are true of objects in Python?",
                    ["Strings and lists are types of built-in objects",
                     "Internal data",
                     "Methods that perform operations involving that data",
                     "All values in Python are objects",
                     "The class statement is used to define new types of objects",
                     ],
                    ["Python objects make hiding data from the programmer easy",
                     "Custom types of objects have inherit behavior from only one parent type",])

@yeahok
def classes2():
    l = []
    return dir(l)

classes3 = MultipleChoice("Method names that start and end with double underscores",
                          "Implement various language operations like +",
                          "Are a great idea, this style should be used for naming new methods",
                          "Are always implemented in the host language (c for cpython)",
                          "Cannot be overridden by custom methods",
                          "Use the same implementation for all types of objects")

@wrongtxt("`class Stack(object)` means that Stack takes one argument at instantiation")
@correct("`class Stack(object)` means the Stack type of object inherits fron `object`")
@wrongtxt("Even though this class definition occurs in a function, the class will be globally accessible")
@correct("Inside the class definition, the def keyword is used to create methods")
@wrongtxt("The first parameter of each method is called self, a keyword in python with special rules")
@correct("The first argument passed in to each method will always be the object itself")
@correct("All operations involving attributes of the object must explicitly refer to the self variable")
@correct("The __init__ method is automatically run to when an object of the type Stack is created")
@correct("The variable x refers to [3, 4, 5] by the end of the function")
@wrongtxt('The Stack object to which s referred no longer exists after `del s`')
@ignorereturn
def classes4():
    """In this code..."""
    class Stack(object):
        def __init__(self):
            self.stack = []
        def push(self, thing):
            self.stack.append(thing)
        def pop(self):
            return self.stack.pop()
        def length(self):
            return len(self.stack)
    s = Stack()
    t = s
    s.push("Dave")
    s.push(42)
    s.push([3,4,5])
    x = s.pop()
    y = s.pop()
    del s
    return

@wrong(['a', 1])
@wrong(['a'])
@wrong([1])
@wrong("<Stack object>")
@display_answer
def classes5():
    class Stack(list):
        def push(self, thing):
            self.append(thing)
    s = Stack()
    s.append(1)
    s.push('a')
    print s

class Repr(object):
    def __repr__(self):
        return "<Foo object>"

@wrong([(Repr(), 1, 2), (1, 2), (1, 2), (1, 2)])
@wrong([(Repr(), 1, 2), (1, 2), (1, 2), (Repr(), 1, 2)])
@wrong([(Repr(), 1, 2), (Repr(), 1, 2), (1, 2), (Repr(), 1, 2)])
@wrong([(1, 2), (Repr(), 1, 2), (1, 2), (Repr(), 1, 2)])
@wrong([(1, 2), (1, 2), (1, 2), (1, 2)])
def classes6():
    class Foo(object):
        def __repr__(self):
            return "<Foo object>"
        def bar(*args):
            return args
        @staticmethod
        def baz(*args):
            return args
    return [Foo.bar(Foo(), 1, 2), Foo().bar(1, 2), Foo.baz(1, 2), Foo().baz(1, 2)]

@yeahok
def exceptions1():
    try:
        undefined_variable
    except NameError as e:
        return e

def foo(x):
    return 3
def bar(x):
    return 3
def baz(x):
    return 3

@wrong(foo)
@wrong(bar)
@wrong(4)
@wrong(7)
def decorators1():
    def foo(x):
        return 3

    @foo
    def bar(y):
        return 4 + y

    return bar

@wrong(foo)
@wrong(bar)
@wrong(baz)
@wrong(7)
@wrong(8)
@wrong(5)
def decorators2():
    def foo(x):
        def baz(z):
            return x(z) + 3
        return baz

    @foo
    def bar(y):
        return y + 5

    return bar(2)


contextmanagers1 = Checkbox('Which of these is a good fit for a context manager?',
                            ['opening a file before working with is, and closing it afterwards',
                             'temporarily setting a global variable to a value, and restoring its original value afterwards',
                             'obtaining a lock on a shared resource in a mutlithreading environment, and releasing it afterwards',
                             'cleanup that ought to happen regardless of whether a section of code is completed normally, or an exception is raised, jumping out of the code.'],
                            ['adding 1 to a variable',
                             'recursively traversing a binary search tree'])

modules1 = Checkbox('Modules...',
        ['have the same name as the filename in which their associated code is written',
            'written in Python must have a .py suffix',
            'are made accessible via the import statement'],
        ['are always written in the host language (for cpython, c)'])

modules2 = Checkbox('from mymodule import MyClass',
        ["executes mymodule",
         "creates a variable called MyClass in the current namespace and binds the class to it"],
        ["creates a variable called mymodule and binds the module object to it"], is_code=True)

modules3 = Checkbox('from mymodule import MyClass as mc',
        ["executes mymodule",
         "creates a variable called mc in the current namespace and binds the class to it"],
        ["creates a variable called mymodule and binds the module object to it"], is_code=True)

help1 = Checkbox('The following are real ways to get help in Python:',
        ['>>> help(reduce)',
         '>>> reduce.__doc__',
         '$ pydoc reduce',
         '>>> dir(reduce)'],
        ['>>> help reduce',
         '>>> reduce.__help__',
         '>>> doc(reduce)'], answers_are_code=True)

executable = Checkbox("In a unix-y environment, which of these are required to make a Python script executable from any directory?",
                      ["Add `#!/usr/bin/env python' or similar to the top of the script",
                       "Set the unix permissions of the file to executable with `chmod u+x`",
                       "Put the script in a folder listed in the PATH environmental variable"],
                      ["Add the file to the PYTHONPATH environmental variable",
                       "Put the script in a folder listed in the PYTHONPATH environmental variable",
                       "Add the file to the PATH environmental variable"])

if __name__ == '__main__':
    ask_all()
