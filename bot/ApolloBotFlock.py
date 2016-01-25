import rainbowmindmachine as rmm
import logging

LOG_FILE = "apollo_bot_flock_jan21.log"

def setup():
    k = rmm.TxtKeymaker()
    k.make_keys('/home/charles/codes/apollospacejunk/bot/data/')
    
def run():
    sh = rmm.Shepherd('/home/charles/codes/apollospacejunk/bot/keys/',sheep_class=rmm.QueneauSheep)

    #sh.perform_action('tweet',{'publish':False})
    sh.perform_pool_action('tweet',{
            'publish' : True,
            'inner_sleep' : 3*60,
            'outer_sleep' : 2*3600
        })


if __name__=="__main__":
    run()

