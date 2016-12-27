import sys
sys.path.insert(0, '../')
from ir import IR

import plistlib

def read(source_file):
	lines = plistlib.readPlist(source_file)
	settings = lines['settings']

	ir = IR()
	ir.name					= lines['name']
	ir.fgcolor				= settings[0]['settings']['foreground']
	ir.bgcolor				= settings[0]['settings']['background']

	ir.keyword1				= settings[7]['settings']['foreground']
	ir.keyword2				= settings[7]['settings']['foreground']
	ir.keyword3				= settings[7]['settings']['foreground']
	ir.keyword4				= settings[7]['settings']['foreground']

	ir.comment1				= settings[1]['settings']['foreground']
	ir.digit				= settings[3]['settings']['foreground']
	ir.operator				= settings[3]['settings']['foreground'] #double check this 
	ir.function				= settings[12]['settings']['foreground']

	ir.literal1				= settings[2]['settings']['foreground']
	ir.literal2				= settings[2]['settings']['foreground']
	ir.literal3				= settings[2]['settings']['foreground']
	ir.caretColor			= settings[0]['settings']['caret']
	ir.selectionColor		= settings[0]['settings']['selection']
	ir.eolMarkerColor		= settings[0]['settings']['foreground']
	ir.lineHighlightColor 	= settings[0]['settings']['lineHighlight']

	return ir
 
def write():
	pass