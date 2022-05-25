# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import collections
def read_file_content(filename):
    # [assignment] Add your code here 
    data = open(filename,'r+')
    txt =data.read()
    
    return txt


def count_words():
   
    text = read_file_content("./story.txt")
    contents_as_list = text.split()
    occurence_count = collections.Counter(contents_as_list)
    print(occurence_count)
        
      #return {"as": 10, "would": 20}
    

count_words()
