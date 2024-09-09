#!/usr/bin/env python3

def swap_keys_values(d):
    return dict((v,k) for k,v in d.items())
