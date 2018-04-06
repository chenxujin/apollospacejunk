import rainbowmindmachine as rmm
import logging

def setup():
    k = rmm.TxtKeymaker()
    k.make_keys('/home/charles/codes/apollospacejunk/bot/data/','/home/charles/codes/apollospacejunk/bot/keys/')
    
def run():
    sh = rmm.Shepherd('/home/charles/codes/apollospacejunk/bot/keys/',sheep_class=rmm.QueneauSheep)

    sh.perform_pool_action('tweet',{
            'publish' : False,
            'inner_sleep' : 3,#3*60,
            'outer_sleep' : 3,#2*3600,
            'lines_length' : 4
        })


if __name__=="__main__":
    #setup()
    run()
