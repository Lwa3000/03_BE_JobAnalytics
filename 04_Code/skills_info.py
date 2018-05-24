# coding: utf-8

# In[1]:


import re # Regular expressions
from collections import Counter # Keep track of our term counts
from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd # For converting results to a dataframe and bar chart plots
import os


# In[2]:


def text_cleaner(text):

    text = str(text) # Get the text from this
    
    lines = (line.strip() for line in text.splitlines()) # break into lines
    
    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each
    
    def chunk_space(chunk):
        chunk_out = chunk + ' ' # Need to fix spacing issue
        return chunk_out  
        
    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line

    # Now clean out all of the unicode junk (this line works great!!!)
        
    try:
        text = text.decode('utf-8') # Need this as some websites aren't formatted
    except:                                                            # in a way that this works, can occasionally throw
        return                                                         # an exception
       
    text = re.sub("[^a-zA-Z.+3]"," ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                                # Also include + for C++
        
    text = text.lower().split()  # Go to lower case and split them apart
        
    stop_words = set(stopwords.words("english")) # Filter out any stop words
    text = [w for w in text if not w in stop_words]
        
    text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
        
    return text


# In[3]:


def get_skills(city, job_desc):
    
    words = []
    
    if len(job_desc) > 0:
        for j in range(0, len(job_desc), 1):
            final_description = text_cleaner(job_desc[j])
            if len(final_description) > 0: 
                words.append(final_description)

        doc_frequency = Counter() # This will create a full counter of our terms. 
        [doc_frequency.update(item) for item in words] 

        # Now we can just look at our final dict list inside doc_frequency

        # Obtain our key terms and store them in a dict. These are the key data science skills we are looking for

        skills_dict = Counter({
                                    "Java": doc_frequency["java"], 
                                    "Excel": doc_frequency["excel"],
                                    "VBA": doc_frequency["vba"],
                                    "D3.js": doc_frequency["d3.js"],
                                    "C++": doc_frequency["c++"], 
                                    "PHP": doc_frequency["php"], 
                                    "Perl": doc_frequency["perl"],
                                    "Python": doc_frequency["python"], 
                                    "Matlab": doc_frequency["matlab"],
                                    "SQL": doc_frequency["sql"], 
                                    "Ruby": doc_frequency["ruby"], 
                                    "R": doc_frequency["r"],
                                    "SAS": doc_frequency["sas"],
                                    "SPSS": doc_frequency["spss"],
                                    "HTML": doc_frequency["html"],  
                                    "JavaScript": doc_frequency["javascript"],
                                    "XML": doc_frequency["xml"],
                                    "Julia": doc_frequency["julia"], 
                                    "Scala": doc_frequency["scala"],
                                    # "Tableau": doc_frequency["tableau"],
                                    # "Looker": doc_frequency["looker"],
                                    "Hadoop": doc_frequency["hadoop"], 
                                    "Spark": doc_frequency["spark"], 
                                    "MySQL": doc_frequency["mysql"],
                                    "HBase": doc_frequency["hbase"], 
                                    "MongoDB": doc_frequency["mongodb"], 
                                    "Theano": doc_frequency["theano"], 
                                    "TensorFlow": doc_frequency["tensorflow"], 
                                    "Hive": doc_frequency["hive"], 
                                    "NoSQL": doc_frequency["nosql"]
                                    })
#         misc_dict = {"Dashboards": doc_frequency["dashboards"],
#                                 "Visualization": doc_frequency["visualization"],
#                                  "Database": doc_frequency["database"],
#                                 "Statistics": doc_frequency["statistics"],
#                                  "Algebra": doc_frequency["algebra"],
#                                  "Calculus": doc_frequency["calculus"],
#                                  "Algorithms": doc_frequency["algorithms"]
#                     }
                          
        skills_df = pd.DataFrame.from_dict(skills_dict, orient='index')
        skills_df = skills_df.sort_values(by=0, ascending=False)
        skills_df = skills_df.loc[skills_df[0]>0,:].reset_index()
        
        skills_df = skills_df.rename(columns={"index": "skill_type", 0: str(city)+'_count'})
        
    else:
        skills_df = print("Error: City not found")

    return  skills_df


# In[4]:
