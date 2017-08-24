import random

POPULATION_START = 1000

print("Welcome to the Gopher Population Simulator!")
print("Starting population: {}\n".format(POPULATION_START))

year = 1
population = POPULATION_START
for i in range(0,5):
    births = (random.randrange(100, 200) / 1000) * population
    deaths = (random.randrange(50, 250) / 1000) * population
    population = population + int(births)
    population = population - int(deaths)
    print("Year {}\n*****\n{} gophers were born. {} died.\nPopulation: {}\n".format(year, int(births), int(deaths), population))
    year += 1