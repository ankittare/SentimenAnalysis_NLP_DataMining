import re;
def clean():
    #TODO: fix bug of  &quot;infinity&quot; line truncating
    f=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\D1.txt", 'r', encoding="utf8");
    o=open("C:\\Users\\Ankit\\Documents\\Programming\\devpy\\SentimenAnalysis_NLP_DataMining\\data\\cleaned_d1.txt", 'w', encoding="utf8");
    flag=False;
    for lines in f:
        if lines!="":
            if(flag!=True):
                s=lines;
            if("<label>" in lines):
                s=s.strip()+'</label>';
            elif("<rating>" in lines):
                s=s.strip()+"</rating>"
            elif("<TEXT>" in lines):
                flag=True;
                o.write(s.strip().replace("<br><br>", "") + "\n");
                s="";
                continue;
            elif(flag == True and "</DOC>" not in lines):
                s += lines.strip() + " ";
                continue;
            elif("</DOC>" in lines):

                s=re.sub('[^0-9a-zA-Z ]+', "", s)
                s =s.lower()+ "</TEXT>\n</DOC>"
                flag=False
            if(flag!=True):
                o.write(s.strip().replace("<br><br>","")+"\n");
            else:
                o.write(s.strip().replace("<br><br>", "") + " ");
            o.flush()
    o.close()

def clean_text(s):
    news=""
    for i in range(0, len(s)):
        if ord(s[i].lower()) >= 97 or ord(s[i].lower()) <= 123 or s[i]==" ":
            news+=s[i]
    return news
clean()