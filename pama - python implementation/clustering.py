import warnings
warnings.simplefilter("ignore", RuntimeWarning)
import math
import random
import plotly
import plotly.plotly as py
plotly.tools.set_credentials_file(username='pamaarniel', api_key='K6JLViZBmTRGzEKmboqz')
import plotly.graph_objs as go
from scipy import misc
from PIL import Image

def main():
##    print ("RUNNING PART ONE...")
##    filename = "kmdata1.txt"
##    samples = readdata(filename)
##    partOne(samples)

    print ("RUNNING PART TWO...")
    imgfile = "kmimg1.png"
    partTwo(imgfile)
    
    
class Sample:
    features = []
    
    def __init__(self):
        self.features = []
  
    def addfeature(self, feature):
        self.features.append(feature)

    def getfeatures(self):
        return self.features

    def getNumberOfFeatures(self):
        return len(self.features)

def readdata(filename):
    """
        str -> list
        loads a .txt file and returns a list of Samples
    """
    try:
        with open(filename) as fp:
            samples = []  
            for line in fp:
                currline = line.split(" ")  #split the line by space
                currsample = Sample()
                
                for num in currline:
                    if(num != ''):
                        currsample.addfeature( float(num) )
                samples.append(currsample)
        return samples
    except IOError:
        print('Error: File does not appear to exist')

def writedata(filename, samples):
    """
    """
    try:
        with open(filename, 'wb') as fp:
            for samp in samples:
                for i in range (0, samp.getNumberOfFeatures()): 
                    fp.write( str((samp.getfeatures())[i]) + " ")
                fp.write("\r\n")
        fp.close()
    except IOError:
        print('Error: Cannot write to file')
        
def displaysamples(samples):
    """
        list -> void
        prints the samples and their features
    """
    for samp in samples:
        for i in range (0, samp.getNumberOfFeatures()):
            print (samp.getfeatures())[i],     #features are comma-separated
        print

def partOne(samples):
    """
        list -> void
        Run 10 iterations
          a. output centroid assignments to iter<n>_ca.txt
          b. output the new centroid locations to iter<n>_cm.txt
          c. output J, appending it to iter<n>_cm.txt
          d. output dJ, difference of curr J from prev J, appending it to iter<n>_cm.txt
    """
    iterations = 10                                             #iterations is set to 10
    numofsamples = len(samples)                                 #total number of samples
    numoffeatures = samples[0].getNumberOfFeatures()            #the number of features in each sample
    centroids = [ [3, 3], [6, 2], [8, 5] ]                      #the clusters; initially set to these values
    numofclusters = len(centroids)                              #number of clusters; expected = 3
    distances = [0] * numofclusters                             #stores the current euclidean distance of a current sample with respect to a cluster
     
    currcost = 0                                                #stores the current calculated cost
    prevcost = 0                                                #remembers the calculated cost for finding the cost difference
    costdiff = 0                                                #cost difference between current cost and previous cost
    
    for i in range(0, iterations):
        print ("Running iteration " + str(i + 1) + "...")
        clusterAssignmentHistory = []                           #cluster assignments, to be written in part a
        currcosts = []                                          #stores the current euclidean distances depending on what cluster a point is currently assigned 
        samplesAssigned = [[] for c in range(numofclusters)]    #stores the current points assigned to cluster k 

        #print("Assigning clusters...")
        #cluster assignments
        for m in range(0, numofsamples):
    
            #find the distances of each cluster to the sample
            for k in range(0, numofclusters):
                currsample = samples[m].getfeatures()
                distances[k] = euclideandistance(currsample , centroids[k])

            #find the index of cluster centroid closest to the sample
            index = distances.index(min(distances))             #find the minimum of the distances and return what index
            currcosts.append(distances[index])                  #append the minimum distance to the sum of current costs
            samplesAssigned[index].append(currsample)           #append currsample to cluster it is currently assigned to; used for updating the centroids
            currclusterassi = index + 1                         #add 1 since our array is zero-based
            clusterAssignmentHistory.append(currclusterassi)    #append current cluster assignment to our cluster assignment history

        #print("Writing cluster assignments to a file...")  #write cluster assignments to iter<i + 1>_ca.txt
        writeclusterassignments( clusterAssignmentHistory, i + 1 )

        #print("Updating centroids...") #update centroids
        for k in range(0, numofclusters):
            centroids[k] = updatecentroid(samplesAssigned[k])   #average (mean) of points assigned to cluster k

        #print("Computing cost J...") #compute J
        currcost = sum(list(currcosts)) / float(len(currcosts)) #gets the current cost J value

        #print("Computing difference of cost J...") #compute dJ
        costdiff = prevcost - currcost
        prevcost = currcost

        #print("Writing update details to a file...") #write updates to iter<i + 1>_cm.txt
        writeupdates( centroids, currcost, costdiff, i + 1 )

        #print("Generating scatterplot for iteration " + str(i + 1) + "...")
        scatterplot(samples, centroids, clusterAssignmentHistory, i + 1)

def scatterplot(samples, centroids, clusterassignments, iteration):    
    ydata = []
    xdata = []
    for i in range(0, len(samples)):
        xdata.append(samples[i].getfeatures()[0])
        ydata.append(samples[i].getfeatures()[1])

    dataset = go.Scatter(
        x = xdata,
        y = ydata,
        mode='markers',
        name='data points',
        marker=dict(
            size='8',
            color = clusterassignments,
            colorscale='Rainbow',
            line = dict(
                width = 1,
                color = 'rgb(0, 0, 0)' #black
            )
        ),
        opacity = 0.8
    )

    xclust = []
    yclust = []
    for i in range(0, len(centroids)):
        xclust.append(centroids[i][0])
        yclust.append(centroids[i][1])

    clusters = go.Scatter(
        x = xclust,
        y = yclust,
        name='clusters',
        mode = 'markers',
        marker = dict(
            symbol = 17, #star symbol
            size = '20',
            color = [1, 2, 3],
            colorscale='Rainbow',
            line = dict(
                width = 2,
                color = 'rgb(0, 0, 0)' #black
            )
        )
     )
    
    data = [dataset, clusters]

    py.plot(data, filename=('scatter-plot' + str(iteration)))

