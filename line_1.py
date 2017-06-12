from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

words = ['morze', 'Polska', 'sklep', 'wiosna', 'dziecko']
filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt",
             "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]

def line_plot(data, titles, words):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Słowa")
    plt.ylabel("Liczba wystąpień")

    colors = ['r', 'b', 'g', 'y', 'm', 'k', 'c']

    for filename_data, title, my_color in zip(data, titles, colors):
        plt.plot(filename_data, color=my_color, label=title)

    plt.legend()

    plt.grid()

    plt.xticks(range(len(words)), words, rotation=90)

    plt.tight_layout()
    plt.savefig('plot2.png')
    plt.show()

def count_freq(fname):
    with open(fname, encoding='utf8') as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    print(result)
    return result

def color_lines(texts, titles, words):
    my_data = []
    for text in texts:
        my_data.append(return_values(count_freq(text), words))
    print(my_data)
    line_plot(my_data, titles, words)

color_lines(filenames, titles, words)