from __future__ import absolute_import
from Components.Converter.Converter import Converter
from Components.Element import cached
from string import ascii_uppercase, ascii_lowercase
class TextCase(Converter):
	"""Converts a StaticText into upper/lower case."""
	UPPER = 0
	LOWER = 1

	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = self.UPPER
		if type == "ToLower":
			self.type = self.LOWER
		elif type == "ToUpper":
			self.type = self.UPPER

	@cached
	def getText(self):
		originaltext = self.source.getText()
		if self.type == self.UPPER:
			return originaltext.upper()
		elif self.type == self.LOWER:
			return originaltext.lower()
		else:
			return originaltext

	text = property(getText)
