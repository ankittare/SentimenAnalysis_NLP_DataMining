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
        for el in tree.findall('DOC'):
            print('-------------------');
            m = model.model();
            il_auto={};
            il_camera = {};
            c="";
            r="";
            sw=model.model.get_stopwords();
            for ch in el.getchildren():
                if(ch.tag=="DOCID"):
                    m.docid=ch.text
                if (ch.tag == "CLASS"):
                    m.product_class = ch.text
                    c=ch.text.strip().lower();
                if (ch.tag == "label"):
                    m.label = ch.text
                if (ch.tag == "rating"):
                    m.rating = ch.text
                    r=ch.text.strip();
                if (ch.tag == "TEXT"):
                    m.text=ch.text.strip().split(' ');
                    df_updated={}
                    for word in m.text:
                        w=word.lower()
                        if w not in sw:
                            if(c=="camera"):
                                if (w not in il_camera):
                                    il_camera[w] = inverted_lists.inverted_list();
                                il_camera[w].tf += 1;
                                if (w not in df_updated):
                                    df_updated[w] == True
                                    il_camera[w].df += 1;
                                    il_camera[w].ratings.add(r)
                            if (c == "auto"):
                                if (w not in il_auto):
                                    il_auto[w] = inverted_lists.inverted_list();
                                il_auto[w].tf += 1;
                                if (w not in df_updated):
                                    df_updated[w] == True
                                    il_auto[w].df += 1;
                                    il_auto[w].ratings.add(r)
            if ch not in self.data_dict:
                self.data_dict[c]=[]
            self.data_dict[c].append(m);
            
    def __iter__(self):
        return self.data_dict;