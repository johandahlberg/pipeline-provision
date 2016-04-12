#!/usr/bin/env python

import os
import datetime
import jwt 

secret = open("secret.key").read()

client_id = os.getlogin() # the user issuing this token 

user = raw_input("Enter the token's user: ")
role = raw_input("Enter the token's role: ")

issued_at = datetime.datetime.utcnow()
expire_at = issued_at + datetime.timedelta(days = 7) # TODO: expire token later in the future 

payload = {
	'iss': '', # issuer claim
	'aud': '', # audience claim
	'iat': '', # issued at claim
	'exp': '', # expiration time claim
	'user': '', # our internal user claim
	'role': '' # our internal role claim
}

jwt_token = jwt.encode(payload, secret, algorithm='HS256')

print "Our secret token for user {0} is created.".format(user)
print "Token: {0}".format(jwt_token)
print "Expire at: {0}".format(expire_at)
print "Role: {0}".format('')

# TODO: Save this in a file in a subdirectory that will act as our database. 
