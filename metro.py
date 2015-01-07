#!/usr/bin/env python

import sys,os
import subprocess
import urllib2
import time
import cPickle

stations = []
for i in range(0,115):
    url_str = "http://www.wmata.com/rider_tools/pids/showpid.cfm?station_id=" + str(i)
    url = urllib2.urlopen(url_str)
    lines = url.readlines()
    station_name = lines[5].strip()[7:-8]
    if station_name != '':
        stations.append([i,station_name,url_str])
        print stations[-1]
    time.sleep(0.1)