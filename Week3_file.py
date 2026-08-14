with open("file/junk.txt","r+") as f:
    file= f.readlines()
    print(f"total number of lines:{len(file)}")
    file.append("text file nanalyssis")
    for item in file:
        f.write(item)