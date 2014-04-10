class Question(object):
    """Generic Question contructor

    Abstract base class - no instances should exist"""
    classes = []
    def __new__(cls, *args, **kwargs):
        if cls is Question:
            cls = [Q for Q in Question.classes
                   if kwargs.get('type', 'FillInTheBlank').lower() == Q.__name__.lower()][0]
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, question, answer=None, correct=None, wrong=None, type='FillInTheBlank', is_code=False):
        """
        >>> q = Question('Why did the chicken?', correct='because', wrong=['dunno', 'hmm...'])
        >>> len(q.answers)
        3
        >>> [a.text for a in q.answers]
        ['because', 'dunno', 'hmm...']
        """
        assert type.lower() == self.__class__.__name__.lower()
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
        self.answers = ([Answer.to_answer(a) for a in list_if_single(answer)] +
                        [Answer.to_correct_answer(a) for a in list_if_single(correct)] +
                        [Answer.to_wrong_answer(a) for a in list_if_single(wrong)])
    def ask(self):
        """ask question in console"""
        print self.question
        print '\n'.join("%d. %s" % (i, q.text) for i, q in zip(self.answers, xrange(1, 10000)))
        r = raw_input()
        if r.isdigit() and self.answers[int(r)-1].correct:
            print 'dingdingding - correct!'
        else:
            print 'bzzz! incorrect.'

class MultipleChoice(Question): pass
class Checkbox(Question): pass
class FillInTheBlank(Question): pass
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
        self.correct = correct
        self.is_code = is_code
    @property
    def wrong(self):
        return not self.correct






if __name__ == '__main__':
    import doctest
    doctest.testmod()
