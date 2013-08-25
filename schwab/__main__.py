import logging
from optparse import OptionParser
from time import time
from schwab import SchwabBrowser
import sys

logger = logging.getLogger(__name__)


def main():
    parser = OptionParser()
    parser.add_option("-u", dest="user_id", action="store")
    parser.add_option("-p", dest="password", action="store")
    parser.add_option("-t", dest="tsv", action="store_true",
        "Print line of tab-separated timestamp and balance values. "
        "Good for piping/appending to a text file.")
    options, args = parser.parse_args()
    if args[0] == 'getbalance':
        br = SchwabBrowser(options.user_id, options.password)
        balance = br.get_balance()
        if options.tsv:
            print "%s\t%.2f" % (time(), balance)
        print "Balance is $%.2f." % balance
    else:
        logger.error("Unknown arg value: %s." % args[0])


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    main()
