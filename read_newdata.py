import pandas
import nltk 
from ntlk.corpus import stopwords
df = pandas.read_json("arxivData.json")

df2 = df[['id', 'title']]


titles = df2['title']

# def by_size(words,size):
#     result = []
#     for word in words:
#         if len(word)<=size:
#             result.append(word)
#     return result



#cleaning functions

STOPWORDS = stopwords.words('english')
STOPWORDS = set(STOPWORDS)
    
def text_prepare(text, STOPWORDS):
    """
        text: a string
        
        return: a clean string
    """
    REPLACE_BY_SPACE_RE = re.compile('[\n\"\'/(){}\[\]\|@,;#]')
    text = re.sub(REPLACE_BY_SPACE_RE, ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.lower()

    # delete stopwords from text
    text = ' '.join([word for word in text.split() if word not in STOPWORDS]) 
    text = text.strip()
    return text

tuple_of_titles = tuple(filtered_titles)
