#! /usr/bin/python

from requests import post
import sys

url = "https://discord.com/api/webhooks/1192566501308370964/73rta6X36fGkxrsv54PqPmSdw221V6h_I7YO2uoFi29T7dwNP8ugiYeGa_NVdcUTh61V"

with open(sys.argv[1], 'r') as f:
    post(url, data={"content": f.read()})
