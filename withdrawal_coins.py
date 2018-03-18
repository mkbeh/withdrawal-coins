# -*- coding: utf-8 -*-

import datetime
import logging

import const

from Smart_API import smart_api


smartapi = smart_api.PySmart()

# Set logger
logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)

fh = logging.FileHandler('tx.log')
logger.addHandler(fh)


def main():
    """
    This tool send all coins from current address to recipient address.
    """
    print(const.LOGO)

    fee = 10000000

    dt = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    balance = int(smartapi.get_balance(const.ADDRESS))

    if balance > 10000000:
        result = smartapi.send_tx(const.RECIPIENT_ID, (balance - fee), const.PASSPHRASE)

        balance = balance / 100000000

        if result is True:
            logger.info('From {0} send {1} to {2} at {3}.'.format(const.ADDRESS, balance, const.RECIPIENT_ID, dt))


if __name__ == "__main__":
    main()
