class DictSmart_t:
    __data = {}
    __default_value: object

    def __init__(self, default_value: object) -> None:
        self.__default_value = default_value
        pass

    def __getitem__(self, key):
        try:
            ret = self.__data[key]
            return ret
        except:
            return self.__default_value

    def __str__(self) -> str:
        return str(self.__data)

    def __setitem__(self, key, value):
        self.__data[key] = value