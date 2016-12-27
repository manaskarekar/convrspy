import sys
sys.path.insert(0, '../')

from ir import IR

def pick_color(line):
	return line.split()[3]

def read(source_file):
	with open(source_file, 'r') as f:
		lines = f.read().split('\n')

	ir = IR()
	ir.name					= source_file
	ir.fgcolor				= "#000000"
	ir.bgcolor				= "#FFFFFF"

	ir.keyword1				= pick_color(lines[7])
	ir.keyword2				= pick_color(lines[7])
	ir.keyword3				= pick_color(lines[7])
	ir.keyword4				= pick_color(lines[7])

	ir.comment1				= pick_color(lines[18])
	ir.digit				= pick_color(lines[25])
	ir.operator				= pick_color(lines[31])
	ir.function				= pick_color(lines[34])

	ir.literal1				= pick_color(lines[31])
	ir.literal2				= pick_color(lines[31])
	ir.literal3				= pick_color(lines[31])
	ir.caretColor			= pick_color(lines[31])
	ir.selectionColor		= pick_color(lines[31])
	ir.eolMarkerColor		= pick_color(lines[31])
	ir.lineHighlightColor 	= pick_color(lines[31])

	return ir

def write(ir):
	pass