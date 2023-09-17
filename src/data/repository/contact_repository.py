import abc

from data.models.contact import Contact


class ContactRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, contact: Contact) -> Contact:
        pass

    @abc.abstractmethod
    def delete(self, contact: Contact):
        pass

    @abc.abstractmethod
    def find_by_id(self, i_d: int) -> Contact:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[Contact]:
        pass

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        pass
