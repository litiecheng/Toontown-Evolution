# Distribution:
distribution dev

# Audio:
audio-library-name p3openal_audio

# Art assets:
model-path ../resources

# Server:
server-version 2.4.1
shard-low-pop 25
shard-mid-pop 50
accountdb-type developer
min-access-level 600

# RPC:
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/

want-web-rpc #f
web-rpc-endpoint http://localhost:8000/rpc/

# DClass files (in reverse order):
dc-file astron/dclass/toon.dc
dc-file astron/dclass/otp.dc

# Core features:
want-pets #t
want-parties #f
want-cogdominiums #t
want-news-page #t 

# Chat:
want-whitelist #f

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t
want-resistance-dance #t

# Developer options:
show-population #t
force-skip-tutorial #t
want-instant-parties #t
