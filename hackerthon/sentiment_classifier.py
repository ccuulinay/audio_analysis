import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


class TextClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


# READS PICKLED WORD FEATURES AS WELL AS SAVED CLASSIFIERS

documents_f = open("pickle_files/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()

word_features7k_f = open("pickle_files/word_features7k.pickle", "rb")
word_features = pickle.load(word_features7k_f)
word_features7k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


open_file = open("pickle_files/originalnaivebayes7k.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle_files/MNB_classifier7k.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle_files/BernoulliNB_classifier7k.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle_files/LogisticRegression_classifier7k.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle_files/LinearSVC_classifier7k.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle_files/SGDC_classifier7k.pickle", "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()

text_classifier = TextClassifier(classifier,
                                 LinearSVC_classifier,
                                 MNB_classifier,
                                 BernoulliNB_classifier,
                                 LogisticRegression_classifier)


def sentiment(text):
    feats = find_features(text)
    # print(feats)
    return text_classifier.classify(feats), text_classifier.confidence(feats)
