import inspect as _inspect
from question import Question, Answer
from question import MultipleChoice, Checkbox, FillInTheBlank

def _text_from_func(func):
    lines = _deindent(_inspect.getsourcelines(func)[0])
    while lines[0].startswith('@'):
        lines.pop(0)
    text = ''.join(lines)
    return text

def _deindent(lines):
    indent = min(len(line) - len(line.lstrip()) for line in lines)
    return [line[indent:] for line in lines]

def question(func):
    return FillInTheBlank(_text_from_func(func), is_code=True, correct=Answer(repr(func()), is_expression=True))

def ask_all():
    for q in Question.all_questions:
        print 'from', q.file
        q.ask()
