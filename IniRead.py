#!python3
#encoding:utf-8
from configparser import ConfigParser, ExtendedInterpolation
config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('./git_up.ini')
print(config['GitHub']['Username'])
print(config['SQLite']['Apis'])
print(config['SQLite']['Accounts'])
print(config['SQLite']['Repositories'])

