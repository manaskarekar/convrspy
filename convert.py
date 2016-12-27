def read_source(source_file, source_format):
	pass #TODO: use importlib or something.

def convert(*args):
	source_file, source_format, target_format = args
	print source_file, source_format, target_format

	if source_format in ["paletton_txt", "pt"]:
		from profiles import paletton_txt
		source_data = paletton_txt.read(source_file)
	elif source_format in ["tmTheme", "tm"]:
		from profiles import tm
		source_data = tm.read(source_file)
	else:
		print "Invalid source format"

	#python handles duplicate imports, albeit with overhead, but we will usually convert from one to a different format.
	if target_format.lower() in [".jedit", "jedit"]:
		from profiles import jedit
		jedit.write(source_data)

