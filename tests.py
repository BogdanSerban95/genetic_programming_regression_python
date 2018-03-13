import sexpdata as sd
from tree_expr import TreeExpression
from genetic_algorithm import GeneticAlgorithm
from data_holder import DataHolder
import time

# a = sd.loads('(add (max (data 0) (data 1)) 2.1)')
# x = [1.1, 2.3]
# expr = TreeExpression().from_s_expression(a)
# print(expr.evaluate_expression(x))
# eval = SExpressionEvaluator()
# print(eval.evaluate([1,2,3,4], a))
# ind = TreeExpression()
# ind.random_init(4)
# print(str(ind))
# ga = GeneticAlgorithm(100, data.n, data.m, 2, 0, 3, 100, data)
# ga.generate_population()
# min_ind = TreeExpression()
# min_ind.fitness = 10000000000000000000000
# for ind in ga.population:
#     if min_ind.fitness > ind.fitness:
#         min_ind = ind
# print(min_ind.fitness)
# print(Individual().random_init(self.max_height))
# s = sd.loads('(min (max 2 3) (log (max 2 2)))')

data = DataHolder(1, 300)
data.load_data('data/data.txt')
ga = GeneticAlgorithm(10, 2, 3, 2, 1, 1, 1, data)
start_time = time.time()
ind = TreeExpression().random_init(5)
ind2 = TreeExpression().random_init(5)
offspring = ga.crossover(ind, ind2)
print(data.evaluate_expression(offspring))
print('Elapsed time: {}'.format(time.time() - start_time))
pass
