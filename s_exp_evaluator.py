import sexpdata as sd
import math


class SExpressionEvaluator(object):
    def evaluate(self, x, expr, *args):
        if type(expr) == list:
            return self.eval_func(x, expr[0], *[self.evaluate(x, e) for e in expr[1:]])
        else:
            return expr

    def eval_func(self, x, exp, *args):
        expression = sd.dumps(exp)
        n = len(x)
        if expression == 'add':
            return args[0] + args[1]
        elif expression == 'sub':
            return args[0] - args[1]
        elif expression == 'mul':
            return args[0] * args[1]
        elif expression == 'div':
            return 0 if args[1] == 0 else args[0] / args[1]
        elif expression == 'pow':
            return args[0] ** args[1]
        elif expression == 'sqrt':
            return math.sqrt(args[0])
        elif expression == 'log':
            return math.log2(args[0])
        elif expression == 'exp':
            return math.e ** args[0]
        elif expression == 'max':
            return max(args)
        elif expression == 'ifleq':
            return args[2] if args[0] <= args[1] else args[3]
        elif expression == 'data':
            return x[args[0]]
        elif expression == 'diff':
            return x[args[0] % n] - x[args[1] % n]
        elif expression == 'avg':
            k = args[0] % n
            l = args[1] % n
            size = math.fabs(k - l)
            size = size if size != 0 else 1
            s = sum(x[min([k, l]): max([k, l])])
            return s / size
