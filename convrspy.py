import sys, os
import plistlib
import convert


if __name__=="__main__":
	if len(sys.argv) != 4:
		print "Incorrect number of args, usage: convrspy <filename> <source_format> <target_format>."
	else:
		if os.path.isdir(sys.argv[1]):
			for f in os.listdir(sys.argv[1]):
				filepath = os.path.join(sys.argv[1], f)
				if os.path.isdir(filepath):
					continue
				convert.convert(filepath, sys.argv[2], sys.argv[3])
		else:
			convert.convert(sys.argv[1], sys.argv[2], sys.argv[3])

	sys.exit()