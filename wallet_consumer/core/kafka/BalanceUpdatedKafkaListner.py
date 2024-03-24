from decimal import Decimal
import json
import threading
from confluent_kafka import Consumer, KafkaException

from core.models import Account

running=True
conf = {'bootstrap.servers': "kafka:29092",
        'auto.offset.reset': 'smallest',
        'group.id': "user_group"}

topic = 'balances'

class BalanceUpdatedKafkaListner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.consumer = Consumer(conf)

    def update_balance(self, account_id: str, balance: Decimal):
        account = Account.objects.filter(account_id=account_id).first()
        if account is None:
            account = Account(account_id=account_id)
        account.balance = Decimal(balance)
        account.save()

    def msg_process(self, msg):
        #Handle Message
        print('---------> Got message Processing.....')
        message = json.loads(msg.value().decode('utf-8'))
        
        print(message)
        
        self.update_balance(message['Payload']['account_id_from'], message['Payload']['balance_account_id_from'])
        self.update_balance(message['Payload']['account_id_to'], message['Payload']['balance_account_id_to'])

        print(message)

    def run(self):
        print("Starting BalanceUpdatedKafkaListner")
        try:
            self.consumer.subscribe([topic])
            while running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue
                
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    self.msg_process(msg)

        finally:
            self.consumer.close()

        print('BalanceUpdatedKafkaListner finished')

def shutdown():
    running = False