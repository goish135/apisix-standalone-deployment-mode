 https://github.com/apache/apisix/blob/master/conf/config.yaml.example
 - basic-auth                     # priority: 2520
 - jwt-auth                       # priority: 2510
 - key-auth                       # priority: 2500

 curl http://127.0.0.1:9080
 (basic-auth) curl -i -uapisix:apisix http://127.0.0.1:9080
 jwt_token=XXX
 (jwt-auth) curl http://127.0.0.1:9080 -H "Authorization: ${jwt_token}" -i
 (key-auth) curl http://127.0.0.1:9080 -H 'apikey: example-key' -i

# Disable the plugin
# Through the disable configuration, you can add a new plugin with disabled status and the request will not go through the plugin.

```
basic-auth: { 
  _meta: {
      "disable": true
  } }
```

