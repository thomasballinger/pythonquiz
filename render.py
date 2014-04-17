from jinja2 import Environment, FileSystemLoader

from question import Question
import intro

env = Environment(loader=FileSystemLoader('.'), autoescape=True)

template = env.get_template('quiz.html')


s = template.render(questions=Question.all_questions)

f = open('test.html', 'w')

f.write(s)

f.close()

