import sys, os
import plistlib
import convert


if __name__=="__main__":
	if len(sys.argv) != 4:
		print "Incorrect number of args, usage: convrspy <filename> <source_format> <target_format>."
	else:
		convert.convert(sys.argv[1], sys.argv[2], sys.argv[3])

	sys.exit()