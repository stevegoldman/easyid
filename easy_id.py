#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:25:54 2019

@author: steve
"""
import random
import hashlib

NOUN_FILE='5_1_all_rank_noun.txt'
ADJECTIVE_FILE='5_3_all_rank_adjective.txt'


nouns=[n for n in[line.split()[0] for line in open(NOUN_FILE).readlines()] \
                  if len(n)>2 and len(n)<11]
adjectives=[a for a in[line.split()[0] for line in open(ADJECTIVE_FILE).readlines()] \
                       if len(a)>2 and len(a)<11]


def easy_id(some_value):
    norm_string=str(some_value).upper().encode('utf-8')
    m=hashlib.md5()
    m.update(norm_string)
    hd=m.hexdigest()
    # 16 upper bytes of the md5 hash
    ha=int(hd[:16],16)
    adj=adjectives[ha%len(adjectives)]
    # 16 lower bytes of the md5 hash
    hn=int(hd[17:],16)
    noun=nouns[hn%len(nouns)]
    return '%s %s'%(adj,noun)


if __name__=='__main__':
    
    print('There are %d nouns'%len(nouns))
    print('There are %d adjectives'%len(adjectives))
    print()
    
    for i in range(50):    
        print(easy_id(str(random.choice(range(1000000)))))
        
        