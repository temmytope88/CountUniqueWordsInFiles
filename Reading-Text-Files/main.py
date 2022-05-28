# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    b = ''
    
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            a = line.strip()
            b = b + "\n" +a
    return b

def count_words():
    text = read_file_content("story.txt")
    words = text.split()
    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)
    my_dict = {}
    for unique in uniques:
        i = 0;
        new_key = unique
        for word in words:
            if (word == unique):
               i = i + 1        
        new_value = i
        my_dict[new_key]=new_value
    print(my_dict)
count_words()




   