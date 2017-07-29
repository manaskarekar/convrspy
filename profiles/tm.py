import sys
sys.path.insert(0, '../')
from ir import IR

import plistlib

def trim_alpha(color, trim = True):
	if trim and len(color[1:]) > 6:
		color = color.strip('#')
		color = '#' + color[2:]
	return color

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
	ir.fgcolor				= trim_alpha(settings[0]['settings'].get('foreground', default_light))
	ir.bgcolor				= trim_alpha(settings[0]['settings'].get('background', default_light))

	ir.keyword1				= trim_alpha(settings[7]['settings'].get('foreground', default_dark))
	ir.keyword2				= trim_alpha(settings[7]['settings'].get('foreground', default_dark))
	ir.keyword3				= trim_alpha(settings[7]['settings'].get('foreground', default_dark))
	ir.keyword4				= trim_alpha(settings[7]['settings'].get('foreground', default_dark))

	ir.comment1				= trim_alpha(settings[1]['settings'].get('foreground', default_dark))
	ir.digit				= trim_alpha(settings[3]['settings'].get('foreground', default_dark))
	ir.operator				= trim_alpha(settings[3]['settings'].get('foreground', default_dark)) #TODO: get the right one
	ir.function				= trim_alpha(settings[12]['settings'].get('foreground', default_dark))

	ir.literal1				= trim_alpha(settings[2]['settings'].get('foreground', default_light))
	ir.literal2				= trim_alpha(settings[2]['settings'].get('foreground', default_light))
	ir.literal3				= trim_alpha(settings[2]['settings'].get('foreground', default_light))
	ir.caretColor			= trim_alpha(settings[0]['settings'].get('caret', default_light))
	ir.selectionColor		= trim_alpha(settings[0]['settings'].get('selection', default_light))
	ir.eolMarkerColor		= trim_alpha(settings[0]['settings'].get('foreground', default_light))
	ir.lineHighlightColor 	= trim_alpha(settings[0]['settings'].get('lineHighlight', default_light))

	return ir

def write():
	pass