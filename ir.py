class IR(object):
	def __init__(self, *args):
		self.name				= None
		self.fgcolor			= None #: "#000000"
		self.bgcolor			= None #: "#FFFFFF"

		self.keyword1			= None #: lines[7]
		self.keyword2			= None #: lines[7]
		self.keyword3			= None #: lines[7]
		self.keyword4			= None #: lines[7]

		self.comment1			= None #: lines[18]
		self.digit				= None #: lines[25]
		self.operator			= None #: lines[31]
		self.function			= None #: lines[34]

		self.literal1			= None #: lines[31]
		self.literal2			= None #: lines[31]
		self.literal3			= None #: lines[31]
		self.caretColor			= None #: lines[31]
		self.selectionColor		= None #: lines[31]
		self.eolMarkerColor		= None #: lines[31]
		self.lineHighlightColor = None #: lines[31]

