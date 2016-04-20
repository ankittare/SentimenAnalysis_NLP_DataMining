class inverted_list:
    def __init__(self):
        self.df=0;
        self.tf=0;
        self.ratings=set([]);
    def __str__(self):
        return "\nTERM FREQUENCY: "+str(self.tf)+"\nDOC FREQ: "+str(self.df)+"\nRATING: "+str(self.ratings)
