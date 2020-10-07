#!/usr/bin/python3
"""
9. Load, add, save
"""


import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    filej = load_from_json_file("add_item.json")
except:
    filej = []

save_to_json_file(filej + sys.argv[1:], "add_item.json")
