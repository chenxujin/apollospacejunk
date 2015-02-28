import rainbowmindmachine as rmm
import logging


def setup():
    k = rmm.TxtKeymaker()
    k.make_keys('data/')
    
def run():
    sh = rmm.Shepherd('keys/',sheep_class=rmm.QueneauSheep)

    #sh.perform_action('tweet',{'publish':False})
    sh.perform_pool_action('tweet',{
            'publish' : True,
            'inner_sleep' : 3*60,
            'outer_sleep' : 2*3600
        })


if __name__=="__main__":
    run()

