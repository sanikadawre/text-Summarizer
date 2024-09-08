# summarizer.py
import spacy
import en_core_web_sm
from string import Template
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
from heapq import nlargest

nlp = en_core_web_sm.load()


stopwords = list(STOP_WORDS)
pos_tag = ['PROPN','ADJ','NOUN','VERB']


def calcStrength(doc,freq_word):
    sentence_strength = {}
    for sentence in doc.sents:
        for word in sentence:
            if word.text in freq_word.keys():
                if sentence in sentence_strength.keys():
                    sentence_strength[sentence] += freq_word[word.text]
                else:
                    sentence_strength[sentence] = freq_word[word.text]
    return sentence_strength

def  filterTokens(doc):
    keyword = []
     ## filtering tokens
    for token in doc:
        if token.text in stopwords:
            continue
        if token.pos_ in pos_tag:
            keyword.append(token.text)
    return keyword

def normalizeFreq(freq_word):
    ## normalize the frequency
    max_freq  = freq_word.most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word]= (freq_word[word]/max_freq)
    return freq_word
    
def getSummary(text_string):
    doc = nlp(text_string)

    keyword = filterTokens(doc)

    freq_word = Counter(keyword)

    freq_word = normalizeFreq(freq_word)
    
    sentence_strength = calcStrength(doc,freq_word)

    summary_sentences = nlargest(2, sentence_strength, key=sentence_strength.get)
    final_summary_sentences  = [w.text for w in summary_sentences ]
    summary = ' '.join(final_summary_sentences)

    return summary
