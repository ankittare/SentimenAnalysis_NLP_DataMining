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
        il_auto = {};
        il_camera = {};
        sw = self.get_stopwords();
        for el in tree.findall('DOC'):
            print('-------------------');
            c="";
            r="";
            d="";
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    d=ch.text;
                if (ch.tag == "CLASS"):
                    c=ch.text.strip().lower();
                if ch.tag == "rating":
                    r=ch.text.strip();
                if ch.tag == "TEXT":
                    text=ch.text.strip().split(' ');
                    df_updated={}
                    for word in text:
                        w=word.lower()
                        if w not in sw:
                            if(c=="camera"):
                                self.update_dict(il_camera,w, df_updated, r, d);
                            if (c == "auto"):
                                self.update_dict(il_camera, w, df_updated, r, d);
                    if ch not in self.data_dict:
                        self.data_dict[c]=[]
                    if c=="camera":
                        self.data_dict[c].append(il_camera);
                    elif c=="auto":
                        self.data_dict[c].append(il_auto);

    def update_dict(self, d, word, df_updated, r, doc):
        if (word not in d):
            d[word] = inverted_lists.inverted_list();
        d[word].tf += 1;
        if (word not in df_updated):
            df_updated[word] = True;
            d[word].df += 1;
            d[word].ratings.add(r)
            d[word].docs.add(doc)

    def get_stopwords(self):
        stopwords = set([]);
        stopwords_file = open(
            "C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\stopwrods.txt");
        for lines in stopwords_file:
            stopwords.add(lines.strip());
        return stopwords;

    def __iter__(self):
        return self.data_dict;