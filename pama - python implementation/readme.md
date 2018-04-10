README.txt
by Jose Arniel Pama

The folling code snippet is used for running the two parts of the machine problem. It is found at the top portion of my program comprising the "main()" function.

def main():
    print ("RUNNING PART ONE...")
    filename = "kmdata1.txt"
    samples = readdata(filename)
    partOne(samples)

    print ("RUNNING PART TWO...")
    imgfile = "kmimg1.png"
    partTwo(imgfile)


1. To run part one only, simply comment out the snippet starting from the print statement "Running Part Two" until the line "partTwo(imgfile)". I have used the online graphing tool called Plot.ly, so it requires to connect to the internet in running part one. The browser automatically opens after generating the graph per iteration.


2. To run part two only, simply comment out the snippet starting from the print statement "Running Part One" until the line "partOne(samples)". A new window will open displaying the resulting compressed image.