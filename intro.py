from quizbuilder import MultipleChoice, Checkbox, question, ask_all, yes, no, wrong, display_answer, true, false, yeahok

underscore = MultipleChoice('What does _ do at the interactive prompt?',
                   'Refers to the last non-None result printed',
                   'Counter for how many times you\'ve hit enter')
underscore.explanation = ("_ refers to the last non-None result returned in the REPL, but isn't "
                 "special in executed programs. It's conventionally used to refer to "
                 "variables that aren't going to be used again.")

executable = Checkbox("Which of these are required to Python program runnable form the command line?",
                      ["Add `#!/usr/bin/env python' to the top of the script",
                       "Set the unix permissions of the file to executable via `chmod u+x`",
                       "Put the script in a folder listed in the PATH environmental variable"],
                      ["Add the file to the PYTHONPATH environmental variable",
                       "Put the script in a folder listed in the PYTHONPATH environmental variable",
                       "Add the file to the PATH environmental variable"])
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

multiple_statements = Checkbox("How do you put multiple statements on one line in Python?",
                      ["a = 1; foo(2); return 1"],
                      ["(a = 1, foo(2), return 1)",
                       "a, _, _ = 1, foo(2), return 1",
                       "[locals().__setitem__('a', 1), foo(2), __return__(1)]"])

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

@wrong('syntax error')
@wrong("1, 'hi', [3, 4]")
@wrong("1, 'hi', <list instance at 0x10401ca70>")
@wrong("1 'hi' [3, 4]")
@display_answer
def printing():
    """What does this function display?"""
    print 1, 'hi', [3, 4]

@wrong(repr(int))
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
                       ".format()"
                       ".encode()"])

file2 = Checkbox("Which of these objects share many methods with file objects?",
                      ["socket.socket()",
                       "sys.stdin",
                       "sys.stderr",
                       "sys.stdout",
                       "StringIO.StringIO",
                       ],
                      ["1"])

file2 = Checkbox("Which of these expressions evaluates to a reversed string? (where the initial string is s)",
                      ["s[::-1]",
                       "''.join(reversed())",
                       ],
                      ["s.reverse()",
                       "reversed(s)",
                       "str(reversed(s))",
                       "s[-1]",
                       "s[0:len(s):-1]",
                       "s[-1:0:-1]",
                       "s[len(s):0:-1]"])
@wrong('<int 1>')
@wrong('\'\"1\"\'')
def repr1():
    return repr(1)

@wrong(3)
@wrong(7)
def repr2():
    return len(repr('abc'))

@wrong(3)
@wrong(7)
def repr3():
    return len(str('abc'))

comprehensions = Checkbox("Which are valid comprehensions in Python?",
                      ["(x for x in 'ab')",
                       "[x+y for x, y in zip('adsf', 'zvxc')]",
                       "{x:y for x, y in zip(range(10), 'abc')}",
                       "{x for x in range(10) if x%2 == 0}",
                       ],
                      ["[1 if x for x in [True, False, True]]",
                       "(x:y for x, y in [[1,2], [3, 4], [5, 6]])",
                       "[ord(c) for c in word for word in ['abc', 'def', 'ghi']]",
                       "(x for x in range(10), range(10)"])

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
                       "1 + 1"])

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
def dicts2():
    d = {1:'a', 'b':2, (4, 5):[6, 7]}
    d.get(4, 'something')

@wrong(2)
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


iteration1 = Checkbox("Which of the following can be used as interators in a for loop?",
                      ["open('filename', 'r')",
                       "os.walk('os.path(os.path.expanduser('~')))",
                       "(1,2)",
                       "1,2,3",
                       "{1,2,3}",
                       "xrange(10000000000)",
                       "the quick brown fox",
                       "(x*x for x in range(10) if x%3 == 1)"
                       ],
                      ["open('filename', 'w')",
                       "None",
                       "1 + 1 + 2 + 3"])

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
@wrong(repr(1))
@wrong(repr(3))
@wrong(repr(4))
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

@wrong(repr(11 + 22 + 33))
@wrong(repr(11 + 33))
@wrong(repr(11 + 22 + 33 + 44 + 55))
def generators2():
    def odd(iterable):
        for x in iterable:
            if x % 2 == 1:
                yield x
    def elevens():
        for i in xrange(1000):
            yield i * 11
    return sum(x for i, x in zip(odd(elevens()), range(3)))

@true
def generators3():
    return range(20).__sizeof__() > xrange(1000).__sizeof__()

@wrong(repr([1, 2, 3, 4]))
@wrong(repr([1, 2, 5, 6]))
@wrong(repr([1, 2, 6, 7]))
@wrong(repr([1, 5, 2, 3]))
@wrong(repr([1, 6, 7, 8]))
@wrong(repr([1, 2, 6, 7]))
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

@wrong(repr((type(1), type('a'), type(None), type(()))))
@wrong(repr((type(1), type('a'), type(coroutines1), type(()))))
@wrong(repr((type(1), type('a'), type(None), type([]))))
def type1():
    return type(1), type('a'), type(lambda: None), type([])

if __name__ == '__main__':
    ask_all()
