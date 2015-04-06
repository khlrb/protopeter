#!/usr/bin/env python

import Prompt, Client

import sys

from pprint import pprint

port = int(raw_input("Which port should I listen on? "))

if len(sys.argv) < 3:
    c = Client.Client("", port)
else:
    c = Client.Client("", port, boot_host=sys.argv[1], boot_port=int(sys.argv[2]))


p = Prompt.Prompt(c)

pprint(p.commands.keys())

while c.running:
    p.prompt()
