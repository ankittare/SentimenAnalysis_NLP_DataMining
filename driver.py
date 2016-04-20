from SentimenAnalysis_NLP_DataMining.xml_handler import xml_parser
def get_data():
    handler=xml_parser();
    handler.parse("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\sample.txt");
    p_dict=handler.__iter__();
    for c in p_dict:
        print("*****************"+c+"*********************")
        for d in p_dict[c]:
            for item in d:
                print(item, d[item].ratings, d[item].docs);
    return p_dict;

# feature matrix in this case shall be a dict of arrays. Keys of dict will be the words, indices of array(values) coresponds to
# the each ratings in which the
def get_feature_matrix():
    d=0;


get_data();