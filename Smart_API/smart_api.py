# -*- coding: utf-8 -*-

import requests
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PySmart")


class PySmart:

    def __init__(self):
        self.content_type = 'application/json'
        self.nethash = 'fc46bfaf9379121dd6b09f5014595c7b7bd52a0a6d57c5aff790b42a73c76da7'
        self.version = '0.0.2'
        self.port = '8282'
        self.url = 'http://127.0.0.1:8282/mainnet/'

    def send_tx(self, recipient_id, amount, passphrase):
        """
        Use this method to send tx. On success the send tx will return True.
        :param recipient_id:
        :param amount:
        :param passphrase:
        :return:
        """
        try:
            # Prepare Tx
            headers = {
                'Content-Type': self.content_type,
            }

            data = '{"recipientId":"%s","amount":"%s","passphrase":"%s"}' % (recipient_id, amount, passphrase)

            url = self.url + 'transaction'

            response = requests.post(url=url, headers=headers, data=data)

            # Broadcast Tx
            jsonstr = response.json()

            id_ = jsonstr['transaction']['id']

            headers = {
                'content-type': self.content_type,
            }

            data = '{"id":"%s"}' % id_

            bdc_url = self.url + 'broadcast'

            response = requests.post(url=bdc_url, headers=headers, data=data)

            # check status of broadcast tx
            jsonstr_bct = response.json()
            success = jsonstr_bct['success']

            if success is True:
                return True
            else:
                return False
        except requests.ConnectionError:
            logger.critical("Connection Error. Couldn't connect to smartholdem API and get balance.")

            return False

    def get_balance(self, address):
        """
        Use this method to get balance. On success balance is returned.
        :param self:
        :param address:
        :return:
        """

        headers = {
            'accept': 'application/json',
        }

        url = self.url + 'account/' + address

        try:
            response = requests.get(url=url, headers=headers)
            jsonstr = response.json()

            # Сheck status
            success = jsonstr['success']

            if success is True:
                # Сheck balance
                balance = jsonstr['account']['balance']

                return balance
            else:
                return None
        except requests.ConnectionError:
            logger.critical("Connection Error. Couldn't connect to smartholdem API and get balance.")

            return False
