from up.registrar import UpRegistrar


class Registrar(UpRegistrar):

    def __init__(self):
        super().__init__("time_logger_cog")

    def register(self):
        external_modules = self._load_external_modules
        if external_modules is not None:
            self._register_modules_from_file()
            return True
        return False
