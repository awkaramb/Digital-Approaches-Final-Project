import sys
import gensim.models
from gensim.models import word2vec

words = []

if __name__ == '__main__':
    print('Loading model...')
    model = word2vec.Word2Vec.load(sys.argv[1])
    for i in model.wv.vocab:
        words.append(i)
    print(words)

    while True:
        word = input('\nType Word: ')
        print(f'Most similar words to {word}:')
        for word, score in model.wv.most_similar(word):
            print(word, score)
