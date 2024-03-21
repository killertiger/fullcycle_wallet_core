from django.core.management.base import BaseCommand
from core.kafka.BalanceUpdatedKafkaListner import BalanceUpdatedKafkaListner


class Command(BaseCommand):
    def handle(self, *args, **options):
        listener = BalanceUpdatedKafkaListner()
        listener.start()