# Copyright 2015 JChase II
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Addition permissions upon request on a case by case basis. 
#
# This is a pubsubhubbub subscriber that subscribes to and handles a youtube 
# channel subscription via the youtube API v.3 
print('Content-type: text/html\n') # So print actually prints to the webpage. w

import requests # Library for sending http requests. 
# imported to get raw data from GET requests. 
import os 
import sys 

# First, we send a subscription request to googles subscriber...

payload = {'hub.callback': 'insert-your-webhook-url', 
'hub.mode': 'subscribe', 'hub.verify': 'sync', 'hub.topic': 
'insert-topic-to-subscribe-to-here'}

returned = requests.post("https://pubsubhubbub.appspot.com/", data=payload)

# Check to make sure the hub responds with 204 or 202 (verified or accepted)

if returned != 204 or 202: 
    print ("Hub did not return 204 or 202")
    exit()

# Next, the hub needs to verify we sent a subscription request. 
# It'll send a GET request to the webhook including details of the 
# subscription... Also a hub.challenge. We must serve a 200 status and
# output hub.challenge in the response. 

Qdict = {}
QString = os.getenv("QUERY_STRING")
Qdict = dict(item.split("=") for item in QString.split("&"))

plzCheckTopic = Qdict['hub.topic'];
if (plzCheckTopic == 'insert-topic-to-subscribe-to'):
    print(Qdict["hub.challenge"]) 
    print("204")
else:
    print(404)



