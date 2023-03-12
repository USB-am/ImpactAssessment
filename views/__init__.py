import eel


eel.init('templates\\ui')


class _Singleton(type):
	_instance = None

	def __call__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super(_Singleton, cls).__call__(*args, **kwargs)

		return cls._instance


class Application(metaclass=_Singleton):
	''' Базовое представление графической части '''

	def run(self) -> None:
		eel.start('index.html')