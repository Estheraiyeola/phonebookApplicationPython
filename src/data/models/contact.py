class Contact:
    def __init__(self):
        self.__i_d = 0
        self.__name = ''
        self.__address = ''
        self.__email = ''
        self.__telephone_number = ''
        self.__contact = None

    def set_id(self, i_d: int) -> None:
        self.__i_d = i_d

    def get_id(self) -> int:
        return self.__i_d

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_address(self, address: str) -> None:
        self.__address = address

    def get_address(self) -> str:
        return self.__address

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    def set_telephone_number(self, telephone_number: str) -> None:
        self.__telephone_number = telephone_number

    def get_telephone_number(self) -> str:
        return self.__telephone_number

    def set_contact(self, contact):
        self.__contact = contact
