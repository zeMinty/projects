#!/usr/bin/python3

from os import system as execute
from sys import argv as arguments
from re import IGNORECASE, compile as regex, match

print('::: Usage: python3 FILE -k PROCESSNAME')

asktokill = False
command = 'lsof -iTCP -sTCP:listen'

if len(arguments) > 1:
	if  arguments[1] in ('-k', '-kill'):
		procs = '|'.join(arguments[2::])
		asktokill = True
	else:
		procs = '|'.join(arguments[1::])

	if len(arguments) > 2 and asktokill or len(arguments) > 1 and not asktokill:
		command += " | awk '$0 ~ /(" +procs+ "|NAME)/ {print $0}'"


execute(command)

if asktokill:
	pattern = regex("(y|yes|n|no)", IGNORECASE)
	print("\n>>> kill $(" +command+ " | awk '$2 ~ /[0-9]+/ {print $2}')")
	while match(pattern, answer := input('# kill? [Y/n]: ')) is None:
		pass

	pattern = regex("(y|yes)", IGNORECASE)
	if (match(pattern, answer)):
		execute("kill $(" +command+ " | awk '$2 ~ /[0-9]+/ {print $2}')")

print('End.')
