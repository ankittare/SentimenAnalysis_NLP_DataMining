from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

def stemmer(words):
    processed_words=[];
    for w in words:
        word=w.lower().strip()
        if word not in stopwords.words('english') and word!='':
            processed = WordNetLemmatizer().lemmatize(word, 'n')  # by Noun
            processed = WordNetLemmatizer().lemmatize(processed, 'v')  # by Verb
            processed_words.append(processed);
    return processed_words;


'''
s="i stumbled upon this camera after much research  its hard to understand why this camera is so hard to find when every pro review site has given it very high marks  i was considering the minolta dimage s404 canon g2 canon s40 olympus d40 pentax optio 430 before i discovered the casio  all of these cameras received good reviews but only the canon g2 was higher than the casio  however the casio uses the exact same lens as the canon g2  the casio is a great camera  when you first take it out of the box you realize that the camera is built very well  everything is laid out nicely  it comes with a neck strap that is very comfortable  i have used a 21 mgpxl camera for the last year and a half  it was a good camera but seemed to always be in the camera bag when i wanted to take a picture  on our last trip to disneyland i missed a lot of good shots  this camera has an excellent lens all glass and quality ccd sony  together they produce great pictures  i have three children the youngest is 7 weeks  i took a closeup of the youngest and printed an 8x10 to see how it would look using a hp photosmart p1000  it was astonishing  i could not see any pixelation whatsoever  without a magnifying glass there is no way you could tell it was digital  with the 41 megapixels you can reduce the size of the files and still have a very high quality output for emailing  this camera also has a ton of manual options that give you great control of your pictures  most of the manual settings are accessed with dial controls not through the menu  this is a plus this camera also uses nimh batteries  this is great because you will always have batteries ready to go  one pro review site rated this camera as one of the best theyd ever seen for battery life  they said they had no idea how casio achieved this but were glad they did  the memory type is very versatile as well  you can use compact flash type i and ii as well as a microdrive up to 1 gig  you will never run out of memory options here  the camera also has a very informative lcd threaded lens and external flash option  the camera looks good feels good and takes great pictures  factor in the relatively low cost and you have yourself a fun piece of equipment  i knew when i bought the 21 mgpxl camera it would be replaced quickly  however i know this camera will be around for a long time ";
s=s.split(' ');
print(s);
print(stemmer(s));

'''
