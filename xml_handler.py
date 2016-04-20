import xml.etree.cElementTree as et
from SentimenAnalysis_NLP_DataMining import model
from SentimenAnalysis_NLP_DataMining import inverted_lists
class xml_parser:

    def __init__(self):
        self.data_dict = {};
    # Call when an element starts

    def parse(self):
        sxml="";
        for lines in  open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\sample.txt"):
            sxml += lines
        tree=et.fromstring(sxml)
        il_auto = {};
        il_camera = {};
        m = model.model();
        sw = m.get_stopwords();
        for el in tree.findall('DOC'):
            print('-------------------');
            c="";
            r="";
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    m.docid=ch.text
                if (ch.tag == "CLASS"):
                    m.product_class = ch.text
                    c=ch.text.strip().lower();
                if ch.tag == "label":
                    m.label = ch.text
                if ch.tag == "rating":
                    m.rating = ch.text
                    r=ch.text.strip();
                if ch.tag == "TEXT":
                    m.text=ch.text.strip().split(' ');
                    df_updated={}
                    for word in m.text:
                        w=word.lower()
                        if w not in sw:
                            if(c=="camera"):
                                self.update_dict(il_camera,w, df_updated, r);
                            if (c == "auto"):
                                self.update_dict(il_camera, w, df_updated, r);
                    if ch not in self.data_dict:
                        self.data_dict[c]=[]
                    if c=="camera":
                        self.data_dict[c].append(il_camera);
                    elif c=="auto":
                        self.data_dict[c].append(il_auto);

    def update_dict(self, d, word, df_updated, r):
        if (word not in d):
            d[word] = inverted_lists.inverted_list();
        d[word].tf += 1;
        if (word not in df_updated):
            df_updated[word] = True;
            d[word].df += 1;
            d[word].ratings.add(r)

    def __iter__(self):
        return self.data_dict;