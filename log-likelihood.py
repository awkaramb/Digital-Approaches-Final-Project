import sys
import os
import re
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def get_newspapers(path_to_files):
    words = []
    english_stopwords = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    for file in os.scandir(path_to_files):
        with open(file.path, encoding='utf-8', errors='ignore') as input_file:
            text = input_file.read()
            text = re.sub(r'<[^>]+>', '', str(text))
        tokens = re.findall(r'\w+', text)
        filtered_tokens = [lemmatizer.lemmatize(token).lower() for token in tokens if token not in english_stopwords]
        words.extend(filtered_tokens)
    return words

if __name__ ==  '__main__':
    path = sys.argv[1]
    window_size = int(sys.argv[2])
    print('Get all text...')
    words = get_newspapers(path)
    print('Building co-occurence representation...')
    bcf = BigramCollocationFinder.from_words(words, window_size=window_size)
    print('Computing top ten word associations using log-likelihood.')
    print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 10))

while True:
    word = input('\nType a word to get top 10 associated words (CTRL+C to quit): ')
    likelihood_scores = []
    for target_word in bcf.word_fd:
        likelihood_score = bcf.score_ngram(BigramAssocMeasures.likelihood_ratio, word, target_word)
        if likelihood_score == None:
            likelihood_score = 0
        likelihood_scores.append((target_word, likelihood_score))
    print(f'\n### Top 10 associated words as measured by Log-likelihood score. ###')
    for target_word, score in sorted(likelihood_scores, key=lambda x:x[1], reverse=True)[:10]:
        print(f'{target_word}: {score}')
        
