from jinja2 import Environment, FileSystemLoader

from questions import Question
import intro

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('quiz.html')


s = template.render(questions=Question.questions)

f = open('test.html', 'w')

f.write(s)

f.close()

