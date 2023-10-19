import random
import math
import pandas as pd
import matplotlib.pyplot as plt

class Bee:
	
	def __init__(self):
		self.flowerList = []
		self.fitness = 0

	def csvParse(self):
		df = pd.read_csv('Resources\Flowers.csv', header=0)
		return [(x, y) for x, y in zip(df['x'], df['y'])]

	def random(self):
		df = self.csvParse()
		random.shuffle(df)
		self.flowerList = [(x, y) for x, y in df]
		self.move()

	def setFlowerList(self, flower:list):
		self.flowerList = flower
		self.move()

	def move(self):
		for i in range(len(self.flowerList)):
			x1, y1 = self.flowerList[i]
			x2, y2 = self.flowerList[(i+1) % len(self.flowerList)]
			self.fitness += int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))



class Hive:

	def __init__(self) -> None:
		self.beeList = []
		self.bestBees = []
		self.bees = []
		self.childList = []

	def generate(self):
		for i in range(100):
			bee = Bee()
			bee.random()
			self.bees.append(bee)
			self.beeList.append(bee.fitness)

	def generateChild(self, flowerlist1, flowerlist2):
		babyBee1 = Bee()
		babyBee2 = Bee()
		babyBee1.flowerList = flowerlist1
		babyBee2.flowerList = flowerlist2
		babyBee1.move()
		babyBee2.move()
		return babyBee1, babyBee2

	def evaluate(self):
		sortedList = sorted(self.bees, key=lambda x: x.fitness)
		self.bees = sortedList[:50]
		self.bestBees.append(self.bees[0].fitness)

	def repopulate(self):

		usableBees = self.bees.copy()
		for i in range(25):
			randomBee1 = random.choice(usableBees)
			usableBees.remove(randomBee1)
			randomBee2 = random.choice(usableBees)
			usableBees.remove(randomBee2)

			parent1half1 = randomBee1.flowerList[:len(randomBee1.flowerList)//2]
			parent1half2 = [x for x in randomBee2.flowerList if x not in parent1half1]
			parent2half1 = randomBee2.flowerList[:len(randomBee2.flowerList)//2]
			parent2half2 = [x for x in randomBee1.flowerList if x not in parent2half1]

			mergedList = parent1half1 + parent1half2
			mergedList2 = parent2half1 + parent2half2

			babyBee1, babyBee2 = self.generateChild(mergedList, mergedList2)

			self.childList.append(babyBee1)
			self.childList.append(babyBee2)

		self.bees = self.bees + self.childList
		self.beeList = self.bees + self.childList
		self.childList = []

		fitnessList = []
		fitnessList = [x.fitness for x in self.bees]
		return fitnessList

	def mutate(self):
		randomBee = random.choice(self.bees)
		for i in range(5):
			randomFlowerIndex = random.randint(0, len(randomBee.flowerList)-1)
			firstHalf = randomBee.flowerList[:randomFlowerIndex]
			secondHalf = randomBee.flowerList[randomFlowerIndex:]
			randomBee.flowerList = secondHalf + firstHalf

	def average(self, lst):
		sum_of_list = 0
		for i in range(len(lst)):
			sum_of_list += lst[i]
		average = sum_of_list/len(lst)
		return average

	def visualizeBestPath(self):
		plt.scatter(*zip(*self.bees[0].flowerList), color='blue')
		plt.ylabel('y')
		plt.xlabel('x')
		plt.title(f"Best bee's path")
		plt.plot(*zip(*self.bees[0].flowerList), linestyle='--', color='red')
		plt.show()
	
	def visualizeBestBee(self):
		plt.plot(self.bestBees)
		plt.ylabel('Fitness')
		plt.xlabel('Bee')
		plt.title(f"Best bee fitness per generation")
		plt.show()

	def visualizeAverageGeneration(self, fitnessList):
		plt.plot(fitnessList)
		plt.ylabel('Average fitness')
		plt.xlabel('Generation')
		plt.title(f"Average fitness per generation")
		plt.show()