import json
from urllib.request import urlopen
from os import sep
from base64 import b64decode
from os import makedirs

#HOST="http://sync-server.appspot.com/test"
HOST="http://moxo.sync-server.appspot.com/"
#HOST="http://localhost:8888/"


TARGET="aott.nmdapps.com"
ENDPOINTNAME="AOTTService"
PACKAGE="com.nomad.aottservice"
PLATFORM="java"  # java|android|objc|dotnet


url= "%s?target=%s&host=%s&endPoint=%s&port=80&header=no&package=%s" % (HOST,PLATFORM,TARGET, ENDPOINTNAME, PACKAGE)
print(url)

f = urlopen(url)
response = f.readall().decode("utf-8")
result = json.loads(response)

#result = json.load(open('resources.txt', 'r'))

package = "src"+sep+PACKAGE.replace(".", sep)+sep
makedirs(package)

for java in result:
    if 'source' in java:
        code = b64decode(java['source'])
        name = package+java['fileName']
        t = open(name, 'w+')
        t.write(str(code,"utf-8"))
        t.close()


