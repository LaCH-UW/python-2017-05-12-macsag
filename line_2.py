from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

rc('font', family='DejaVu Sans')

filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
             "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]
word = 'Baryka'

def line_plot(results, texts_titles, word):
    plt.title('Liczba wystąpień słowa: ' + word)
    plt.xlabel('Teksty')
    plt.ylabel('Liczba wystąpień')

    plt.plot(results, color='r', label=word)
    plt.legend()

    plt.grid()

    plt.xticks(range(len(texts_titles)), texts_titles, rotation=90)

    plt.tight_layout()
    plt.savefig('plot3.png')
    plt.show()

def count_freq(fname):
    with open(fname, encoding='utf8') as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
        print(freq_dist)
    return freq_dist

def return_values(freq, word):
    result = freq[word] if word in freq else 0
    return result

def one_word(fnames, texts_titles, word):
    dane = []
    for fname in fnames:
        dane.append(return_values(count_freq(fname), word))
    print(dane)
    line_plot(dane, texts_titles, word)

one_word(filenames, titles, word)