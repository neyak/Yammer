import json
import os
import shutil
import requests
import time
import requests.auth 
import urllib
import pandas as pd
import urllib2
from urllib2 import Request, urlopen
from pandas.io.json import json_normalize

access_token = "*************************"
headers = {"Authorization": "Bearer " + access_token}

import csv

#extract for a hashtag pass the tag id as first parameter
messages_abouttopic('XXXXXXX','',1,topicfolder)