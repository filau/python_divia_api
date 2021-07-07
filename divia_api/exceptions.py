from sys import exit


class InvalidWay(Exception):
    def __init__(self):
        print("Exception: The way can only be “A” or “R”. Exiting.")
        exit(1)
