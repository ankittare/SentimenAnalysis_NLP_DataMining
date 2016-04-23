from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def stemmer(words):
    processed_words=[];
    for w in words:
        word=w.lower().strip()
        if word not in stopwords.words('english') and word!='':
            processed = WordNetLemmatizer().lemmatize(word, 'n')  # by Noun
            processed = WordNetLemmatizer().lemmatize(processed, 'v')  # by Verb
            processed_words.append(processed);
    return processed_words;
