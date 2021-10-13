import Points
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#fonction pour optimiser selon la distance des points avec la distance la plus courte.
def optiTrajet(pointDeDepart, points):
    actualpoint = pointDeDepart
    trajetOpti = []
    #On repete jusqu'a ne plus avoir de points dans le tableau, on est donc sur de faire tpus les points
    while len(points)>0:
        distanceMin = 10000
        indice = 0
    #On calcule la distance de chaque points et on ajoute le point le plus proche dans notre trajet opti tout en l'enlevant du premier tableau        
        for point in points:
            distance = math.sqrt((point.x - actualpoint.x)**2 + (point.y - actualpoint.y)**2 + (point.z - actualpoint.z)**2)
            if (distance <= distanceMin):
                distanceMin = distance
                indice = points.index(point)
        trajetOpti.append(points[indice])
        del points[indice]
    return trajetOpti


def Representer3D(points):
    x = [] #liste de points coordx
    y = [] #liste de points coordy
    z = [] #liste de points coordz
    plt.rcParams["figure.figsize"] = [10.50, 10.50] #parametres de la fenetre
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure() #fait pop la fenetre
    for point in points:
        ax = fig.add_subplot(projection="3d") #ajout de la figure encore vide
        if (points.index(point) == len(points)-1): #mise en place de limites pour ne pas depasser le tableau de points
            break
        x.append(point.x)
        x.append(points[points.index(point)+1].x) #ajout du point xi et x(i+1)
        y.append(point.y)
        y.append(points[points.index(point)+1].y) #ajout du point yi et y(i+1)
        z.append(point.z)
        z.append(points[points.index(point)+1].z)#ajout du point zi et z(i+1)
        #print(ax.plot)
    ax.scatter(x, y, z, c='red', s=100) #ajout des points rouge en surbrillance par rapport aux listes xyz
    ax.plot(x, y, z, color='black') #ajout des segments entre les points par rapport aux listes xyz       
    plt.show() #ajoute les modifs sur la figure
        




if __name__ == '__main__':
    mespoints = optiTrajet(Points.Point(0, 0, 0) , Points.randomNumbers(10)) #optitrajet sur 10 points aléatoires
    Representer3D(mespoints) #lancer la représentation 3D



#fonction de reference pour le graph 3D
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
#fig = plt.figure()
#ax = fig.add_subplot(projection="3d")
#x, y, z = [1, 1.5], [1, 2.4], [3.4, 1.4]
#ax.scatter(x, y, z, c='red', s=100)
#ax.plot(x, y, z, color='black')
#plt.show()