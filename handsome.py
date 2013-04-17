import json
from urllib.request import urlopen
from os import sep

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
result = json.load(f)

#result = json.load(open('resources.txt', 'r'))

package = "src"+sep+PACKAGE.replace(".", sep)+sep

for java in result:
    if java.has_key('source'):
        code = java['source'].decode('BASE-64')
        name = package+java['fileName']
        t = open(name, 'w+')
        t.write(code)
        t.close()


