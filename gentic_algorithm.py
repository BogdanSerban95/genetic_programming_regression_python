from individual import Individual


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
            ind = Individual()
            ind.random_init(self.max_height)
            ind.fitness = self.data.evaluate_expression(ind.expr)
            self.population.append(ind)

    def selection(self):
        pass

    def crossover(self, ind_x, ind_y):
        pass

    def run_ga(self):
        pass
