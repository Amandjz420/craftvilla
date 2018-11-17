from datetime import datetime

from .models import Truck


def check_for_expiry():
    Truck.objects.filter(expiration__lte=datetime.now()).update(status=3)
