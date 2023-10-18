# Write a Program to read a text file and find all unique words and how many times the
# word occurrences.
count={}
with open("file.txt","r") as f:
    for line in f:
        for word in line.split():
            if(word in count) :
                count[word]+=1 
            else:
                count[word]=1

            
for word,count in count.items():
    print(f"{word}: {count}")