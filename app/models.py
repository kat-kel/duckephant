import os

from app.forms import ConnectionForm


class User:
    def __init__(self, form: ConnectionForm | None = None) -> None:
        if form:
            self.username = form.username.data
            self.password = form.password.data
            self.port = str(form.port.data)
            self.host = form.host.data
            self.database_name = form.database.data
            self.authenticated = True
        else:
            self.username = self.get_env_var("POSTGRES_USERNAME")
            self.password = self.get_env_var("POSTGRES_PASSWORD")
            self.port = self.get_env_var("POSTGRES_PORT")
            self.host = self.get_env_var("POSTGRES_HOST")
            self.database_name = self.get_env_var("POSTGRES_DB_NAME")
            authenticated = self.get_env_var("DUCKEPHANT_USER_AUTHENTICATED")
            if authenticated == "True":
                self.authenticated = True
            else:
                self.authenticated = False
        print(self.__dict__)
        self.set_vars()

    def get_env_var(self, key: str) -> str | None:
        v = os.environ.get(key)
        if not v or v == "":
            return None
        else:
            return v

    def set_vars(self):
        os.environ["POSTGRES_USERNAME"] = self.username or ""
        os.environ["POSTGRES_PASSWORD"] = self.password or ""
        os.environ["POSTGRES_PORT"] = self.port or ""
        os.environ["POSTGRES_HOST"] = self.host or ""
        os.environ["POSTGRES_DB_NAME"] = self.database_name or ""
        os.environ["DUCKEPHANT_USER_AUTHENTICATED"] = str(self.authenticated) or ""
