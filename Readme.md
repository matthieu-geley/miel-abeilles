# Le miel et les abeilles

## Un arbre, des fleurs et des abeilles

Une colonie d’abeilles a construit sa ruche dans un arbre, qui trône au beau milieu d’un champ de fleurs. A son arrivée dans l'arbre, la colonie était constituée de 101 abeilles, dont leur reine.
Afin de se nourrir, leur reine et leurs larves, les abeilles doivent quitter la ruche en quête de pollen. Un champ de fleurs mellifères se trouvant tout autour de l’arbre, trouver le nectar nécessaire ne devrait pas être un souci.
Ne connaissant pas ce nouveau territoire, les abeilles vont partir au hasard au travers du champ, butiner chacune des fleurs, avant de retourner à la ruche.
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

- range(**integrer**) : nombre de générations ligne 9

- n % (**integrer**) : fréquence de mutation ligne 10

Pour finir exécuter le fichier `main.py` dans le terminal :

```
Python3 main.py
```

## Algorithme et fonctionnement

L’algorithme utilisé dans ce projet est le suivant :

1. On **génère** une population d’abeilles aléatoirement, chaque abeille est une solution potentielle pour relier chaque point du champ de fleurs.

2. **Evaluation** du score de fitness de chaque abeille en calculant la distance totale parcourue par l’abeille.

3. **Sélection** des abeilles les plus performantes afin de les faire se reproduire.

4. **Reproduction** des abeilles sélectionnées afin de générer une nouvelle population d’abeilles.

5. Faire la **mutation** d'une partie de la population à intervalle régulier.

6. **Répéter** les étapes 2 à 5 jusqu’à ce qu’une condition d’arrêt soit atteinte.

    La condition d’arrêt actuel est le nombre de générations.

## Visualisation des résultats

### Parcours de la meilleure abeille de la dernière génération

![image](https://github.com/matthieu-geley/miel-abeilles/assets/115145423/8fa772ca-03db-4047-b77c-098ad325261e)

### Evolution de la distance parcourue en moyenne par une génération d’abeille au fil du temps

![image](https://github.com/matthieu-geley/miel-abeilles/assets/115145423/120907a8-710e-4398-9bc6-ab62ddbf624c)

### Evolution de la distance parcourue par la meilleur abeille au fil du temps

![image](https://github.com/matthieu-geley/miel-abeilles/assets/115145423/07b4935f-6f11-4612-924a-1d6cd06fda34)

## Conclusion

On peut voir que la distance parcourue par la meilleure abeille diminue au fil des générations.
On peut aussi voir que le temps de parcours moyen diminue au fil des générations.
On peut donc en conclure que les abeilles ont appris à parcourir le champ de fleurs de manière plus efficace.
