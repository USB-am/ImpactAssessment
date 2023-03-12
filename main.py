# -*- coding: utf-8 -*-

import config
from views import Application
# from logics.docx.document import DocumentTemplate


def main():
	# d1 = DocumentTemplate('templates\\template.docx')
	# d1.render({'title': 'Hello, world!', 'description': 'Test of template'})
	# d1.save('output.docx')
	Application().run()


if __name__ == '__main__':
	main()