from go_to_cross import Crosswords
dictionary_words = dict()


def load_dict_words():
    global dictionary_words
    with open('data/сырдт.csv', encoding='utf-8') as myfa:
        lines = myfa.read().split('\n')
        for i in lines:
            question = i[:-1]
            print(question)
    with open(f'data/data/{question}', encoding='utf-8') as myf:
        lines = myf.read().split('\n')
        for ind, i in enumerate(lines):
            word_rus, word_ose = i.split()
            dictionary_words[str(ind + 1)] = [word_rus, word_ose]
'''    with open(f'data/{question}', encoding='utf-8') as myf:
        lines = myf.read().split('\n')
        for ind, i in enumerate(lines):
            word_rus, word_ose = i.split()
            dictionary_words[str(ind + 1)] = [word_rus, word_ose]'''


#sender = None


def get_sender():
    global sender
#    sender = sender()
#dicti()
#print(dictionary)