import xml.sax
from SentimenAnalysis_NLP_DataMining import model

class xml_handler( xml.sax.ContentHandler ):

    def __init__(self):
        self.CurrentData = ""
        self.docid = ""
        self.product_class = ""
        self.rating = ""
        self.label = ""
        self.text = ""
        self.product_class_dict = {};
    # Call when an element starts

    def startElement(self, tag, attributes):
        self.CurrentData = tag

   # Call when an elements ends
    def endElement(self, tag):
        pc="";
        rating="";
        t="";
        l="";
        d="";
        if self.CurrentData == "CLASS":
            pc=self.product_class;
        elif self.CurrentData == "rating":
            rating=self.rating
        elif self.CurrentData == "TEXT":
            t=self.text;
        elif self.CurrentData == "label":
            l=self.label;
        elif self.CurrentData == "DOCID":
            d=self.docid;
        m=model.model(d,l,rating,pc,t)
        if(l not in self.product_class_dict.keys()):
            self.product_class_dict[l]=[];
        self.product_class_dict[l].append(m);
        self.CurrentData="";

   # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "DOCID":
            self.docid = content
        elif self.CurrentData == "CLASS":
            self.product_class = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "label":
            self.label = content
        elif self.CurrentData == "TEXT":
            self.text = content

    def __iter__(self):
        return self.product_class_dict;

def main():
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = xml_handler()
    parser.setContentHandler( Handler );
    parser.parse("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\cleaned_d1.txt");
    print(Handler.__iter__());

main();
