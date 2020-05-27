from utils.removeStopwords import removeStopwords


def stop_words():
    text = "loremIpsum text, with letters a, b, c, d, and names, like mateus, felipe, gonçalves."
    print(f'text:\n{text}\n\n')
    text_without_stopwords = removeStopwords(
        text, ['a', 'b', 'e', 'like', 'and'])
    print(f'text without stopwords:\n{text_without_stopwords}\n\n')


def unique_test():
    print('REMOVE STOPWORDS\n')
    stop_words()
