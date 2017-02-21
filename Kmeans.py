

from __future__ import division
import math
import random
import csv

data = []

with open('data.csv') as csvfile:
  dbreader = csv.reader(csvfile, delimiter=',')
  for row in dbreader:
    data.append(tuple(map(lambda x: float(x), row)))

print("dataset loaded")


def euclidian_dist(coordinate_A, coordinate_B):
    return math.sqrt((coordinate_B[1]-coordinate_A[1])**2+(coordinate_B[0]-coordinate_A[0])**2)

def assign_initial_centroids(k, data):
    return random.sample(data, k)

def assign_tuples_to_clusters(centroids, data):
    clusters = [[] for i in range(len(centroids))]
    for coordinate in data:
        distances = [euclidian_dist(coordinate, centroid) for centroid in centroids]
        clusters[distances.index(min(distances))].append(coordinate)
    return clusters

def derive_centroids_for_clusters(clusters):
    new_centroids = []
    for cluster in clusters:
        X_coordinates, Y_coordinates = zip(*cluster)
        new_centroids.append((sum(X_coordinates)/len(X_coordinates),sum(Y_coordinates)/len(Y_coordinates)))
    return new_centroids

def kmeans_cluster(k, data):
    current_centroids = assign_initial_centroids(k, data)
    print("***Current centroids***")
    print(current_centroids)
    current_clusters = assign_tuples_to_clusters(current_centroids, data)
    print("***Current clusters***")
    print(current_clusters)
    new_centroids = derive_centroids_for_clusters(current_clusters)
    print("***New Centroids***")
    print(new_centroids)

    while sorted(current_centroids, key=lambda tup: (tup[0], tup[1])) != sorted(new_centroids, key=lambda tup: (tup[0], tup[1])):
        print("Current centroid and new centroid are not same, so make new centroid current and find new one ")
        print("")
        current_centroids = new_centroids
        print("***Current centroids***")
        print(current_centroids)
        current_clusters = assign_tuples_to_clusters(new_centroids, data)
        print("***Current clusters***")
        print(current_clusters)
        new_centroids = derive_centroids_for_clusters(current_clusters)
        print("***New Centroids***")
        print(new_centroids)

    print("Current Centroid and New Centroid match.. Exit")
kmeans_cluster(2,data)






