import inspect

def annotation(name):
    def annotate(*values):
        def wrapper(question):
            if not hasattr(question, name):
                setattr(question, name, [])
            getattr(question, name).extend(values)
            return OutputQuestion.convert_or_passthrough(question)
        return wrapper
    annotate.__name__ = name
    return annotate

annotations = ['source', 'reference', 'hint', 'difficulty', 'wrong', 'tag', 'affirmation']
source = annotation('souce')
reference = annotation('reference')
hint = annotation('hint')
difficulty = annotation('difficulty')
wrong = annotation('wrong')
tag = annotation('tag')
affirm = annotation('affirm')
answer = annotation('answer')

class Question(object):
    def __repr__(self):
        return repr(type(self)) + ':\n' + self.question +'\n    ' + self.correct + '\n'

class OutputQuestion(Question):
    @classmethod
    def convert_or_passthrough(cls, thing):
        if isinstance(thing, Question):
            return thing
        else:
            return cls.from_func(thing)
    @classmethod
    def from_func(cls, func):
        lines = inspect.getsourcelines(func)[0]
        while lines[0].startswith('@'):
            lines.pop(0)
        text = ''.join(lines)
        answer = repr(func())
        q = cls(text, answer)
        for kind in annotations:
            if hasattr(func, kind):
                if not hasattr(q, kind):
                    setattr(q, kind, [])
                getattr(q, kind).extend(getattr(func, kind))
        return q
    def __init__(self, question, correct):
        self.question = question
        self.correct = correct

question = OutputQuestion.from_func


@source('http://docs.python.org/2/reference/datamodel.html')
@tag('addition')
def addition():
    """Adding two numbers """
    return 1 + 1

print addition

class MultipleChoice(Question):
    def __init__(self, question, correct, *wrong):
        self.question = question
        self.correct = correct
        self.answers = (correct,) + wrong


q = MultipleChoice('What does _ do at the interactive prompt?',
                   'Refers to the last non-None answer printed'
                   'Counter for how many times you hit enter',
                   'Something stupid'
                   )
q.affirmation = ("_ refers to the last non-None answer returned in the REPL, but isn't "
                 "special in executed programs. It's conventionally used to refer to "
                 "variables that aren't going to be used again.")


