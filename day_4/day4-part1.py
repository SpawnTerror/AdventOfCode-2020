
import re
dirtydata = []
cleandata = []
documents = {}
good_documents = []

with open('day_4/input.txt', 'r') as input_txt:
    dirtydata = input_txt.read().split('\n\n')
  
    for everyline in dirtydata:
        cleandata.append(re.split('[\n\s]', everyline))
   
    documents = [dict([(line.split(":")) for line in passport]) for passport in cleandata]
    
    for passport in documents:
        if len(passport) >= 8:
            good_documents.append(passport)
        if len(passport) == 7:
            if 'cid' not in [item for item in passport]:
                    good_documents.append(passport)
        
print(len(good_documents))



