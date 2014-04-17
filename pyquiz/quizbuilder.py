import inspect as _inspect
import types
import StringIO
import sys
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
    """Make the function below a question, with what it returns as the answer"""
    return FillInTheBlank(_text_from_func(func), correct=Answer(repr(func()), is_code=True), is_code=True)

def yes(func):
    """The function below is a yes/no question, and the answer is yes"""
    return MultipleChoice(_text_from_func(func), Answer('yes'), Answer('no'), is_code=True)

def no(func):
    """The function below is a yes/no question, and the answer is no"""
    return MultipleChoice(_text_from_func(func), Answer('no'), Answer('yes'), is_code=True)

def true(func):
    """The function below is a True/False question, and the answer is True"""
    return MultipleChoice(_text_from_func(func), Answer('True'), Answer('False'), is_code=True)

def false(func):
    """The function below is a True/False question, and the answer is False"""
    return MultipleChoice(_text_from_func(func), Answer('False'), Answer('True'), is_code=True)

def yeahok(func):
    """Multiple choice question with just one answer: the right one"""
    return MultipleChoice(_text_from_func(func), Answer(repr(func()), is_code=True), is_code=True)

def wrong(answer, is_code=True):
    """Supplies a wrong answer for a multiple choice question"""
    if not isinstance(answer, basestring):
        answer = repr(answer)
    def dec(func):
        func = _multiple_choice_passthrough(func)
        func.answers.append(Answer(answer, correct=False, is_code=is_code))
        return func
    return dec

def display_answer(func):
    """Uses what is printed to stdout when the function is run as the correct answer"""
    ans = Answer(_stdout_output(func), correct=True, is_code=True)
    func = _fill_in_the_blank_passthrough(func)
    func.answers.append(ans)
    return func

class _RedirectStdout(object):
    def __enter__(self):
        self.orig_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
        return sys.stdout
    def __exit__(self, *args):
        sys.stdout = self.orig_stdout

def _stdout_output(func):
    with _RedirectStdout() as f:
        func()
    f.seek(0)
    s = f.read()
    if s.endswith('\n'):
        s = s[:-1]
    return s

def _multiple_choice_passthrough(func):
    if isinstance(func, types.FunctionType):
        return MultipleChoice(_text_from_func(func), correct=Answer(repr(func()), is_code=True), is_code=True)
    return func

def _fill_in_the_blank_passthrough(func):
    if isinstance(func, types.FunctionType):
        return FillInTheBlank(_text_from_func(func), correct=Answer(repr(func()), is_code=True), is_code=True)
    return func

def _checkbox_passthrough(func):
    if isinstance(func, types.FunctionType):
        return FillInTheBlank(_text_from_func(func), corrects=Answer(repr(func()), is_code=True), is_code=True)
    return func

def ask_all():
    """Ask all questions in the console"""
    for q in Question.all_questions:
        print 'from', q.file
        q.ask()
