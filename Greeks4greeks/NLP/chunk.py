import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree 
def get_continuous_chunks(text):
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             if current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk

my_sent = "How's the weather in New York and Brooklyn" 
get_continuous_chunks(my_sent)
['New York', 'Brooklyn']