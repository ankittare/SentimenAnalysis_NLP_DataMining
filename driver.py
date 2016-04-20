from SentimenAnalysis_NLP_DataMining.xml_handler import xml_parser
def get_data():
    handler=xml_parser();
    handler.parse();
    p_dict=handler.__iter__();
    for c in p_dict:
        print("*****************"+c+"*********************")
        for d in p_dict[c]:
            for item in d:
                print(item, d[item].tf/d[item].df);
    return p_dict;

def get_feature_matrix:
    


get_data();