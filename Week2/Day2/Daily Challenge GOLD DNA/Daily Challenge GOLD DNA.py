import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def flip(self):
        self.value = 1 - self.value

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to flip each gene
                gene.flip()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        return any(chromosome.is_all_ones() for chromosome in self.chromosomes)

class Organism:
    def __init__(self, dna, mutation_probability):
        self.dna = dna
        self.mutation_probability = mutation_probability

    def mutate(self):
        if random.random() < self.mutation_probability:
            self.dna.mutate()

# Simulation
mutation_probability = 0.001  # Adjust mutation probability as desired
generation = 0
population = [Organism(DNA(), mutation_probability) for _ in range(100)]  # Initial population size

while True:
    generation += 1
    for organism in population:
        organism.mutate()
        if organism.dna.is_all_ones():
            print(f"Generation {generation}: Found organism with all ones DNA.")
            exit()