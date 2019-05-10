
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



#preprocessing
#reading the files, our keywords and pages 

keywords = pd.read_csv('keyword.csv')
pages = pd.read_csv('pages.csv')

#Get files raw data
processed_keywords = keywords.values
processed_pages = pages.values


for page in processed_pages:
    print('From the web page called  ', page[0])
    print("----------------------------------- \n")
    
    with open(page[0]) as fp:                   # Open files
        
        outputFile = BeautifulSoup(fp, "lxml")  #Read page files 
        
        for keyword in processed_keywords:
            
            pattern = re.compile(keyword[0])     # define our keyword as a search pattern
            
            class MyHTMLParser(HTMLParser):
                def handle_starttag(self, tag, attrs):   # get all the start tag,read their attricbutes and 
                    for attr in attrs:                   #check for pattern matching 
                        if pattern.search(str(attr)):
                            print("Match :", pattern.search(str(attr)))
                            
                def handle_data(self, data):             # Read data inside the start and end tag and check 
                    if pattern.search(data):             #for pattern matching
                        print("Match :", pattern.search(data))
            
            parser = MyHTMLParser()
            parser.feed(str(outputFile))
            
            if pattern.search(str(outputFile.a)):                       #using a tag, to read href attribute and check 
                  print("Match :", pattern.search(str(outputFile.a)))  #pattern matching
                
    print(" ")

