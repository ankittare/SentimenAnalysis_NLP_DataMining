import xml.etree.cElementTree as et
from SentimenAnalysis_NLP_DataMining import inverted_lists
class xml_parser:

    def __init__(self):
        self.data_dict = {};

    def parse(self, input):
        sxml="";
        for lines in  open(input):
            sxml += lines
        tree=et.fromstring(sxml)
        #map for auto, holding inverted list for word in auto category
        il_auto = {};
        # map for camera, holding inverted list for word in camera category
        il_camera = {};
        sw = self.get_stopwords();

        for el in tree.findall('DOC'):
            print('-------------------');
            cat="";
            rating="";
            doc="";
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    doc=ch.text;
                if (ch.tag == "CLASS"):
                    cat=ch.text.strip().lower();
                if ch.tag == "rating":
                    rating=ch.text.strip();
                if ch.tag == "TEXT":
                    text=ch.text.strip().split(' ');
                    #df_updated={}
                    word_count=self.word_count(text, sw);
                    for word in word_count:
                            if(cat=="camera"):
                                self.update_dict(il_camera,word,word_count[word],doc, rating);
                            if (cat == "auto"):
                                self.update_dict(il_auto, word,word_count[word], doc,rating);
                    if cat not in self.data_dict:
                        self.data_dict[cat]=[]
                    if cat=="camera":
                        self.data_dict[cat].append(il_camera);
                    elif cat=="auto":
                        self.data_dict[cat].append(il_auto);

    def update_dict(self, il, word,count,doc, r):
        if (word not in il):
            il[word] = inverted_lists.inverted_list();
        #il[word].tf += 1;
        #if (word not in df_updated):
        #    df_updated[word] = True;
            #il[word].df += 1;
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