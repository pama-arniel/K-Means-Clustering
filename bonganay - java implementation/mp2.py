import math
import random

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from scipy import misc
from PIL import Image


def partOne():
    filename = "kmdata1.txt"
    dataset = read(filename)
    k1 = [3, 3]
    k2 = [6, 2]
    k3 = [8, 5]
    k = [k1, k2, k3]
    iterations = 10
    iterate(dataset, k, iterations)


def read(filename):
    dataset = []
    try:
        f = open(filename, "r")
        for line in f:
            data = line.split()
            sample = [float(data[0]), float(data[1])]
            dataset.append(sample)
        f.close()
        return dataset
    except Exception:
        print "File does not exit!"

def iterate(dataset, centroids, iterations):
    list_k = []
    list_values = []
    k = centroids
    prev_cost = 0
    for i in range(0, iterations):
        values = assign_centroids(dataset, k)
        list_values.append(values[2])
        list_k.append(values[1])
        c = cost(values[0])
        write_to_file(values[3], values[1], prev_cost, c, i)
        k = values[1]
        prev_cost = c
    show_graph(list_k, list_values)

def write_to_file(assignment, curr_centroid, prev_cost, curr_cost, iter):
    filename = ("iter%s") % (iter + 1)
    file1 = open(filename + "_ca.txt", "w")
    i = 0
    for x in assignment:
        file1.write(str(x) + "\n")
        i += 1
    file1.close()
    file2 = open(filename + "_cm.txt", "w")
    i = 1
    for k in curr_centroid:
        w = ("centroid_%d = (%f, %f)") % (i, k[0], k[1])
        file2.write(w + "\n")
        i += 1
    w = "J = %f" % (curr_cost)
    file2.write(w + "\n")
    w = "dJ = %f" % (prev_cost - curr_cost)
    file2.write(w)
    file2.close()


def assign_centroids(dataset, k):
    for_cost = []
    assignment = []
    # assigned_data = [[]] * len(k)
    for sample in dataset:
        point = [sample[0], sample[1]]


        minimum = distance(point, k[0])
        min_index = 0
        i = 0
        for centroid in k:
            d = distance(point, centroid)
            if (d < minimum):
                minimum = d
                min_index = i
            i += 1
        for_cost.append(minimum)
        assignment.append(min_index + 1)
    c1 = []
    c2 = []
    c3 = []

    i = 0
    for a in assignment:
        if a == 1:
            c1.append(dataset[i])
        elif a == 2:
            c2.append(dataset[i])
        elif a == 3:
            c3.append(dataset[i])
        i += 1
    assigned_data = [c1, c2, c3]
    new_k = [[0, 0], [0, 0], [0, 0]]
    i = 0

    for a in assigned_data:
        for data in a:
            new_k[i][0] += data[0]
            new_k[i][1] += data[1]
        new_k[i][0] = new_k[i][0] / len(a)
        new_k[i][1] = new_k[i][1] / len(a)
        i += 1
    result = [for_cost, new_k, assigned_data, assignment]
    return result

def cost(values):
    sum = 0.0;
    for x in values:
        sum += x
    return sum / len(values)

def distance(point1, point2):
    res = 0
    for i in range(0, len(point1)):
        a = float(point1[i]) - float(point2[i])
        res += a**2

    return math.sqrt(res)

def partTwo():
    pixels = misc.imread("kmimg1.png")
    transformed = []

    for array in pixels:
        for rgb in array:
            transformed.append(list(rgb))

    numofclusters = 16

    randomindices = random.sample(xrange(0, 16384), numofclusters)
    centroids = []

    for i in randomindices:
        centroids.append(transformed[i])
    
    k = centroids
    assignment = []
    for i in range(0, 10):
        print "Compressing"
        values = reassign_part2(transformed, k)
        k = values[0]
        assignment = values[1]
    for index in range(0, len(k)):
        for x in range(0, len(k[index])):
            k[index][x] = int(k[index][x])

    new_data = []

    for a in assignment:
        new_data.append(k[a])
    col = 128
    row = 128
    compressedImage = [new_data[col * q: col * (q + 1)] for q in range(row)]
    newimage = Image.new('RGB', (128, 128))  # type, tuple size
    newimage.putdata([tuple(p) for row in compressedImage for p in row])
    newimage.save("compressed.png")

