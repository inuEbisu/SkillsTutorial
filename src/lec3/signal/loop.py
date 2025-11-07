#!/usr/bin/env python
import signal, time


def sigint_handler(signum, time):
    print(f"\nI got a {signum}, but I am not stopping")


# signal.signal(signal.SIGINT, sigint_handler)
# signal.signal(signal.SIGTERM, sigint_handler)

i = 0
while True:
    time.sleep(0.1)
    print(f"{i}", end="\n")
    i += 1
