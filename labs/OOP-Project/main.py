import requests
from pprint import pprint
from github import Github


class User:
	# all attrs protected and last private
	def __init__(self, username: str, age: int, main_language: str):
		self._username = username
		self._age = age
		self._main_language = main_language
		self.__main_lang_ext: str = self.__get_ext()

	def get_main_lang_ext(self):
		return self.__main_lang_ext

	# Переопределение
	def __str__(self):
		return f'USER: {self._username}\nAGE: {self._age}\nMAIN LANG: {self._main_language}\nEXT: {self.__main_lang_ext}'

	# Private method
	def __get_ext(self) -> str:
		match self._main_language.lower():
			case "javascript":
				return ".js"
			case "c++":
				return ".cpp"
			case "typescript":
				return ".ts"
			case "c":
				return ".c"
			case "kotlin":
				return ".kt"
			case "python":
				return ".py"
			case "java":
				return ".java"
			case "php":
				return ".php"
			case "assembler":
				return ".asm"
		return "UNKNOWN"


# Наследование
class AuthorizedUser(User):
	def __init__(self, username: str, age: int, main_language: str, password: int):
		super().__init__(username, age, main_language)
		self.password = password

	# Переопределение
	def __str__(self):
		return super().__str__() + f"\nPASSWORD: {self.password}"

	# TODO сделать метод вывода логина и пароль и переопределить его



if __name__ == "__main__":
	iam = User("altq33", 20, "JavaScript")
	iama = AuthorizedUser("altq33", 20, "TypeScript", "dkfjksjfkdf")
	print(iama)