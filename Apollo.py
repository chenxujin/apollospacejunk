from Shepherd import *

def the_real_mccoy():
    """
    This is it. The Real McCoy.
    """
    s = Shepherd()
    s.setup('keys/',
            line_interval = 5,
            total_interval = 5000 )
    s.loop()

if __name__=="__main__":
    the_real_mccoy()


