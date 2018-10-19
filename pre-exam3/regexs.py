import re

nospace = re.compile('\S+')

quotation = re.compile('"[^ ][^"]+[^ ]"')

twonum = re.compile('(-?[0-9]+(\.[0-9]+)?)(,| |, )(-?[0-9]+(\.[0-9]+)?)') # I got this idea from TA Irena Huang

likely_name =re.compile('[A-Z]([a-z]+|.)( [A-Z][a-z]+){1,2}')