import beehive

hive = beehive.Hive()

def main():
    averageList = []
    # Generate a new hive
    hive.generate()
    for n in range(25):
        if n % 10 == 0:
            hive.mutate()
        hive.evaluate()
        fit = hive.repopulate()
        average = hive.average(fit)
        averageList.append(average)
        # print(f"average value: {average}")

        fitList = []
        for x in hive.bees:
            fitList.append(x.fitness)
        # print(f" bee's fit: {sorted(fitList)}")
    hive.visualizeBestPath()
    # print(f"fit value: {fit}")
    hive.visualizeAverageGeneration(averageList)
    hive.visualizeBestBee()

if __name__ == "__main__":
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime').print_stats(20)