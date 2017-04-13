import requests
import xmltodict

user = 'jssadmin'
pwd = 'jamf1234'
OK = 200

url = 'https://greenbay03.jamfcloud.com/JSSResource'
#   'https://jss.lan:8443/edu03/JSSResource/'

r = requests.get(url+'/mobiledevices', verify=False, auth=(user,pwd))

if r.status_code != OK:
   print('Uh-oh, status code is: ', r.status_code)
   exit()

newDict = xmltodict.parse(r.text)['mobile_devices']['mobile_device']

m = []
n = []

print "\n\n"
for f in newDict:
   n.append(f['name'])
   m.append(f['model'])
   print 'Username: %s, Name: %s, Model: %s' % (f['username'],f['name'],f['model'])

#print 'creating dictionary'
d = dict(zip(n, m))

#print 'print out dict of keys/values'
#for key in iter(d):
#   print key, d[key]
