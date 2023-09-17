import abc

from data.models.phonebook import Phonebook


class PhonebookRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, phonebook: Phonebook) -> Phonebook:
        pass

    @abc.abstractmethod
    def delete(self, phonebook: Phonebook):
        pass

    @abc.abstractmethod
    def find_by_id(self, i_d: int) -> Phonebook:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[Phonebook]:
        pass

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        pass
