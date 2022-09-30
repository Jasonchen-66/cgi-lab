#!/usr/bin/env python3

import os
import json

#create an empty dictionary
env = {}

#iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value

print("Content-type: application/json") #html is following
print() # blank line, end of headers

#print env dictionary in json format
print(json.dumps(env))