import requests
import time

subdomains = ['cart.amazon.com', 'favourites.amazon.com', 'checkout.amazon.com']
def checkstatus(subdomain):
    try:
        response = requests.get(f'http://{subdomain}', timeout=5)
        if response.status_code == 200:
            return 'server_is_Up'
        else:
            return 'Down'
    except:
        return 'Server_is_Down'
print('Subdomain\tStatus')


while True:
    for subdomain in subdomains:
        status = checkstatus(subdomain)
        print(f'{subdomain}\t{status}')
    time.sleep(60)
