import sys
import os
import time
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

def main():

    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    actualPos = 0
    actualNeg = 0
    actualNeu = 0

    for root, directories, filenames in os.walk(sys.argv[1]):


        for each_filename in filenames:
            if each_filename.endswith(".txt"):

                path = root + '/' + each_filename


                with open(os.path.join(root, each_filename), 'r', encoding="latin1") as f:
                    # print("path is ",f)
                    tokens = f.read()


                    if "Train" in path:
                        train_data.append(tokens)
                        if "positive" in path:
                            train_labels.append("positive")
                        elif "negative" in path:
                            train_labels.append("negative")
                        elif "neutral" in path:
                            train_labels.append("neutral")

                    elif "Dev" in path:
                        test_data.append(tokens)

                        if "positive" in path:
                            actualPos = actualPos + 1
                            test_labels.append("positive")
                        elif "negative" in path:
                            actualNeg = actualNeg + 1
                            test_labels.append("negative")
                        elif "neutral" in path:
                            actualNeu = actualNeu + 1
                            test_labels.append("neutral")

    # features = []
    #
    #
    #
    #
    # for each_word in train_data:
    #     # print(i)
    #     if each_word in string.punctuation:
    #         punct = True
    #     else:
    #         punct = False
    #
    #
    #     features.extend([
    #         'token.isPunctuation=%s' % punct,
    #         # 'word.isupper=%s' % each_word.isupper()
    #
    #     ])


    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    print(type(train_vectors))
    featureset = []

    count = 1
    # for i in train_vectors:
    #     print (i.toarray())
    #     count = count + 1
    # print (count)



    # # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()

    classifier_liblinear.fit(train_vectors, train_labels)

    prediction_liblinear = classifier_liblinear.predict(test_vectors)
    pos = 0
    neg = 0;
    neu = 0;
    for i in prediction_liblinear:
        # print("labels are ",i)
        if "positive" in i:
            pos = pos + 1
        elif "negative" in i:
            neg = neg + 1
        elif "neutral" in i:
            neu = neu + 1
    print("act posi ", actualPos)
    print("act negi ", actualNeg)
    print("act neut ", actualNeu)
    print("pred posi ", pos)
    print("pred negi ", neg)
    print("pred neut ", neu)


    print("Results for LinearSVC()")
    print(classification_report(test_labels, prediction_liblinear))

if __name__ == '__main__':

    main()
