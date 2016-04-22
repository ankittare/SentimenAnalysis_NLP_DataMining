import xml.etree.cElementTree as et
from SentimenAnalysis_NLP_DataMining import inverted_lists
from SentimenAnalysis_NLP_DataMining.stemming import stemmer


class xml_parser:

    def __init__(self):
        self.data_dict = {};
        self.doc_ratings={};

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

        for el in tree.findall('DOC'):
            cat,rating,doc="","","";
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    doc=ch.text;
                if (ch.tag == "CLASS"):
                    cat=ch.text.strip().lower();
                if ch.tag == "rating":
                    rating=ch.text.strip();
                    self.doc_ratings[doc]=rating;
                if ch.tag == "TEXT":
                    text=ch.text.strip().split(' ');
                    #removing stop words and stemming.
                    processed_text=stemmer(text);
                    word_count=self.word_count(processed_text);
                    #print(word_count, doc, rating);
                    for word in word_count:
                            self.update_dict(il[cat],word,word_count[word],doc, rating);
                    if cat not in self.data_dict:
                        self.data_dict[cat]=[]
                    self.data_dict[cat].append(il[cat]);

    def update_dict(self, il, word,count,doc, r):
        if (word not in il):
            il[word] = inverted_lists.inverted_list();
        il[word].ratings.add(r)
        il[word].tf+=count;
        il[word].df += 1;
        doc=int(doc.strip())
        if doc in il[word].docs:
            il[word].docs[doc]+=count;
        else:
            il[word].docs[doc] =count;

    def word_count(self,text):
        d={};
        for w in text:
            if w not in d:
                d[w]=1;
            else:
                d[w]+=1;
        return d;

    def __iter__(self):
        return [self.data_dict,self.doc_ratings];