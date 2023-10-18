import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Bee:

	def __init__(self, id=0):
		self.id = id
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
		self.population = 0 #nombre d'abeilles
		self.beeList = [] #liste des abeilles
		self.bestBees = []
		self.bees = [] #liste des abeilles
		self.childList = [] #liste des abeilles enfants

	def generate(self):
		for i in range(100):
			bee = Bee(i)
			bee.random()
			self.bees.append(bee)
			self.beeList.append((bee.id, bee.fitness))

	def generateChild(self, flowerlist1, flowerlist2):
		babyBee1 = Bee(self.population) #création d'une première abeille enfant
		self.population += 1 #ajoute 1 à la population
		babyBee2 = Bee(self.population) #création d'une deuxième abeille enfant
		self.population += 1 #ajoute 1 à la population
		babyBee1.flowerList = flowerlist1
		babyBee2.flowerList = flowerlist2
		babyBee1.move()
		babyBee2.move()
		return babyBee1, babyBee2

	def evaluate(self):
		sortedList = sorted(self.bees, key=lambda x: x.fitness) #trie la liste par score fitness
		# print(f"sorted List: {sortedList}") #affiche le score fitness de la meilleure abeille
		self.bees = sortedList[:50]
		self.bestBees.append(self.bees[0].fitness)

	def repopulate(self): #croisement des abeilles

		usableBees = self.bees.copy() #liste des abeilles utilisable
		for i in range(25): #boucle pour chaque abeille de la liste restante
			randomBee1 = random.choice(usableBees) #choix d'une abeille au hasard (parent 1)
			usableBees.remove(randomBee1) #ajoute l'abeille à la liste des abeilles utilisées
			randomBee2 = random.choice(usableBees) #choix d'une abeille au hasard (parent 2)
			usableBees.remove(randomBee2) #ajoute l'abeille à la liste des abeilles utilisées

			p1h1 = randomBee1.flowerList[:len(randomBee1.flowerList)//2] #première moitié du parent 1
			p1h2 = [x for x in randomBee2.flowerList if x not in p1h1] #deuxième moitié du parent 1
			p2h1 = randomBee2.flowerList[:len(randomBee2.flowerList)//2] #première moitié du parent 2
			p2h2 = [x for x in randomBee1.flowerList if x not in p2h1] #deuxième moitié du parent 2

			mergedList = p1h1 + p1h2 #fusion des deux moitiés
			# print(f"merged list: {mergedList}")
			# print(f"merged list len: {len(mergedList)}")
			# break
			mergedList2 = p2h1 + p2h2 #fusion des deux moitiés

			babyBee1, babyBee2 = self.generateChild(mergedList, mergedList2) #ajoute la liste fusionnée à l'abeille

			self.childList.append(babyBee1) #ajoute l'id et le score fitness de l'abeille enfant 1 dans la liste
			self.childList.append(babyBee2) #ajoute l'id et le score fitness de l'abeille enfant 2 dans la liste

		# print(f"bee's: {self.bees}") #affiche la liste des abeilles enfants
		self.bees = self.bees + self.childList #ajoute les abeilles enfants à la liste des abeilles
		self.beeList = self.bees + self.childList #ajoute les abeilles utilisées et les abeilles enfants à la liste des abeilles
		self.childList = []

		fitnessList = []
		fitnessList = [x.fitness for x in self.bees]
		return fitnessList

	def mutate(self):
		randomBee = random.choice(self.bees) #choix d'une abeille au hasard
		for i in range(5):
			randomFlowerIndex = random.randint(0, len(randomBee.flowerList)-1) #choix d'une fleur au hasard
			firstHalf = randomBee.flowerList[:randomFlowerIndex] #première moitié de la liste
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
		# print(f"best bee: {len(self.bees[0].flowerList)}")
		# print(f"best bee: {self.bees[0].flowerList}")
		plt.ylabel('y')
		plt.xlabel('x')
		plt.title(f"Best bee's path")
		plt.plot(*zip(*self.bees[0].flowerList), linestyle='--', color='red')
		plt.show()
	
	def visualizeBestBee(self):
		"""best bee fitness per generation"""
		plt.plot(self.bestBees)
		plt.ylabel('Fitness')
		plt.xlabel('Bee')
		plt.title(f"Best bee fitness per generation")
		plt.show()

	def visualizeAverageGeneration(self, fitnessList):
		plt.plot(fitnessList)
		print(fitnessList)
		print(len(fitnessList))
		plt.ylabel('Average fitness')
		plt.xlabel('Generation')
		plt.title(f"Average fitness per generation")
		plt.show()