# coding: L1
from sys import addaudithook, exit


def audit(event, args):
    print('[!] Forbidden event: ' + event)
    exit(1)


addaudithook(audit)
