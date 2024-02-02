import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        reqUrl = f"{settings.OPENPAY_BASE_URL}/{settings.OPENPAY_COMMERCE_ID}/customers"
        token = f"{settings.OPENPAY_PRIVATE_KEY}:"
        headersList = {
            "Accept": "*/*",
        }

        payload = ""

        response = requests.request(
            "GET",
            reqUrl,
            auth=HTTPBasicAuth(token, ""),
            data=payload,
            headers=headersList
        )

        print(response.text)
