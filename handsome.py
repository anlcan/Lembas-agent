#! /usr/bin/env python3

import json
import argparse
import os

from shutil import rmtree

from urllib.request import urlopen
from base64 import b64decode

#HOST="http://sync-server.appspot.com/test"
DEFAULT_HOST="http://moxo.sync-server.appspot.com/"
#HOST="http://localhost:8888/"


parser = argparse.ArgumentParser(description='Handsome Service Code Generator')

parser.add_argument("-h", "--host", nargs=1, default=DEFAULT_HOST,
                    help="handsome codegen server addres, must have a trailing / ie:http://moxo.sync-server.appspot.com or http://localhost:8080/")

parser.add_argument('-t', '--target',nargs=1,required=True,
                   help=' target handsome server address ie:aott.nmdapps.com')

parser.add_argument('-s', '--service',nargs=1,required=True,
                   help=' target handsome service Name ie:AOTTService')

parser.add_argument('-p', '--package',nargs=1,default="com.handsome.services",
                   help='desired package named, used only if platform is android|java ie:com.nomad.aottservice')

parser.add_argument('-c', '--platform',default="objc",nargs=1,
                   help='platform to which code should be generated  java|android|objc|dotnet')

args = parser.parse_args()
print(args)



TARGET=args.target[0]
ENDPOINTNAME=args.service[0]
PACKAGE=args.package[0]
PLATFORM=args.platform[0]
HOST=args.host[0]

# TODO check missing parameters ?
url= "%s?target=%s&host=%s&endPoint=%s&port=80&header=no&package=%s&project=%s" % (HOST,PLATFORM,TARGET, ENDPOINTNAME, PACKAGE, ENDPOINTNAME)
print("fetching code", url)

f = urlopen(url)
response = f.readall().decode("utf-8")
result = json.loads(response)

#result = json.load(open('resources.txt', 'r'))

package = ENDPOINTNAME+os.sep
if PLATFORM in ['android', 'java']:
	package = "src"+os.sep+PACKAGE.replace(".", os.sep)+os.sep

try:
    #with open(package): pass
    # TODO backup generated directory before removing
    rmtree(package)
except IOError:
   print ('Oh dear.')

os.makedirs(package)

for classFile in result:
    if 'source' in classFile:
        code = b64decode(classFile['source'])
        name = package+classFile['fileName']
        t = open(name, 'w+')
        t.write(str(code,"utf-8"))
        t.close()


