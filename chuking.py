import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

# Descargamos los datos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLTK es una biblioteca de Python para procesamiento de lenguaje natural."
words = word_tokenize(text)
tagged = nltk.pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
result = parser.parse(tagged)
print(result)

from nltk import ne_chunk, pos_tag, word_tokenize
import nltk

# Descargamos los datos necesarios de NLTK
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
text = "Barack Obama was born in Hawaii."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
ner_chunks = ne_chunk(pos_tags)
print(ner_chunks)