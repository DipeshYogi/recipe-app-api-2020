import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    """DJango command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for databasse...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database is not available, waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!!'))
