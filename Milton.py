from Shepherd import *

def make_keys():
    """
    This goes through each poem
    and asks, one by one, if you want to make a key for it.
    Then 'keys/' is populated.
    """
    keymaker = Keymaker()
    keymaker.make_keys('poems/')

def jonestown():
    """
    Every bot destroys its own history
    """
    s = Shepherd()
    s.setup('keys/')
    s.jonestown()

def the_real_mccoy():
    """
    This is it. The Real McCoy.
    """
    s = Shepherd()
    s.setup('keys/',
            line_interval = 60,
            poem_interval = 1800 )
    s.loop()

if __name__=="__main__":
    #make_keys()
    #jonestown()
    #test_loop()
    the_real_mccoy()

