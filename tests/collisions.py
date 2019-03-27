
import os
import sys
#surely there's a better way
sys.path.append('/Users/steve/easyid')
import easy_id
import collections
loads=collections.defaultdict(dict)
#All this is necessary because the module can be loaded from
#other working directories.
curdirectory=os.path.dirname(__file__)
manifestfile=os.path.join(curdirectory,'manifest_lines.csv')

for line in open(manifestfile).readlines()[1:]:
    wo,load,profile,manifest=line.split(',')
    #strip crlf
    manifest=manifest[:-1]
    eid=easy_id.easy_id(profile+manifest)
    loads[load][(profile,manifest)]=eid    

    

print("There are %d loads"%len(loads.keys()))
print("There are %d profile/manifests"%sum([len(v.keys())for (k,v) in loads.items()]))
collision_count=0
for (k,v) in loads.items():
    collisions=collections.defaultdict(list)
    for (k1,v1) in v.items():
        if v1 in collisions:
            collisions[v1].append(k1)
            print("Collision in load %s:  %s goes to %s"%(k,v1,collisions[v1]))
            collision_count+=1
        else:
            collisions[v1].append(k1)    

print ("%d collisions within loads"%collision_count)