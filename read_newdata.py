import pandas
import nltk
import re

import pandas as pd
from nltk.corpus import stopwords

df = pandas.read_json("arxivData.json")

df2 = df[['id', 'title']]

STOPWORDS = stopwords.words('english')
STOPWORDS = set(STOPWORDS)


def text_prepare(text, STOPWORDS):
    """        text: a string

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

titles = pd.DataFrame(
    columns=['fixed_titles']
)
titles["fixed_titles"] = df2['title'].apply(lambda x: text_prepare(x, STOPWORDS))
titles_lists = titles["fixed_titles"]
tuple_titles = tuple(titles_lists)


# new_list =[]
# for x in titles_lists:
#     if "machine" in x:
#         new_list.append(x)
# print(new_list)
# print(len(new_list))