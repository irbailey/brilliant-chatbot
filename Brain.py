# Dependencies
import random
from abc import ABC, abstractmethod

class BrainInterface(ABC):
    """Interface for chatbot brains."""

    @abstractmethod
    def process(self, textfile) -> None:
        """Learn from an input file."""

    @abstractmethod
    def generate(self, context: str, noutput: int ) -> str:
        """Return text generated from the input string."""

class NGram(BrainInterface):
    """
    A class representing an nGram-based predictive text model.
    Attributes:
        nglen: int 
            The n-gram length + 1,
            e.g. nglen=3 implies that 2 words of context will be used to generate each new word.
        word_map: dictionary
            The map between each nglen-gram and the words which follow it in the input text.
        punctuation: str
            The string containing all the characters which will be removed when 
                                parsing the input text.
                                
    Methods:
    
        process(textfile)
            Populate the word_map using the text contained in the file textfile
        generate(context, noutput)
            Generate noutput words of text based on the words contained in the context string 
        
    """

    punctuation='.;,-“’”:?—‘!()_—'
    word_map={}
    nglen=2
    
        
    def set_len(self,nglen) -> None:
        """
        Sets the length of the nGram used in the word map
        Parameters
        ----------
            nglen: int
                    The n-gram length + 1
        """
        self.nglen=nglen
        
    def process(self,textfile) -> None:
        """
        Populate the word_map using the text (converted to lowercase and with the characters in the punctuation string removed) contained in the file textfile.

        Parameters
        ----------
            textfile: file object
                    The file to be parsed.
        """
        window=[]
        for line in textfile:
            for word in line.split():
                clean_word = word.strip(NGram.punctuation).lower()
                window.append(clean_word)
                if len(window) == self.nglen:
                  key = tuple(window[0:self.nglen-1])
                  value = window[self.nglen-1]
                  if key in self.word_map:
                    self.word_map[key].append(value)
                  else:
                    self.word_map[key] = [value]
                  window.pop(0)

    def generate(self,context,noutput) -> str:
        """
        Generate noutput words of text based on the words contained in the context string.
        
        Parameters
        ----------
            context: string
                    The string used to give the initial context (the first nglen words) to generate the next word from the word_map.
            noutput: int
                    The number of words of output to generate.
        """
        response=[]
        words=context.split()[0:self.nglen]
       
        for i in range(noutput):
            words.append("blah")
            response.append(words[0])
            next_words = self.word_map[tuple(list(words)[0:self.nglen-1])]
            words[self.nglen-1] = random.choice(next_words)
            words.pop(0)
        return " ".join(response)
 
