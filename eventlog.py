import hoover, hoover.utils
import json
import csv
import urllib2

protocol = 'http'
proxy = 'localhost:8080'
endpoint = "%s://%s/push" % (protocol, proxy)

if __name__=='__main__':
    #open the csv file
    file = r'C:\dev\www\eventlog.csv'
    f = open(file, 'rb')
    d = csv.DictReader(f)

    for row in d:
        message = json.dumps(row)
        req = urllib2.Request(endpoint, message, {'Content-Type': 'application/json'})
        url_f = urllib2.urlopen(req)
        response = url_f.read()
        url_f.close()
        #h.request(endpoint, 'POST', message)
    f.close()
