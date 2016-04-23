from SentimenAnalysis_NLP_DataMining.parser import xml_parser
import statistics

def get_data():
    handler=xml_parser();
    handler.parse("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\sample.txt");
    outfile=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\inverted_list.txt", 'w');
    [p_dict,d_dict, word_vector]=handler.__iter__();
    '''
    print(d_dict);
    for c in p_dict:
        print("*****************"+c+"*********************")
        for words in p_dict[c]:
            s=words, p_dict[c][words].tf/p_dict[c][words].df, p_dict[c][words].docs, p_dict[c][words].ratings;
            outfile.write(str(s)+"\n")
            outfile.flush()
    outfile.close()
    '''
    [feature_matrix, response_matrix]=get_feature_matrix(variance_matrix(p_dict['camera'], d_dict, word_vector), p_dict['camera'], d_dict, word_vector);

# feature matrix in this case shall be a dict of arrays. Keys of dict will be the words, indices of array(values) coresponds to
# the each ratings in which the
def get_feature_matrix(var_matrix, p_dict, d_dict, wv):
    matrix = []
    response_matrix=[];
    word_vector = list(wv);
    i = 0;
    for d in d_dict:
        response_matrix.append(float(d_dict[d]));
        matrix.append([])
        for elem in var_matrix:
            print(elem[1]);
            key=int(d.strip());
            if elem[1] in p_dict and key in p_dict[elem[1]].docs:
                matrix[i].append(p_dict[elem[1]].docs[key]);
            else:
                matrix[i].append(0)
        i += 1;

    for i in range(0, len(matrix)):
        print(matrix[i]);
    return [matrix, response_matrix];

#takign variance of each term in the dict and removing all the terms with less than 0.5 variance
def variance_matrix(p_dict, d_dict, wv):
    matrix=[]
    i=0;
    word_vector=list(wv);
    for d in d_dict:
        matrix.append([])
        for term in word_vector:
            if term in p_dict and int(d.strip()) in p_dict[term].docs:
                matrix[i].append(p_dict[term].docs[int(d.strip())])
            else:
                matrix[i].append(0)
        i+=1;
    var_matrix=[];
    for i in range(0, len(matrix[0])):
        m=[]
        for j in range(0, len(matrix)):
            m.append(matrix[j][i]);
        v=statistics.variance(m);
        if(v>0.5):
            var_matrix.append((v, word_vector[i]));
    return var_matrix;

get_data()