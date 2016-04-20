class model:
    def __init__(self):
        self.docid = "";
        self.label = "";
        self.rating = "";
        self.product_class = "";
        self.text = "";
    def get_stopwords(self):
        stopwords=set([]);
        stopwords_file=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\stopwrods.txt");
        for lines in stopwords_file:
            stopwords.add(lines.strip());
        return stopwords;

    def __str__(self):
        return "DOCID: "+self.docid+"\nLABEL: "+self.label+"\nRATING: "+self.rating+"\nCLASS: "+self.product_class+"\nTEXT:"+"\n"+self.text;




