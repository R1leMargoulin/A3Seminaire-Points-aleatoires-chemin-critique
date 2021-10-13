import random

#Objet pour placer nos points
class Point:
    def __init__(self, coordx, coordy, coordz):
        self.x = coordx
        self.y = coordy
        self.z = coordz


#cette fonction créé une liste de 10 points aléatoire avec les doordonnees entre -20 et 20
def randomNumbers(n):
    table = []
    for i in range(n):
        table.append(Point(random.uniform(-20, 20), random.uniform(-20, 20), random.uniform(-20, 20)))
    return table



if __name__ == '__main__':
    mespoints = randomNumbers(10)
    for point in mespoints:
        print(point.x, ",", point.y, ",", point.z, "\n") 
#        print (mespoints.index(point))