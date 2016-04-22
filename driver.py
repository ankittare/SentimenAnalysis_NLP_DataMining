from SentimenAnalysis_NLP_DataMining.parser import xml_parser
def get_data():
    handler=xml_parser();
    handler.parse("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\sample.txt");
    outfile=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\inverted_list.txt", 'w');
    [p_dict,d_dict]=handler.__iter__();
    print(d_dict);
    for c in p_dict:
        print("*****************"+c+"*********************")
        for d in p_dict[c]:
            for item in d:
                s=item, d[item].tf/d[item].df;
                outfile.write(str(s)+"\n");
                outfile.flush()
    outfile.close()
    return p_dict;

# feature matrix in this case shall be a dict of arrays. Keys of dict will be the words, indices of array(values) coresponds to
# the each ratings in which the
def get_feature_matrix():
    d=0;

def variance_matrix():
    x=0;


get_data();