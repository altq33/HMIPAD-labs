import os

import requests
from pprint import pprint
from github import Github


class User:
    # all attrs protected and last private
    def __init__(self, username: str, age: int, main_language: str):
        self.username = username
        self._age = age
        self._main_language = main_language
        self.__main_lang_ext: str = self.__get_ext()

    def get_main_lang_ext(self):
        return self.__main_lang_ext

    def change_username(self, new_login: str):
        self.username = new_login

    # Переопределение
    def __str__(self):
        return f'USER: {self.username}\nAGE: {self._age}\nMAIN LANG: {self._main_language}\nEXT: {self.__main_lang_ext}'

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
    def __init__(self, username: str, age: int, main_language: str, password: str, access_token: str):
        super().__init__(username, age, main_language)
        self.__password = password
        self.__access_token = access_token

    def get_password(self):
        return self.__password

    def get_access_token(self):
        return self.__access_token

    # Переопределение
    def __str__(self):
        return super().__str__() + f"\nPASSWORD: {self.__password}"

    # Перегрузка метода (костыльная без либ)
    def change_password(self, old_pas: str, new_pas: str, login: str | None = None):
        if not login:
            if old_pas == self.__password:
                self.__password = new_pas
                return
        else:
            if old_pas == self.__password and login == self.username:
                self.__password = new_pas
                return
        print("password or login do not match")


# Класс для работы с GITHUB API
class GithubChecker:
    __github_instance = Github()
    __base_url = "https://api.github.com/users/"

    def __init__(self, user: User | AuthorizedUser):
        self.is_auth = True if isinstance(user, AuthorizedUser) else False
        self.user_data = None
        self.__user = user
        self.__user_api_url = self.__base_url + self.__user.username
        if self.is_auth:
            self.__auth_github_instance = Github(user.get_access_token())

    # Тут выводим основную информацию
    def show_main_data(self):
        if not self.user_data:
            self.user_data = requests.get(self.__user_api_url).json()
        followers = [i["login"] for i in requests.get(self.user_data["followers_url"]).json()]
        print(f'Username: {self.user_data["login"]}\nName: {self.user_data["name"]}\nlocation: {self.user_data["location"]}\n '
              f'URL: {self.user_data["html_url"]}\nfollowers: {followers}')

    def define_favorite_lang(self):
        languages = {}
        repos = requests.get(self.__user_api_url + "/repos").json()
        for i in repos:
            if i["language"] in languages.keys():
                languages[i["language"]] += 1
            else:
                languages[i["language"]] = 1
        print(f"Favorite language of {self.__user.username} is {max(languages, key=languages.get)}")

    def get_js_ts_files_from_repos(self):
        path = 'C:\MyProjects\HMIPAD-labs\labs\OOP-Project\js-ts-from-repo'
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            for repo in self.__auth_github_instance.get_user().get_repos():
                for content in repo.get_contents(""):
                    if content.path.endswith(".js") or content.path.endswith(".ts") or content.path.endswith(".tsx"):
                        filename = os.path.join("js-ts-from-repo", f"{repo.full_name.replace('/', '-')}-{content.path}")
                        with open(filename, "wb") as f:
                            f.write(content.decoded_content)
        except Exception as e:
            print(e)

    def search_repo(self, request: str):
        for repo in self.__github_instance.search_repositories(request):
            pprint(repo)


if __name__ == "__main__":
    altq33 = AuthorizedUser("username", 20, "Typescript", "PASSWORD", "access token")
    g = GithubChecker(altq33)
    g.search_repo("React")
    # и можно потестить другие методы, но нужно правильно создать юзера.
