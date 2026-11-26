# Dependencies
import Brain 

class Bot:
    """
    A class representing a chatbot.
    Attributes:
        name: string 
            The name of the bot.
        brain: 
            The brain model which can process input text and predictively generate output.
       
    Methods:
    
        introduce()
            Print a greeting.
        respond(context, nwords)
            Return 'nwords' of response to the words in the string 'context'.  
        read(booklist)
            Loop over all the files listed in the list 'booklist', and use each one to train the bot's brain
            
    """

    def __init__(self,name,brain=Brain.NGram()):
        self.name=name
        self.brain=brain
        
    def introduce(self) ->None:
        """
        Print a greeting.
        """
        print("Hello, I'm", self.name)
        
    def respond(self,context,nwords=5) -> str:
        """
        Return 'nwords' of response to the words in the string 'context'.
        Parameters
        ----------
            context: str
                    The input string used to generate the response.
            nwords: int
                    The number of words of output to generate.
        """
        return self.brain.generate(context, nwords)
    
    def read(self,booklist) ->None:
        """
        Loop over all the files listed in the list 'booklist', and use each one to train the bot's brain.
        Parameters
        ----------
            booklist: list of str
                    A list of strings, where each string contains the filename of a file to be passed to the bot's brain.
        """
        for book in booklist:
            textfile=open(book)
            self.brain.process(textfile)

