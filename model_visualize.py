import sys
import numpy as np
import plotly.express as px
from gensim.models import word2vec
from sklearn.manifold import TSNE

def display_all(model_name):
    model = word2vec.Word2Vec.load(model_name)
    words = [word for word in model.wv.vocab]
    word2vec_matrix = np.array([model.wv[w] for w in words])
    draw_scatter_plot(word2vec_matrix, words, model_name)

def display_closest(model_name, word):
    title = f"20 words most associated with '{word.upper()}' for model {model_name}"
    model = word2vec.Word2Vec.load(model_name)
    similar_words = model.wv.similar_by_word(word, topn=20)
    word_labels = [word]
    query_word_vector = model.wv[word]
    results_matrix = np.array([query_word_vector])
    for word, _ in similar_words:
        word_vector = model.wv[word]
        word_labels.append(word)
        results_matrix = np.append(results_matrix, np.array([word_vector]), axis=0)
    draw_scatter_plot(results_matrix, word_labels, title)

def draw_scatter_plot(matrix, words, title):
    tsne_model = TSNE(n_components=2, init='pca', perplexity=40)
    reduced_matrix = tsne_model.fit_transform(matrix)
    x = reduced_matrix.transpose() [0]
    y = reduced_matrix.transpose() [1]
    color = np.random.randn(len(words))
    size = [1 for _ in range(len(words))]
    fig = px.scatter(x=x, y=y, text=words, size=size, color=color, render_mode='webgl', title=title)
    fig.update_layout(coloraxis_showscale=False)
    fig.update_traces(mode='markers+text', textposition='top center')
    fig.show()

if __name__ == '__main__':
    if len(sys.argv) > 2:
        display_closest(sys.argv[1], sys.argv[2])
    else:
        display_all(sys.argv[1])