def reassign_part2(dataset, k):
    for_cost = []
    assignment = []
    for sample in dataset:
        point = [sample[0], sample[1]]
        minimum = distance(point, k[0])
        min_index = 0
        i = 0
        for centroid in k:
            d = distance(point, centroid)
            if (d < minimum):
                minimum = d
                min_index = i
            i += 1
        for_cost.append(minimum)
        assignment.append(min_index)
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    c10 = []
    c11 = []
    c12 = []
    c13 = []
    c14 = []
    c15 = []
    c16 = []
    i = 0
    for a in assignment:
        if a == 0:
            c1.append(dataset[i])
        elif a == 1:
            c2.append(dataset[i])
        elif a == 2:
            c3.append(dataset[i])
        elif a == 3:
            c4.append(dataset[i])
        elif a == 4:
            c5.append(dataset[i])
        elif a == 5:
            c6.append(dataset[i])
        elif a == 6:
            c7.append(dataset[i])
        elif a == 7:
            c8.append(dataset[i])
        elif a == 8:
            c9.append(dataset[i])
        elif a == 9:
            c10.append(dataset[i])
        elif a == 10:
            c11.append(dataset[i])
        elif a == 11:
            c12.append(dataset[i])
        elif a == 12:
            c13.append(dataset[i])
        elif a == 13:
            c14.append(dataset[i])
        elif a == 14:
            c15.append(dataset[i])
        elif a == 15:
            c16.append(dataset[i])
        i += 1
    assigned_data = [c1, c2, c3,c4, c5, c6, c7, c8,c9, c10, c11, c12, c13,c14, c15, c16]
    new_k = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    for a in assigned_data:
        for data in a:
            new_k[i][0] += data[0]
            new_k[i][1] += data[1]
            new_k[i][2] += data[2]

        new_k[i][0] = new_k[i][0] / len(a)
        new_k[i][1] = new_k[i][1] / len(a)
        new_k[i][2] = new_k[i][2] / len(a)

        i += 1
    result = [new_k, assignment]
    return result

class Graph:
    ax = None
    plt = None
    fig = None
    iteration = 0
    centroids = None
    values = None
    data1 = []
    k1 = []

    def __init__(self, plot, ax, fig, centroids, values):
        self.ax = ax
        self.plt = plot
        self.fig = fig
        self.centroids = centroids
        self.values = values

    def next(self, event):
        self.iteration += 1
        if self.iteration == len(self.values):
            self.iteration = 0
        self.set_values()

    def prev(self, event):
        self.iteration -= 1
        if self.iteration == -1:
            self.iteration = 9
        self.set_values()

    def set_values(self):
        data = (self.values[self.iteration][0], self.values[self.iteration][1], self.values[self.iteration][2])
        self.data1 = []
        for d in data:
            x = []
            y = []
            for point in d:
                x.append(point[0])
                y.append(point[1])
            self.data1.append([x, y])
        k = self.centroids[self.iteration]
        self.k1 = []
        for point in k:
            x = [point[0]]
            y = [point[1]]
            self.k1.append([x, y])
        self.show()

    def show(self):

        colors = ("purple", "green", "red")

        groups = ("centroid 1", "centroid 2", "centroid 3")

        self.ax.remove()
        self.ax = self.fig.add_subplot(1, 1, 1, axisbg="1.0")

        for d, color, group, centroid in zip(self.data1, colors, groups, self.k1):
            x, y = d
            self.ax.scatter(x, y, alpha=1, c=color, edgecolors='none', s=30, label=group)
            x1, y1 = centroid
            self.ax.scatter(x1, y1, alpha=1, c=color, edgecolors='black', s=500, marker='*')

        title = "Iteration %d" % (self.iteration + 1)
        self.plt.title(title)
        self.plt.legend(loc=0)
        # fn = "%s.png" %(title)
        # self.plt.savefig(fn)
        self.plt.show()


def show_graph(centroids, values):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
    plt.title('Iteration 1')
    plt.legend(loc=0)
    plt.subplots_adjust(bottom=0.2)
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bprev = Button(axprev, 'Previous')
    callback = Graph(plt, ax, fig, centroids, values)
    bnext.on_clicked(callback.next)
    bprev.on_clicked(callback.prev)
    callback.set_values()



partOne()
# partTwo()