import sys
sys.path.insert(0, '../')
from ir import IR

import plistlib

def read(source_file):
	try:
		lines = plistlib.readPlist(source_file)
	except:
		print "Error reading scheme file %s" % source_file
		return IR()

	if len(lines['settings']) < 13:
		print "Skipping file, not enough fields."
		return IR() #TODO: Handle this better

	settings = lines['settings']

	default_dark = "#000000" #TODO: pick a default color based on whether the theme is dark or light.
	default_light = "#FFFFFF"

	ir = IR()
	ir.name					= lines['name']
	ir.fgcolor				= settings[0]['settings'].get('foreground', default_light)
	ir.bgcolor				= settings[0]['settings'].get('background', default_light)

	ir.keyword1				= settings[7]['settings'].get('foreground', default_dark)
	ir.keyword2				= settings[7]['settings'].get('foreground', default_dark)
	ir.keyword3				= settings[7]['settings'].get('foreground', default_dark)
	ir.keyword4				= settings[7]['settings'].get('foreground', default_dark)

	ir.comment1				= settings[1]['settings'].get('foreground', default_dark)
	ir.digit				= settings[3]['settings'].get('foreground', default_dark)
	ir.operator				= settings[3]['settings'].get('foreground', default_dark) #TODO: get the right one
	ir.function				= settings[12]['settings'].get('foreground', default_dark)

	ir.literal1				= settings[2]['settings'].get('foreground', default_light)
	ir.literal2				= settings[2]['settings'].get('foreground', default_light)
	ir.literal3				= settings[2]['settings'].get('foreground', default_light)
	ir.caretColor			= settings[0]['settings'].get('caret', default_light)
	ir.selectionColor		= settings[0]['settings'].get('selection', default_light)
	ir.eolMarkerColor		= settings[0]['settings'].get('foreground', default_light)
	ir.lineHighlightColor 	= settings[0]['settings'].get('lineHighlight', default_light)

	return ir

def write():
	pass