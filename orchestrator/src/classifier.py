import nltk
from nltk.tokenize import word_tokenize # or use some other tokenizer
nltk.download('punkt')

class NLTKClassifier:
    
    def __init__(self, training_data):
        # format training data and train classifier
        all_words = set(word.lower() for passage in training_data for word in word_tokenize(passage[0]))
        formatted_training_data = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in training_data]
        classifier = nltk.NaiveBayesClassifier.train(formatted_training_data)
        # store tokenized training set and trained classifier
        self.all_words = all_words
        self.classifier = classifier

    def classify(self, message_string):
        message_features = {word: (word in word_tokenize(message_string.lower())) for word in self.all_words}
        return self.classifier.classify(message_features)

