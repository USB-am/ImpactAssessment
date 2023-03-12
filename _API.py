# -*- coding: utf-8 -*-


class Document:
	''' Представление шаблона.docx '''

	def __init__(self, path_to_template: str):
		self.path_to_template = path_to_template

	def __str__(self):
		return f'Document "{self.path_to_template}"'


class Model:
	def __init__(self):
		pass

	def construction_template_fields(self, doc: Document) -> str:
		' Возвращает html код шаблона '


class View:
	def __init__(self):
		pass


class Controller:
	def __init__(self, model: Model, view: View):
		self.model = model
		self.view = view

	def _binding_view_triggers(self) -> None:
		' Привязать события преставления с моделью '

	def construction_template_fields(self, doc: Document) -> None:
		' Построение UI для шаблона.docx '


class Application:
	def __init__(self):
		self.controller = Controller()
		self.model = Model()
		self.view = View()


if __name__ == '__main__':
	Application().run()