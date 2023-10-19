import beehive

def main():
    hive = beehive.Hive()
    averageList = []
    hive.generate()

    for n in range(100):
        if n % 10 == 0:
            hive.mutate()
        hive.evaluate()
        fit = hive.repopulate()
        average = hive.average(fit)
        averageList.append(average)

        fitList = []
        for x in hive.bees:
            fitList.append(x.fitness)

    hive.visualizeBestPath()
    hive.visualizeAverageGeneration(averageList)
    hive.visualizeBestBee()

main()

""" Calcul de temps d'execution """

# if __name__ == "__main__":
#     import cProfile, pstats
#     profiler = cProfile.Profile()
#     profiler.enable()
#     main()
#     profiler.disable()
#     stats = pstats.Stats(profiler).sort_stats('cumtime').print_stats(20)