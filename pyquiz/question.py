import inspect
import random
import re
from jinja2 import Markup

#TODO refactor conversion code (passthroughs, changing question type)

class Question(object):
    """Generic Question contructor

    Abstract base class - no instances of this class should be constructed"""
    classes = []
    all_questions = []
    def __new__(cls, *args, **kwargs):
        if cls is Question:
            cls = [Q for Q in Question.classes
                   if kwargs.get('type', 'FillInTheBlank').lower() == Q.__name__.lower()][0]
        q = object.__new__(cls, *args, **kwargs)
        if not hasattr(q, 'file'):
            q.file = _get_module()
        Question.all_questions.append(q)
        return q

    @property
    def id(self):
        return Question.all_questions.index(self)

    def unregister(self):
        Question.all_questions.remove(self)

    def __init__(self, question, answer=None, correct=None, wrong=None, type='FillInTheBlank', is_code=False, answers_are_code=False):
        """
        >>> q = Question('Why did the chicken?', correct='because', wrong=['dunno', 'hmm...'])
        >>> len(q.answers)
        3
        >>> [a.text for a in q.answers]
        ['because', 'dunno', 'hmm...']
        """
        # type actually happens during __new__, so assert
        assert type.lower() == self.__class__.__name__.lower(), str(type.lower()) + ' vs ' + str(self.__class__.__name__.lower())
        def list_if_single(arg):
            if arg is None:
                return []
            if isinstance(arg, basestring):
                return [arg]
            try:
                iter(arg)
            except TypeError:
                return [arg]
            return arg
        self.is_code = is_code
        self.question = question
        self.answers = ([Answer.to_answer(a) for a in list_if_single(answer)] +
                        [Answer.to_correct_answer(a) for a in list_if_single(correct)] +
                        [Answer.to_wrong_answer(a) for a in list_if_single(wrong)])
        if answers_are_code:
            for a in self.answers:
                a.is_code = True
    def ask(self):
        """ask question in console"""
        print self.question
        if len(self.answers) == 2 and set(['yes', 'no']) == set(a.text for a in self.answers):
            self.answers.sort(key=lambda x: x.text, reverse=True)
        else:
            random.shuffle(self.answers)
        print '\n'.join("%d)  %s" % (i, a.text) for i, a in zip(xrange(1,1000), self.answers))
        r = raw_input()
        if r.isdigit() and int(r) <= len(self.answers) and self.answers[int(r)-1].correct:
            print _green('dingdingding - correct!')
        elif any(_normalize(r) == _normalize(a.text) for a in self.answers if a.correct):
            print _green('dingdingding - correct!')
        elif len(self.answers) == 2 and set(['yes', 'no']) == set(a.text for a in self.answers):
            answer_is_yes = 'yes' == [a.text for a in self.answers if a.correct][0]
            if (answer_is_yes and 'y' in r.lower()) or not answer_is_yes:
                print _green('dingdingding - correct!')
            else:
                print _red('bzzz! incorrect.')
        else:
            print _red('bzzz! incorrect.')
    def html(self):
        return (Markup('<pre><code>') if self.is_code else '') + str(self.text) + (Markup('</pre></code>') if self.is_code else '')
    @property
    def text(self):
        return self.question
    @property
    def alpha_answers(self):
        return sorted(self.answers, key=lambda a: str(a.text))
    @property
    def correct_answers(self):
        return [a for a in self.answers if a.correct]
    @property
    def wrong_answers(self):
        return [a for a in self.answers if a.wrong]

class MultipleChoice(Question):
    def __init__(self, question, correct, *wrongs, **kwargs):
        Question.__init__(self, question, correct=correct, wrong=wrongs, type='multiplechoice', **kwargs)
class Checkbox(Question):
    def __init__(self, question, corrects, wrongs, **kwargs):
        Question.__init__(self, question, correct=corrects, wrong=wrongs, type='checkbox', **kwargs)
    def ask(self):
        """ask question in console"""
        print self.question
        random.shuffle(self.answers)
        for a in self.answers:
            print a.text
            r = raw_input('y/n ')
            if (('y' in r.lower() and a.correct) or not a.correct):
                print _green('dingdingding - correct!')
            else:
                print _red('bzzz! incorrect.')

def _normalize(s):
    return ''.join(re.sub(r'"', '"', s).split()).lower()

class FillInTheBlank(Question):
    def ask(self):
        """ask question in console"""
        print self.question
        r = raw_input('> ')
        if any(_normalize(r) == _normalize(a.text) for a in self.answers if a.correct):
            print _green('dingdingding - correct!')
        else:
            print _red('bzzz! incorrect.')
Question.classes.extend([MultipleChoice, Checkbox, FillInTheBlank])

class Answer(object):
    @classmethod
    def to_correct_answer(cls, answer):
        """
        >>> Answer.to_correct_answer('yep').correct
        True
        >>> Answer.to_correct_answer(Answer('blah', correct=False)).correct
        True
        """
        a = cls.to_answer(answer)
        a.correct = True
        return a
    @classmethod
    def to_wrong_answer(cls, answer):
        """
        >>> Answer.to_wrong_answer('yep').correct
        False
        >>> Answer.to_wrong_answer(Answer('blah', correct=False)).correct
        False
        """
        a = cls.to_answer(answer)
        a.correct = False
        return a
    @classmethod
    def to_answer(cls, answer):
        """
        >>> Answer.to_answer('yep').correct
        True
        >>> Answer.to_answer(Answer('blah', correct=False)).correct
        False
        """
        if isinstance(answer, cls):
            return answer
        else:
            return Answer(answer, correct=True)
    def __init__(self, text, correct=True, is_code=False):
        self.text = text
        assert isinstance(self.text, str), self.text
        self.correct = correct
        self.is_code = is_code
    @property
    def wrong(self):
        return not self.correct
    def html(self):
        if '\n' in str(self.text):
            return (Markup('<pre><code>') if self.is_code else '') + str(self.text) + (Markup('</pre></code>') if self.is_code else '')
        else:
            return (Markup('<code>') if self.is_code else '') + str(self.text) + (Markup('</code>') if self.is_code else '')

def _get_module(a=1):
    s = inspect.stack()
    return s[1][1]

def _green(s):
    return '\x1b[32m%s\x1b[39m' % (s,)
def _red(s):
    return '\x1b[31m%s\x1b[39m' % (s,)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
