import sexpdata as sp
from math import fabs, sqrt, log2, e


class TreeExpression(object):
    def __init__(self):
        self.expr = None
        self.children = []
        self.height = 0

    def from_s_expression(self, parsed_expr):
        if type(parsed_expr) == list:
            self.expr = sp.dumps(parsed_expr[0])
            child_heights = []
            for elem in parsed_expr[1:]:
                child = TreeExpression().from_s_expression(elem)
                child_heights.append(child.height)
                self.children.append(child)
            self.height += max(child_heights) + 1
        else:
            self.expr = parsed_expr
            self.children = None
        return self

    def evaluate_expression(self, x):
        if self.children is None:
            return self.expr
        else:
            return self.eval_func(x, *[child.evaluate_expression(x) for child in self.children])

    def eval_func(self, x, *args):
        n = len(x)
        if self.expr == 'add':
            return args[0] + args[1]
        elif self.expr == 'sub':
            return args[0] - args[1]
        elif self.expr == 'mul':
            return args[0] * args[1]
        elif self.expr == 'div':
            return 0 if args[1] == 0 else args[0] / args[1]
        elif self.expr == 'pow':
            return args[0] ** args[1]
        elif self.expr == 'sqrt':
            return sqrt(args[0])
        elif self.expr == 'log':
            return log2(args[0])
        elif self.expr == 'exp':
            return e ** args[0]
        elif self.expr == 'max':
            return max(args)
        elif self.expr == 'ifleq':
            return args[2] if args[0] <= args[1] else args[3]
        elif self.expr == 'data':
            return x[args[0]]
        elif self.expr == 'diff':
            return x[args[0] % n] - x[args[1] % n]
        elif self.expr == 'avg':
            k = args[0] % n
            l = args[1] % n
            size = fabs(k - l)
            size = size if size != 0 else 1
            s = sum(x[min([k, l]): max([k, l])])
            return s / size
