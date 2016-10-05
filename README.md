# A Python3 IRC backdoor
A Proof of Concept (PoC) IRC backdoor written in Python3

First off, don't look at it as a backdoor, look at it as a software to manage your clients from an IRC channel. I know this looks bad but it can actually do some good ;)

I used a "Echo" code for starting the work. Going for pure Python3 with socket rather than using existing IRC clients for Python. I figured this is much more clean and easy to use.

# Working Right Now

Sending Commands through the IRC channel and get back stdout and stderr in there.
What else do you want? :-P

# Future Plan

1) Sending multi-line commands and bash scripts

2) Adding PGP security to backdoors rather than SSL

3) Adding File Transfer Feature

4) Sending back command responses in a text file

5) A lot more... 



# Relative Projects

* [Gcat](https://github.com/byt3bl33d3r/gcat), which uses Gmail as backend
* [Twittor](https://github.com/PaulSec/twittor), A fully featured backdoor that uses Twitter as a C&C server
