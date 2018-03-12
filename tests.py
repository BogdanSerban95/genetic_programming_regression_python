import sexpdata as sd
from individual import Individual
from tree_expr import TreeExpression

a = sd.loads('(add (max (data 0) (data 1)) 2.1)')
x = [1.1, 2.3]
expr = TreeExpression().from_s_expression(a)
print(expr.evaluate_expression(x))
# eval = SExpressionEvaluator()
# print(eval.evaluate([1,2,3,4], a))
pass
# print(Individual().random_init(self.max_height))
