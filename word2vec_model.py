import sys
import re
import nltk
import os

from gensim.models import word2vec
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

def get_newspapers(path):
    english_stopwords = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokenized_sentences = []
    count = 0
    total_files = len(os.listdir(path))
    for file in os.scandir(path):
        with open(file.path, encoding='utf-8', errors='ignore') as input_file:
            text = input_file.read()
            text = re.sub(r'<[^>]+>', '', text)
        sentences = re.split(r'[!?.]+', text)
        for sentence in sentences:
            sentence = word_tokenize(sentence)
            tagged_sentence = pos_tag(sentence)
            sentence = [token for token, pos in tagged_sentence if pos in ('NN', 'NNS')]
            sentence = [lemmatizer.lemmatize(token).lower() for token in sentence if token not in english_stopwords]
            sentence = [token for token in sentence if not token.isdigit()]
            tokenized_sentences.append(sentence)
        count += 1
        print(f'\r{count}/{total_files} files done', end = '')
    return tokenized_sentences

if __name__ == '__main__':
    path = sys.argv[1]
    window_size = int(sys.argv[2])

    print('Getting sentences...')
    sentences = get_newspapers(path)

    print('\nTraining model...', flush=True)
    model = word2vec.Word2Vec(sentences, min_count=10, window=window_size, size=300, iter=10, workers=8)
    model.save(f'/Users/amazinganthony/digital_approaches/models/{sys.argv[3]}')
    print('Model complete.')
