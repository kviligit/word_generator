filename = input("enter complete path of file you would like to convert")
file = open(filename, "r")
wordlist = []
# This part is specific to the format of the word lists from Sprakbanken.
for line in file:
    splitline = line.split(' ')
    wordlist.append(splitline[2])
file.close()

outfilename = input("Provide desired name of output file: \n")
outfile = open(outfilename, "w")
for i in wordlist:
    outfile.write(i)
outfile.close()