from data.models.contact import Contact
from data.repository.contact_repository import ContactRepository


class ContactRepositoryImpl(ContactRepository):
    def __init__(self):
        self.__contacts = []
        self.__counter = 0

    def save(self, contact: Contact) -> Contact:
        contact_does_not_exist = contact.get_id() == 0
        if contact_does_not_exist:
            self.save_new(contact)
        else:
            self.update(contact)

    def delete(self, contact: Contact):
        self.__contacts.remove(contact)

    def find_by_id(self, i_d: int) -> Contact:
        for contact in self.__contacts:
            if contact.get_id() == i_d:
                return contact

    def find_all(self) -> list[Contact]:
        return self.__contacts

    def count(self) -> int:
        return self.__counter

    def clear(self) -> None:
        self.__counter += len(self.__contacts)
        self.__contacts.clear()

    def save_new(self, contact) -> None:
        contact.set_id(self.generate_id())
        self.__contacts.append(contact)
        self.__counter += 1

    def update(self, contact) -> None:
        updated_contact = self.find_by_id(contact.get_id())
        updated_contact.set_contact(contact.set_contact())

    def generate_id(self) -> int:
        return self.__counter + 1
