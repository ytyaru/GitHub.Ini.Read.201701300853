#!python3
#encoding:utf-8
import configparser
config = configparser.ConfigParser()
config.read('./git_up.ini')
print(config['GitHub']['Username'])
print(config['SQLite']['Apis'])
print(config['SQLite']['Accounts'])
print(config['sqlite']['repositories'])

