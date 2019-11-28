def splitparts(filearr, div):
  filelen = len(filearr)
  divsize = filelen / div
  remainder = filelen % div

  fileparts = []

  divstart = 0
  
  for i in range(1, div+1):
    fileslice = filearr[divstart * divsize : i * divsize]
    
    fileparts.append(fileslice)

    divstart += 1
  
  if remainder > 0:
    count = remainder 
    for i in range(remainder):
      fileparts[-1].append(filearr[filelen - count])
      count -= 1
    
  return fileparts


def main():
  filename = input("Enter path to filename: ")
  savepath = input("Enter path to save split parts: ")
  partname = input("Enter filename prefix for split parts (0 for default): ")
  divisions = input("Enter number of desired parts: ")

  if partname == 0:
    partname = "part"

  print("Writing to: " + savepath + partname + "n" + ".txt")

  thefile = open(filename, "r")
  f = thefile.readlines()
  thefile.close()

  parts = splitparts(f, divisions)

  for i in range(divisions):
    partpath = savepath + partname + str(i) + ".txt"
    part = open(partpath, "a+")

    for j in range(len(parts[i])):
      part.write(parts[i][j])

    part.close()
  
  print("Successfully split file.")

if __name__ == "__main__":
  main()