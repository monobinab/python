#!/usr/bin/python
__author__ = 'msaha'

new_cnt = "/appl/rts/flume_audit/jboss/new_cnt/000000_0"
old_cnt = "/appl/rts/flume_audit/jboss/old_cnt/000000_0"

new_cnt_handler = open(new_cnt, 'r').readlines()
print new_cnt_handler
old_cnt_handler = open(old_cnt, 'r').readlines()
print old_cnt_handler