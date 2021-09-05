import subprocess
import sys
import logging
import time
import salt.utils

# get some parameters
logging.basicConfig()
log = logging.getLogger(__name__)
print('Number of arguments: ' + str(len(sys.argv)))
print('Argument List: ' + str(sys.argv))
#print('testing salt:' + __salt__)

if len(sys.argv) < 3:
    log.error("Please specify which config & engine you want to deploy to, for example: cm_deploy.py <au/uk> <1-20>")
    sys.exit("params not set")


def _synchronize_config(config):
    try:
        log.info("synchronizing config :" + config)
        subprocess.call(['/usr/local/siteminder/bin/synchronize-config.sh config-' + config])
        subprocess.call(['/usr/local/siteminder/bin/synchronize-exploded.sh'])
        subprocess.call(['/usr/local/siteminder/bin/synchronize-summary.rb'])
    except:
        log.error('Unexpected error has occured during synchronizing ' + config, sys.exc_info()[0])
        sys.exit('stopping automated deployment due to error on sync')


def _stop_engine(engine):
    try:
        subprocess.call(['/usr/local/siteminder/bin/stop-engine.sh engines/engine-' + str(engine)])
    except:
        log.error('Unexpected error has occured during stopping engine ' + str(engine), sys.exc_info()[0])
        sys.exit('stopping automated deployment due to stop engine')


def _start_engine(engine):
    try:
        subprocess.call(['/usr/local/siteminder/bin/start-engine.sh engines/engine-' + str(engine)])
    except:
        log.error('Unexpected error has occured during check running engine ' + str(engine), sys.exc_info()[0])
        sys.exit('stopping automated deployment due to check running engine v2')


def _check_running_engines(engine):
    try:
        proc1 = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', 'engine-' + engine], stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out,err = proc2.communicate()
        print('out: {0}'.format(out))
        print('err: {0}'.format(err))
    except:
        log.error('Unexpected error has occured during check running engine ' + str(engine), sys.exc_info()[0])
        sys.exit('stopping automated deployment due to check running engine v2')


_synchronize_config(sys.argv[1])
_stop_engine(sys.argv[2])
time.sleep(30)
_check_running_engines(sys.argv[2])
#_start_engine(sys.argv[2])

print('Congrats! deployment has been completed!')


