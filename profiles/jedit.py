

def read():
	pass

def write(ir):
	data = \
"""#jEdit Editor Scheme
#:mode=properties:lineSeparator=\\n:
scheme.name=%s
view.fgColor=\\%s
view.bgColor=\\%s
view.gutter.fgColor=\\%s
view.gutter.bgColor=\\%s
view.gutter.highlightColor=\\%s
view.gutter.currentLineColor=\\%s
view.gutter.markerColor=\\%s
view.gutter.noFocusBorderColor=\\%s
view.gutter.focusBorderColor=\\%s
view.gutter.foldColor=\\%s
view.gutter.structureHighlightColor=\\%s
view.gutter.selectionAreaBgColor=\\%s
view.style.keyword1=color\:\\%s
view.style.keyword2=color\:\\%s
view.style.keyword3=color\:\\%s
view.style.keyword4=color\:\\%s
view.style.comment1=color\:\\%s
view.style.digit=color\:\\%s
view.style.operator=color\:\\%s
view.style.function=color\:\\%s
view.style.literal1=color\:\\%s
view.style.literal2=color\:\\%s
view.style.literal3=color\:\\%s
view.style.caretColor=\\%s
view.style.selectionColor=\\%s
view.style.eolMarkerColor=\\%s
view.style.lineHighlightColor=\\%s""" % \
\
(
ir.name,
ir.fgcolor,			
ir.bgcolor,
ir.fgcolor,			
ir.bgcolor,

ir.keyword1,
ir.lineHighlightColor,			
ir.keyword3,	
ir.bgcolor,
ir.fgcolor,	
ir.fgcolor,	
ir.bgcolor,	
ir.bgcolor,	

ir.keyword1,
ir.keyword2,
ir.keyword3,	
ir.keyword4,

ir.comment1,			
ir.digit,				
ir.operator,			
ir.function,

ir.literal1,			
ir.literal2,			
ir.literal3,			
ir.caretColor,			
ir.selectionColor,		
ir.eolMarkerColor,		
ir.lineHighlightColor,
)

	f = open(ir.name.split('.')[0] + ".jedit-scheme", 'w+') #get path to root
	f.write(data)