import logging
from optparse import OptionParser
from schwab import SchwabBrowser
import sys

logger = logging.getLogger(__name__)


def main():
    parser = OptionParser()
    parser.add_option("-u", dest="user_id", action="store")
    parser.add_option("-p", dest="password", action="store")
    options, args = parser.parse_args()
    if args[0] == 'getbalance':
        br = SchwabBrowser(options.user_id, options.password)
        balance = br.get_balance()
        print "Balance is $%.2f." % balance
    else:
        logger.error("Unknown arg value: %s." % args[0])


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    main()
