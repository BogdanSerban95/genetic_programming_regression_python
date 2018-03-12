import sexpdata as spd
from s_exp_evaluator import SExpressionEvaluator
import argparse
from data_holder import DataHolder


def main():
    exp_eval = SExpressionEvaluator()
    parser = argparse.ArgumentParser(description='Genetic programming.')
    parser.add_argument('-question', help='Question number', type=int, required=True)
    parser.add_argument('-n', type=int)
    parser.add_argument('-m', type=int)
    parser.add_argument('-x', type=str)
    parser.add_argument('-expr', type=str)
    parser.add_argument('-data', type=str)

    args = parser.parse_args()
    question = args.question

    if question == 1:
        x = [float(i) for i in args.x.split(' ')]
        expr = spd.loads(args.expr)
        print(exp_eval.evaluate(x, expr))
    elif question == 2:
        data_holder = DataHolder()
        data_holder.load_data(args.data)
        expr = spd.loads(args.expr)
        print(compute_mse(expr, data_holder.x, data_holder.y, args.m))


def compute_mse(exp, x, y, m):
    se_sum = 0
    exp_eval = SExpressionEvaluator()
    for i in range(m):
        exp_val = exp_eval.evaluate(x[i], exp)
        print(exp_val, type(exp_val))
        se_sum += (y[i] - exp_val) ** 2
    return se_sum / m


if __name__ == '__main__':
    main()
