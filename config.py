PORT = 443

TO_CLT_BUFSIZE = 262144
TO_TG_BUFSIZE = 262144

# name -> secret (32 hex chars)
USERS = {
    "tg":  "42aad8aa14b76f7bd88d381eeb5a896f",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "f66d4f6e5d64bf22f9b1782df72a398b"
