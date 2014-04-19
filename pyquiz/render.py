
from jinja2 import Environment, PackageLoader

from pyquiz.question import Question

import imp


def render(output, *filenames):

    for fn in filenames:
        imp.load_source('', fn)

    env = Environment(loader=PackageLoader('pyquiz', 'templates'), autoescape=True)
    template = env.get_template('quiz.html')
    s = template.render(questions=Question.all_questions)

    with open(output, 'w') as f:
        f.write(s)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('modules', nargs='+', help='names of modules to import for questions')
    parser.add_argument('-o', '--output', action='store', help='name of output file')
    args = parser.parse_args()
    render(args.output, *args.modules)

if __name__ == '__main__':
    main()
