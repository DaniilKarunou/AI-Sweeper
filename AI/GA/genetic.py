from random import random, choice
from abc import abstractmethod, ABC

class Element(ABC):

    @abstractmethod
    def __init__(self):
        self.fitness = self.evaluate_function()

    def mutation(self):
        self._perform_mutation()
        self.fitness = self.evaluate_function()

    @abstractmethod
    def _perform_mutation(self):
        pass

    @abstractmethod
    def crossover(self, element, start_end):
        pass

    @abstractmethod
    def evaluate_function(self):
        pass

from random import randint, sample

class Population(Element):
    def __init__(self, points):
        self.points = points
        super().__init__()

    def _perform_mutation(self):
        first = randint(1, len(self.points) - 2)
        second = randint(1, len(self.points) - 2)

        self.points[first], self.points[second] = self.points[second], self.points[first]

    def crossover(self, element, start_end):
        #child_points = self.points[1:int(len(self.points) / 2)]
        child_points = self.points[1:randint(2, len(self.points))]
        for point in element.points:
            if point not in child_points and point not in start_end:
                child_points.append(point)

            if len(child_points) == len(element.points):
                break
        return Population(start_end + child_points + start_end)

    def evaluate_function(self):
        sum = 0
        for i in range(len(self.points)-1):
            sum += self.calculate_distance(self.points[i][0], self.points[i+1][0], self.points[i][1], self.points[i+1][1])
        return sum

    def calculate_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def __repr__(self):
        return self.points

    def __str__(self):
        return str(self.points)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]

class GeneticAlgorithm():

    def __init__(self, gen_size, gen_limit, mutation_probability = 0.5):
        self.gen_size = gen_size
        self.mutation_probability = mutation_probability
        self.gen_limit = gen_limit


    def selection(self, generation):
        max_selected = int(len(generation) / self.gen_size)
        sorted_by_assess = sorted(generation, key=lambda x: x.fitness)
        return sorted_by_assess[:max_selected]

    def first_population(self, start_end, points):
        return [Population(start_end + sample(points, len(points)) + start_end) for _ in range(self.gen_size)]

    def run(self, start_end, points):
        population = self.first_population(start_end, points)
        population.sort(key=lambda x: x.fitness)
        population_len = len(population)
        fitnesses = []
        i = 0
        while True:
            selected = self.selection(population)
            new_population = selected.copy()
            while len(new_population) != population_len:
                child = choice(population).crossover(choice(population), start_end)
                if random() <= self.mutation_probability:
                    child.mutation()
                new_population.append(child)

            population = new_population
            the_best_match = min(population, key=lambda x: x.fitness)
            i += 1
            print(f"Generation: {i} S: {str(the_best_match)} fitness: {the_best_match.fitness}")

            fitnesses.append(the_best_match.fitness)
            if self.stop_condition(fitnesses, i, self.gen_limit):
                return the_best_match

    def stop_condition(self, fitnesses, generation, gen_limit):
        if len(fitnesses) == 3000:
            if len(set(fitnesses)) == 1 or generation == gen_limit:
                print("Stopped at generation {}".format(generation))
                return True
            else:
                fitnesses.clear()
        return False