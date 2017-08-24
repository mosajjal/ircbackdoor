# A Python3 IRC backdoor
A Proof of Concept (PoC) IRC backdoor written in Python3
NOT CONTINUED AS WE SPEAK

First off, don't look at it as a backdoor; look at it as a software to manage your clients from an IRC channel. I know this looks bad but it can actually do some good ;)

I used a "Echo" code for starting the work. Going for pure Python3 with socket rather than using existing IRC clients for Python. I figured this is much cleaner and easier to use.

# Working Right Now

Sending Commands through the IRC channel and get back stdout and stderr in there. 
NOT WORKING: canceling commands such as ping etc. So be careful when issuing commands.

# Future Plan

First, this entire backdoor is going to be re-written with Asyncio (partially done)

1) Sending multi-line commands and bash scripts

2) Adding PGP security to backdoors rather than SSL

3) Adding File Transfer Feature

4) Sending back command responses in a text file

5) Error handling and freeze/timeout detection

5) A lot more... 

* looks like Sending files/scripts and all [DCC](https://en.wikipedia.org/wiki/Direct_Client-to-Client) connections are a bit "too P2P" for a backdoor. So I'm staying out of it to find a better replacement for that feature. Although if you have a root backdoor there's SO MUCH you can do. I mean you might not even need file transfer/script features. Again, use responsibly ;-)

# Relative Projects

* [Gcat](https://github.com/byt3bl33d3r/gcat), which uses Gmail as backend.
* [Twittor](https://github.com/PaulSec/twittor), A fully featured backdoor that uses Twitter as a C&C server.
* Also checkout [BasicRAT](https://github.com/vesche/basicRAT), a cross-platform Python Remote Access Trojan (RAT).

# Notes

* Fork me, star me, give me pull requests

* Take a look at the code. Half (all?) the help and documentaiton is in there