def euclideandistance(sample, centroid):
    """
        list, list -> num
        accepts one sample and compute its Euclidean distance
        with respect to the given centroid
    """
    lenA = len(sample)
    lenB = len(centroid)

    if(lenA != lenB):
      raise Exception("Input error: sample and centroid given do not match in number of features")
    else:
      sumofsquares = 0
      for i in range(0, lenA):
        curr = centroid[i] - sample[i]
        sumofsquares += (curr * curr)
      return math.sqrt(sumofsquares)

    
def updatecentroid(samplesAssigned):
    numofsamples = len(samplesAssigned)
    numoffeatures = len(samplesAssigned[0])
    averagesperfeature = [0] * numoffeatures
    featuressum = [0] * numoffeatures

    for m in range(0, numofsamples):
        for k in range(0, numoffeatures):
            featuressum[k] += samplesAssigned[m][k]

        for k in range(0, numoffeatures):
            averagesperfeature[k] = featuressum[k] / float(numofsamples)

    return averagesperfeature


def writeclusterassignments(clusterassignments, iteration):
    filename = "iter" + str(iteration) + "_ca.txt"
    try:
        with open(filename, 'wb') as fp:
            caLen = len(clusterassignments)
            for i in range(0, caLen):
                fp.write( str(clusterassignments[i]) )
                fp.write("\r\n")
        fp.close()
    except IOError:
        print('Error: Cannot write to file')
     

def writeupdates(centroids, cost, costdiff, iteration):
    filename = "iter" + str(iteration) + "_cm.txt"
    try:
        with open(filename, 'wb') as fp:
            #write centroids
            numofcentroids = len(centroids)
            for i in range(0, numofcentroids):
                numoffeatures = len(centroids[i])
                fp.write("centroid " + str(i + 1) + ": ")
                for k in range(0, numoffeatures):
                    fp.write(str(centroids[i][k]) + " ")
                fp.write("\r\n")

            #write cost
            fp.write("J = " + str(cost) + "\r\n")

            #write cost difference
            fp.write("dJ = " + str(costdiff) + "\r\n")
        fp.close()
    except IOError:
        print('Error: Cannot write to file')


def partTwo(imgfilename):
    pixels = misc.imread(imgfilename) #the 128x128x3 rgb array
    transformed = []                  #the 16384x3 rgb array

    print("Transforming image to its 16384x3 RGB array...")
    for array in pixels:
        for rgb in array:
            transformed.append( list(rgb) )

    numofsamples = len(transformed)     #total number of samples
    numoffeatures = len(transformed[0])
    numofclusters = 16

    print("Randomizing 16 centroids...")
    randomindices = random.sample(xrange(0, 16384), numofclusters) #choose 16 indices from 0-16383
    centroids = []
    
    for i in randomindices:
        centroids.append( transformed[i] )

    distances = [0] * numofclusters #stores the current euclidean distance of a current sample with respect to a cluster
    iterations = 10

    print("Running iterations...")
    #Run 10 iterations of K-means to cluster the pixels into the 16 colors nearest to each one.
    for i in range(0, iterations):
        clusterAssignmentHistory = []
        samplesAssigned = [[] for c in range(numofclusters)]    #stores the current points assigned to cluster k

        #cluster assignments
        for m in range(0, numofsamples):

            #find the distances of each cluster to the sample
            for k in range(0, numofclusters):
                currsample = transformed[m]
                distances[k] = euclideandistance(currsample , centroids[k])

            #find the index of cluster centroid closest to the sample 
            index = distances.index(min(distances))             #find the minimum of the distances and return what index
            samplesAssigned[index].append(currsample)           #append currsample to cluster it is currently assigned to; used for updating the centroids
            currclusterassi = index + 1                         #add 1 since our array is zero-based
            clusterAssignmentHistory.append(currclusterassi)    #append current cluster assignment to our cluster assignment history

        #update centroids
        for k in range(0, numofclusters):
            centroids[k] = updatecentroid(samplesAssigned[k])   #average (mean) of points assigned to cluster k

    print("Rounding off the final intensity values of the 16 centroids...")
    #round off to integer values the intensity values of the 16 centroids
    for k in range(0, numofclusters):
        centroids[k] = map(int, centroids[k])

    print("Assigning the RGB values of each pixel according to its nearest centroid...")
    #assign the intensity value of a pixel to the intensity value of the centroid to which it has been assigned
    finalpixels = []
    numofassis = len(clusterAssignmentHistory)
    for i in range(0, numofassis):
        k = clusterAssignmentHistory[i]
        finalpixels.append(centroids[k - 1])

    print("Converting the 16384x3 RGB array to 128x128x3...")
    #convert to 128 x 128 x 3
    col = 128
    row = 128
    compressedImage = [ finalpixels[col*i : col*(i+1)] for i in range(row)]

    print("Saving the final compressed image...")
    #save image
    newimage = Image.new('RGB', (128, 128))  # type, tuple size
    newimage.putdata([tuple(p) for row in compressedImage for p in row])
    newimage.save("compressed.png")

    print("Showing the compressed image...")
    im = Image.open("compressed.png")
    im.show()
            
if __name__ == "__main__":
    main()
