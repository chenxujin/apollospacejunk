from Shepherd import *

def the_real_mccoy():
    """
    This is it. The Real McCoy.
    """
    s = Shepherd()
    s.setup('keys/',
            line_interval = 120,
            total_interval = 3000 )
    s.loop()

if __name__=="__main__":
    the_real_mccoy()


