#/usr/bin/python

import urllib2

# proxy support
proxy = urllib2.ProxyHandler({'http': 'http://198.24.129.252:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

my_ip = urllib2.urlopen('http://whatthehellismyip.com/?ipraw').read()
print my_ip
