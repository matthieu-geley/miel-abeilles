# Le miel et les abeilles

## Un arbre, des fleurs et des abeilles

    Une colonie d’abeilles a construit sa ruche dans un arbre, qui trône au beau milieu d’un champ de fleurs. A son arrivée dans l'arbre, la colonie était constituée de 101 abeilles, dont leur reine.
    Afin de se nourrir, leur reine et leurs larves, les abeilles doivent quitter la ruche en quête de pollen. Un champ de fleurs mellifères se trouvant tout autour de l’arbre, trouver le nectar nécessaire ne devrait pas être un souci. Ne connaissant pas ce nouveau territoire, les abeilles vont partir au hasard au travers du champ, butiner chacune des fleurs, avant de retourner à la ruche.
    La reine de la ruche, étant connue pour son envie de prospérer et son élitisme, souhaite améliorer, au fil du temps, l'efficacité de sa colonie.
    Les abeilles ayant butiné l’ensemble des pissenlits et des sauges le plus rapidement, devront s’accoupler et transmettre leur connaissance du champ de fleurs à leurs enfants. 
    Les abeilles les plus lentes seront remplacées par les nouvelles afin de maintenir la colonie à 100 individus et une reine.

## Une ruche en plein essor

    A l’aide d’un algorithme génétique, représentez informatiquement l'évolution des connaissances du champ de fleurs au fil des générations.
    Le paramétrage final de l’algorithme devra être justifié par des comparaisons entre différents paramétrages (mutation rate, mutation rate fixe ou évolutif, taux de reproduction, système de reproduction, métrique du calcul de fitness, ...).

## La reine est fière de ses abeilles

    Pas peu fière des résultats obtenus par sa méthode de sélection naturelle, Maya, la reine des abeilles, souhaite pouvoir visualiser et présenter ses résultats.
    Vous devrez donc ajouter la possibilité de générer un graphe de points (représentants les positions des fleurs) reliés les uns aux autres afin de représenter le chemin de la meilleure abeille de la dernière génération étudiée.
    Affichez son arbre généalogique. Vous devez aussi générer un graphe représentant l'évolution du temps de parcours moyen d’une génération d’abeille au cours du temps.

## Algorithme

    L’algorithme génétique utilisé est le suivant :
        1. Générer une population d’abeilles aléatoirement
        2. Evaluer la fitness de chaque abeille
        3. Sélectionner les abeilles les plus performantes
        4. Générer une nouvelle population d’abeilles à partir des abeilles sélectionnées
        5. Faire la mutation d'une partie de la population toutes
        6. Répéter les étapes 2 à 5 jusqu’à ce qu’une condition d’arrêt soit atteinte

## Structure du code

    Le code est composé de deux fichiers et un dossier contenant les données ressources :

- `main.py` : contient le code de lancement principal

- `beehive.py` : contient la classe *Bee* et la classe *Hive*

- dossier `Resources` : contient le fichier *Flowers*.csv contenant les données des fleurs

## Comment lancer le code

    Pour lancer le code, il faut en premier lieu installer les dépendances nécessaires au bon fonctionnement du code. Pour cela, il faut exécuter la commande suivante dans le terminal :

```
pip install -r requirements.txt
```

    Ensuite, il vous faut ouvrir le fichier `main.py` et modifier les paramètres de l'algorithme génétique. Les paramètres sont les suivants :

- range(**int**) : nombre de générations ligne 9

- n % (**int**) : fréquence de mutation ligne 10

    Pour finir exécuter le fichier `main.py` dans le terminal :

```
Python3 main.py
```

Here are some ways you could optimize the bee colony optimization code:

- Use Numpy vectors and operations instead of basic Python lists and loops where possible. This will speed up things like calculating distances.

- Limit copying of lists. For example, in `repopulate()`, you could generate the child bee lists in place rather than making copies. 

- Reduce overall complexity. Some parts like `move()` seem more complex than needed. You may be able to simplify the logic.

- Add flexibility for parameters like population size, number of generations, etc to be set as inputs rather than hardcoding.

- Use memoization to cache computed fitness values rather than recomputing.

- Parallelize fitness evaluation and breeding steps across bees.

- Optimize data layout to improve locality and cache utilization. For example store flowers and bees in separate contiguous arrays.

- Profile the code to identify hot spots and focus optimization there. 

- Consider moving the expensive inner loops like fitness evaluation to compiled code (C/C++ extension or Numba) rather than plain Python.

- Use more efficient data structures like Sets vs Lists in some places.

- Reduce number of copies made, reuse objects where possible.

So in summary, leverage Numpy, reduce complexity, parallelize, use memoization and caching, profile and optimize hotspots, and consider moving inner loops to compiled code. That should help significantly speed up the implementation.

Based on a quick analysis of the bee colony optimization code you provided:

The overall big O is dominated by the `repopulate()` method, which is O(n^2) due to the nested loops over the bees lists to select random parents and generate offspring.

Specifically:

- `generate()` is O(n) where n is the population size. Simple loop to generate bees.

- `move()` is O(n) where n is number of flowers. Calculates fitness.

- `evaluate()` is O(n log n) due to sorting the bees by fitness.

- `repopulate()` is O(n^2) as explained above. Two nested loops over bees.

- `mutate()` is O(1). Mutates a single random bee.

- `average()` is O(n) to calculate average fitness.

- `visualize_best_bee()` is O(n) to plot bee path. 

- `visualize_average_generation()` is O(n) to plot fitness over generations.

So the repopulation step dominates with O(n^2) complexity. The overall algorithm is likely running in O(g * n^2) time where g is the number of generations.

Some ways to improve this:

- Use a more efficient parent selection and breeding approach.

- Parallelize the loops to reduce effective time complexity.

- Reduce number of generations g.

- Limit population size n per generation.
