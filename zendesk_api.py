import requests

ALL_TIX = "https://{subdomain}.zendesk.com/api/v2/tickets.json"
TIX_DET = "https://{subdomain}.zendesk.com/api/v2/tickets/{tid}.json"

def format_subdomain(subdomain):
    """Formats subdomain into Zendesk api URL."""
    return ALL_TIX.format(subdomain=subdomain)

def format_ticket(subdomain, tid):
    """Formats Zendesk api URL to retrieve ticket details."""
    return TIX_DET.format(subdomain=subdomain, tid=tid)

def request(url, email, pw):
    """Returns tickets in JSON."""

    r = requests.get(url, auth=(email, pw))
    if r.status_code != 200:
        print('Status:', r.status_code, 'Problem with the request.')
    return r.json()
