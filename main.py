from keepme import *
import sys
import requests

passwds = sys.argv[1:]
for passwd in passwds:
    hashes, tail = request_data(passwd, requests.get)
    count = count_leaks(hashes, tail)
    if count:
        print(f"{passwd}: found {count} times")
    else:
        print(f"{passwd} is good to go no leak found..!!")
