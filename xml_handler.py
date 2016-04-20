import xml.etree.cElementTree as et
from SentimenAnalysis_NLP_DataMining import inverted_lists
class xml_parser:

    def __init__(self):
        self.data_dict = {};

    def get_input_string(self, input):
        sxml = "";
        for lines in open(input):
            sxml += lines
        return sxml;

    def parse(self, input):

        tree=et.fromstring(self.get_input_string(input))
        #mai linverted list for both camera and auto
        il={};
        il["camera"]={};
        il["auto"]={};
        sw = self.get_stopwords();

        for el in tree.findall('DOC'):
            print('-------------------');
            cat,rating,doc="","","";
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    doc=ch.text;
                if (ch.tag == "CLASS"):
                    cat=ch.text.strip().lower();
                if ch.tag == "rating":
                    rating=ch.text.strip();
                if ch.tag == "TEXT":
                    text=ch.text.strip().split(' ');
                    word_count=self.word_count(text, sw);
                    for word in word_count:
                            self.update_dict(il[cat],word,word_count[word],doc, rating);
                    if cat not in self.data_dict:
                        self.data_dict[cat]=[]
                    self.data_dict[cat].append(il[cat]);

    def update_dict(self, il, word,count,doc, r):
        if (word not in il):
            il[word] = inverted_lists.inverted_list();
            il[word].ratings.add(r)
            il[word].docs.append((doc,count));

    def word_count(self,text, stopwords):
        d={};
        for word in text:
            w=word.lower();
            if w not in stopwords:
                if w not in d:
                    d[w]=1;
                else:
                    d[w]+=1;
        return d;

    def get_stopwords(self):
        stopwords = set([]);
        stopwords_file = open(
            "C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\stopwrods.txt");
        for lines in stopwords_file:
            stopwords.add(lines.strip());
        return stopwords;

    def __iter__(self):
        return self.data_dict;