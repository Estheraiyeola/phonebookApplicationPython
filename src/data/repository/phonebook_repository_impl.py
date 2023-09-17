from data.models.phonebook import Phonebook
from data.repository.phonebook_repository import PhonebookRepository


class PhonebookRepositoryImpl(PhonebookRepository):
    def __init__(self):
        self.counter = 0
        self.phonebooks = []

    def save(self, phonebook: Phonebook) -> Phonebook:
        phonebook_does_not_exist = phonebook.get_id() == 0
        if phonebook_does_not_exist:
            self.save_new(phonebook)
        else:
            self.update(phonebook)
        return phonebook

    def delete(self, phonebook: Phonebook):
        self.phonebooks.remove(phonebook)

    def find_by_id(self, i_d: int) -> Phonebook:
        for phonebook in self.phonebooks:
            if phonebook.get_id() == i_d:
                return phonebook

    def find_all(self) -> list[Phonebook]:
        return self.phonebooks

    def count(self) -> int:
        return self.counter

    def clear(self) -> None:
        self.counter -= len(self.phonebooks)
        self.phonebooks.clear()

    def save_new(self, phonebook):
        phonebook.set_id(self.generate_id())
        self.phonebooks.append(phonebook)
        self.counter += 1

    def update(self, phonebook):
        updated_phonebook = self.find_by_id(phonebook.get_id())
        updated_phonebook.set_username()

    def generate_id(self) -> int:
        return self.counter + 1
