from docxtpl import DocxTemplate


class DocumentTemplate(DocxTemplate):
	''' Предавление файла-шаблона '''

	def __init__(self, path: str, context: dict={}):
		self.path = path
		self.context = context

		super().__init__(path)

	def __str__(self):
		return f'<DocumentTemplate "{self.path}">'