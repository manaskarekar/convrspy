class IR(object):
	def __init__(self, *args):
		default_dark			= "#000000"
		default_light			= "#FFFFFF"
		self.name				= default_dark
		self.fgcolor			= default_light
		self.bgcolor			= default_dark 

		self.keyword1			= default_dark
		self.keyword2			= default_dark
		self.keyword3			= default_dark
		self.keyword4			= default_dark

		self.comment1			= default_dark
		self.digit				= default_dark
		self.operator			= default_dark
		self.function			= default_dark

		self.literal1			= default_dark
		self.literal2			= default_dark
		self.literal3			= default_dark
		self.caretColor			= default_dark
		self.selectionColor		= default_dark
		self.eolMarkerColor		= default_dark
		self.lineHighlightColor = default_dark

