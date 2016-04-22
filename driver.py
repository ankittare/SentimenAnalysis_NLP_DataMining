from SentimenAnalysis_NLP_DataMining.parser import xml_parser
import statistics

def get_data():
    handler=xml_parser();
    handler.parse("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\sample.txt");
    outfile=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\inverted_list.txt", 'w');
    [p_dict,d_dict, word_vector]=handler.__iter__();
    print(d_dict);
    for c in p_dict:
        print("*****************"+c+"*********************")
        for words in p_dict[c]:
            #print(words, p_dict[c][words])
            s=words, p_dict[c][words].tf/p_dict[c][words].df, p_dict[c][words].docs, p_dict[c][words].ratings;
            outfile.write(str(s)+"\n")
            outfile.flush()
    outfile.close()
    variance_matrix(p_dict['camera'], d_dict, word_vector)
    return p_dict

# feature matrix in this case shall be a dict of arrays. Keys of dict will be the words, indices of array(values) coresponds to
# the each ratings in which the
def get_feature_matrix():
    d=0;

def variance_matrix(p_dict, d_dict, word_vector):

    matrix=[]
    for d in d_dict:
        matrix.append([])
    for i in range(0, len(matrix)):
        for term in word_vector:
            if term in p_dict:
                matrix[i].append(p_dict[term].tf/p_dict[term].df)
            else:
                matrix[i].append(0)
    var_matrix=[];
    for i in range(0, len(matrix[0])):
        m=[]
        for j in range(0, len(matrix)):
            m.append(matrix[j][i]);
        print(m);
        var_matrix.append(statistics.variance(m));
    print(var_matrix)




get_data()