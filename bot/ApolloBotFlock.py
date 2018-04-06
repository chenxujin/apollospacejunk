import rainbowmindmachine as rmm
import os, glob

DATADIR = os.path.join(os.getcwd(), 'data')
KEYSDIR = os.path.join(os.getcwd(), 'keys')
LIVE = False

def setup():
    k = rmm.TxtKeymaker()
    k.make_keys(DATADIR, KEYSDIR)
    
def run():
    sh = rmm.Shepherd(KEYSDIR, 
                      flock_name = 'apollo',
                      sheep_class=rmm.QueneauSheep)

    if not LIVE:
        sh.perform_pool_action('tweet',{
                'publish' : False,
                'inner_sleep' : 3,#3*60,
                'outer_sleep' : 3,#2*3600,
                'lines_length' : 4
            })
    else:
        sh.perform_pool_action('tweet',{
                'publish' : True,
                'inner_sleep' : 3*60,
                'outer_sleep' : 2*3600,
                'lines_length' : 4
            })


if __name__=="__main__":

    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR,"*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()

