This is a work in progress if we do not want to use Tarzan as web proxy, and instead would like to e.g. use the Caddy proxy with the jwt module (https://caddyserver.com/docs/jwt). 

Caddy is **much** easier to setup and configure than Kong. A drawback though is that if we start generating JWT tokens with a script similar to these then we will stumble across other issues like how do we revoke a token? 

Some resources: 

- https://jwt.io/introduction/
- https://github.com/BTBurke/caddy-jwt
- https://github.com/BTBurke/caddy-jwt/issues/3
- https://github.com/mholt/caddy/issues/246
- https://pyjwt.readthedocs.org/en/latest/
- http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html
- http://dghubble.com/blog/posts/json-web-tokens-and-go/
