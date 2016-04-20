from SentimenAnalysis_NLP_DataMining.xml_handler import xml_parser


def get_data():
    handler=xml_parser();
    handler.parse();
    p_dict=handler.__iter__();
    for c in p_dict:
        for item in p_dict[c]:
            print(item);
    return p_dict;