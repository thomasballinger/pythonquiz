import inspect
import re
from curtsies import fmtfuncs

def annotation(name):
    def annotate(*values):
        def wrapper(question):
            if not hasattr(question, name):
                setattr(question, name, [])
            getattr(question, name).extend(values)
            return Question.convert_or_passthrough(question)
        return wrapper
    annotate.__name__ = name
    return annotate

annotations = ['sources', 'references', 'hints', 'difficulties', 'wrongs', 'tags', 'affirms', 'corrects']
source = annotation('souces')
reference = annotation('references')
hint = annotation('hints')
difficulty = annotation('difficulties')
tag = annotation('tags')
affirm = annotation('affirms')
wrong = annotation('wrongs')
correct = annotation('corrects')


class Question(object):
    title = ''
    template = 'multiplechoice'
    question_is_code = False
    id_counter = 0

    all_questions = []

    def __init__(self, question, correct=None):
        self.question = question
        if correct is None:
            self.corrects = []
        else:
            self.corrects = [correct]
        self.register()
    @classmethod
    def from_func(cls, func):
        lines = deindent(inspect.getsourcelines(func)[0])
        while lines[0].startswith('@'):
            lines.pop(0)
        text = ''.join(lines)
        if getattr(func, 'ignoreresult', False):
            q = cls(text)
        else:
            correct = repr(func())
            q = cls(text, correct)
        q.title = func.__name__
        q.question_is_code = True
        for kind in annotations:
            if not hasattr(q, kind):
                setattr(q, kind, [])
            if hasattr(func, kind):
                getattr(q, kind).extend(getattr(func, kind))
        return q
    @classmethod
    def from_other_question(cls, thing):
        q = cls(thing.question)
        for att in q.__dict__.keys():
            q[att] = thing[att]
        return q
    @classmethod
    def convert_or_passthrough(cls, thing):
        if isinstance(thing, cls):
            return thing
        elif isinstance(thing, Question):
            pass
        else:
            return cls.from_func(thing)
    def register(self):
        Question.all_questions.append(self)
        self.id = Question.id_counter
        Question.id_counter += 1

    def __repr__(self):
        s = fmtfuncs.bold(type(self).__name__)
        s += (': '+fmtfuncs.bold(self.title.title()) if self.title else '')
        s += '\n'
        s += fmtfuncs.gray(self.question)
        s += '\n'
        s += fmtfuncs.gray('\n').join(fmtfuncs.green(repr(x) if not isinstance(x, basestring) else x) for x in self.corrects)
        s += '\n'
        s += fmtfuncs.gray('\n').join(fmtfuncs.red(repr(x) if not isinstance(x, basestring) else x) for x in self.wrongs)
        s += '\n'
        return str(s)
    def solve(self, attempt):
        normalize = lambda x: re.sub("'", '"', re.sub(r'\s', '', repr(x)))
        return normalize(repr(attempt)) in [normalize(c) for c in self.corrects]
    @property
    def answers(self):
        return self.corrects + self.wrongs
    @property
    def answer_objects(self):
        return ([Answer(s, True, self.question_is_code) for s in self.corrects] +
                [Answer(s, False, self.question_is_code) for x in self.wrongs])


class Answer(object):
    def __init__(self, text, correct, is_code = False):
        self.text = text
        self.correct = correct
        self.is_code = is_code
    @property
    def correct_class(self):
        return 'correct' if self.correct else 'incorrect'

def deindent(lines):
    indent = min(len(line) - len(line.lstrip()) for line in lines)
    return [line[indent:] for line in lines]

class WriteTheOutput(Question):
    template = 'textbox'
    pass

def multiplechoice(func):
    pass

def ignoreresult(func):
    """Used to ignore the result of running a function"""
    func.ignoreresult = True
    if hasattr(func, 'corrects'):
        assert len(func.corrects) == 1
        assert isinstance(func, Question)
        func.corrects = []

    return WriteTheOutput.convert_or_passthrough(func)

def yes(func):
    func.corrects = ['Yes']
    func.wrongs = ['No']
    func.ignoreresult = True
    return MultipleChoice.convert_or_passthrough(func)

def no(func):
    func.corrects = ['No']
    func.wrongs = ['Yes']
    func.ignoreresult = True
    return MultipleChoice.convert_or_passthrough(func)

def true(func):
    assert func()
    func.wrongs = [False]
    return MultipleChoice.convert_or_passthrough(func)

def false(func):
    assert not func()
    func.wrongs = [True]
    return MultipleChoice.convert_or_passthrough(func)

def yeahok(func):
    func.wrongs = []
    return MultipleChoice.convert_or_passthrough(func)

question = Question.from_func

class MultipleChoice(Question):
    template = 'multiplechoice'
    def __init__(self, question, correct=None, *wrong):
        self.question = question
        if correct is None:
            self.corrects = []
        else:
            self.corrects = [correct]
        self.wrongs = list(wrong)
        self.register()

class Checkbox(Question):
    template = 'checkbox'
    def __init__(self, question, corrects=(), wrongs=()):
        self.question = question
        self.corrects = list(corrects)
        self.wrongs = list(wrongs)
        self.register()

if __name__ == '__main__':
    @source('http://docs.python.org/2/reference/datamodel.html')
    @tag('addition')
    def addition():
        """Adding two numbers """
        return 1 + 1

    print addition
    print addition.solve(1)
    print addition.solve(2)


    q = MultipleChoice('What does _ do at the interactive prompt?',
                       'Refers to the last non-None answer printed',
                       'Counter for how many times you hit enter',
                       'Something stupid'
                       )
    q.affirmation = ("_ refers to the last non-None answer returned in the REPL, but isn't "
                     "special in executed programs. It's conventionally used to refer to "
                     "variables that aren't going to be used again.")

    print q

    @correct('1 hi [3, 4]')
    @wrong('syntax error')
    @wrong("1, 'hi', [3, 4]")
    @wrong("1, 'hi', <list instance at 0x10401ca70>")
    @wrong("1 'hi' [3, 4]")
    @ignoreresult
    def indentation1():
        """Is this valid Python?"""
        print 1, 'hi', [3, 4]

    print indentation1
