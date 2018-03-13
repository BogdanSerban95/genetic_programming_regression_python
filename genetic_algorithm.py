from tree_expr import TreeExpression
import random as rnd
import copy


class GeneticAlgorithm(object):
    def __init__(self, lmbd, n, m, k, chi, max_height, time_budget, data):
        self.pop_size = lmbd
        self.n = n
        self.m = m
        self.k = k
        self.chi = chi
        self.data = data
        self.population = []
        self.max_height = max_height
        self.time_budget = time_budget

    def generate_population(self):
        for i in range(self.pop_size):
            ind = TreeExpression().random_init(self.max_height)
            ind.fitness = self.data.evaluate_expression(ind)
            self.population.append(ind)

    def selection(self):
        pass

    def crossover(self, ind_x, ind_y):
        # find a common branch
        offspring_x = copy.deepcopy(ind_x)
        offspring_y = copy.deepcopy(ind_y)
        branches_x, branches_y = self.get_common_branches(offspring_x, offspring_y)
        # switch between them
        switch_root_idx = rnd.randint(0, len(branches_x) - 1)
        switch_child_idx = rnd.randint(0, min(
            [
                len(branches_x[switch_root_idx].children),
                len(branches_y[switch_root_idx].children)
            ]) - 1)
        aux = branches_x[switch_root_idx].children[switch_child_idx]
        branches_x[switch_root_idx].children[switch_child_idx] = branches_y[switch_root_idx].children[switch_child_idx]
        branches_y[switch_root_idx].children[switch_child_idx] = aux
        return offspring_x

    def get_common_branches(self, x, y):
        common_x = [x]
        common_y = [y]
        if x.children is None or y.children is None:
            return [], []

        if len(x.children) == len(y.children):
            for i in range(len(x.children)):
                c_x, c_y = self.get_common_branches(x.children[i], y.children[i])
                common_x.extend(c_x)
                common_y.extend(c_y)
        return common_x, common_y

    def run_ga(self):
        pass
