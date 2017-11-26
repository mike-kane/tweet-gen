class Histogram(object):
    '''
    Class used to create and analyze a histogram of all words present in a corpus.


     '''

     def __init__(self, file_path):
         '''
         Initializes the histogram object.  Expects a path to the corpus as an input.

         Corpus must be in .txt format.
         '''
         pass

    def create_histogram(self):
        '''
        Helper function used to create the actual histogram object and populate it with counts
        for each unique word in the corpus.

        Takes no arguments.  Returns a dictionary with tokens as keys, count as values.
        '''
        pass

    def __clean_text(self):
        '''
        Cleans the tokens by:
            --removing punctation (excluding periods)
            --making all words lower case

        Returns a string containing the cleaned version of the text.
        '''
        pass
