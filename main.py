import sexpdata as spd
from s_exp_evaluator import SExpressionEvaluator
import argparse


def main():
    exp_eval = SExpressionEvaluator()
    parser = argparse.ArgumentParser(description='Genetic programming.')
    parser.add_argument('-question', help='Question number', type=int, required=True)
    parser.add_argument('-n', type=int)
    parser.add_argument('-x', type=str)
    parser.add_argument('-expr', type=str)

    args = parser.parse_args()
    question = args.question

    if question == 1:
        x = [float(i) for i in args.x.split(' ')]
        expr = spd.loads(args.expr)
        print(exp_eval.evaluate(x, expr))


if __name__ == '__main__':
    main()
