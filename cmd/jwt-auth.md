https://apisix.apache.org/docs/apisix/3.10/plugins/jwt-auth/

# tool 1: https://jwt.io/#debugger-io 
## use for get the encoded token by setting up payload and verify signature
# tool 2: https://www.unixtimestamp.com/
## paload.exp use unix time, Y/M/D/H/M/S

# how to generate token ?
## set the 
### (1) PAYLOAD | key & exp 
#### key same with jwt-auth/key 
#### exp(unixtime) need to after now 
### (2) verify signature | secret-key
#### secret-key same with jwt-auth/secret

jwt_token=encoded token
curl http://127.0.0.1:9080 -H "Authorization: ${jwt_token}" -i









