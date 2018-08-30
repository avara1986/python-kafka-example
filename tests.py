from __future__ import absolute_import, unicode_literals

import unittest
from time import sleep
from project.consumer import get_data
from project.producer import produce_message


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_test(self):
        value_to_send = "Ejecucion de test"
        print("Start")
        produce_message([value_to_send, ])

        print("Send data ok")
        count = 0
        data = False
        while count < 5 and not data:
            msg = get_data()
            if msg is None:
                sleep(1)
                count +=1
                continue
            if msg.error():
                sleep(1)
                count += 1
                print('Error: {}'.format(msg.value()))
                continue
            data = msg.value().decode('utf-8')
            print('Received message: {}'.format(data))
        self.assertEqual(data, value_to_send)
        print("Get data ok")
