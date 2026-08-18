import nltk
#nltk.download('wordnet')
#nltk.download('punkt_tab')
#nltk.download('averaged_perceptron_tagger_eng')
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

stemmer = PorterStemmer()

lemmatizer = WordNetLemmatizer()

wordss = "The students are studying NLP techniques and have studied language models."
words = wordss.lower()
tokens = word_tokenize(words)
for wo in tokens:

    print(stemmer.stem(wo))

    print(lemmatizer.lemmatize(wo))
print(pos_tag(tokens))
