import os

files = os.listdir("images")
i = 1
for file in files:
    if file.endswith(".png"): #jeisob file ends with .png oisob file k print koro
        print(file)    # print all files and images
        
    os.rename(f"images/{file}", f"images/{i}.png")
    i = i + 1 # sokol png file er nam change hoyeche serial by 1-17    
        

    os.rename("images/chatsheet.pdf", "images/importantsheet.pdf") # chatsheet.pdf file name change to importantsheet.pdf just use simply os module
    # os.rename("images/text.txt", "images/documents.txt") # text.txt file name change to documents.txt just use simply os module

