from unittest import TestCase

from data.models.contact import Contact
from data.repository.contact_repository_impl import ContactRepositoryImpl


class TestCaseForContactRepository(TestCase):
    def setUp(self) -> None:
        self.contact_repository = ContactRepositoryImpl()

    def test_that_one_contact_can_be_added(self):
        self.contact = Contact()
        self.contact_repository.save(self.contact)

        self.assertEqual(1, self.contact_repository.count())

    def test_that_one_contact_can_be_added_and_found(self):
        self.contact = Contact()
        self.contact.set_name('esther')
        self.contact.set_contact('08138112782')
        self.contact_repository.save(self.contact)

        self.assertEqual(1, self.contact_repository.count())
        self.assertEqual('esther', self.contact_repository.find_by_id(1).get_name())

    def test_that_one_contact_can_be_added_and_updated(self):
        self.contact = Contact()
        self.contact.set_name('esther')
        self.contact_repository.save(self.contact)

        self.assertEqual(1, self.contact_repository.count())
        self.assertEqual(self.contact.get_name(), self.contact_repository.find_by_id(1).get_name())

        self.updated_phonebook = self.contact_repository.find_by_id(1)
        self.updated_phonebook.set_name('Esther')

        self.assertEqual('Esther', self.contact_repository.find_by_id(1).get_name())

    def test_that_contacts_can_be_added_and_can_all_be_printed_at_the_same_time(self):
        self.contact1 = Contact()
        self.contact1.set_name('esther')
        self.contact_repository.save(self.contact1)

        self.assertEqual(1, self.contact_repository.count())
        self.assertEqual('esther', self.contact_repository.find_by_id(1).get_name())

        self.contact2 = Contact()
        self.contact2.set_name('Esther')
        self.contact_repository.save(self.contact2)

        self.assertEqual(2, self.contact_repository.count())
        self.assertEqual('Esther', self.contact_repository.find_by_id(2).get_name())

        self.contact3 = Contact()
        self.contact3.set_name('Esteri')
        self.contact_repository.save(self.contact3)

        self.assertEqual(3, self.contact_repository.count())
        self.assertEqual('Esteri', self.contact_repository.find_by_id(3).get_name())

        self.expected_list = [self.contact1, self.contact2, self.contact3]
        self.assertEqual(self.expected_list, self.contact_repository.find_all())

    def test_that_a_contact_can_be_added_can_be_deleted(self):
        self.contact1 = Contact()
        self.contact1.set_name('esther')
        self.contact_repository.save(self.contact1)

        self.assertEqual(1, self.contact_repository.count())
        self.assertEqual('esther', self.contact_repository.find_by_id(1).get_name())

        self.contact2 = Contact()
        self.contact2.set_name('Esther')
        self.contact_repository.save(self.contact2)

        self.assertEqual(2, self.contact_repository.count())
        self.assertEqual('Esther', self.contact_repository.find_by_id(2).get_name())

        self.contact3 = Contact()
        self.contact3.set_name('Esteri')
        self.contact_repository.save(self.contact3)

        self.assertEqual(3, self.contact_repository.count())
        self.assertEqual('Esteri', self.contact_repository.find_by_id(3).get_name())

        self.contact_repository.delete(self.contact2)
        self.assertIsNone(self.contact_repository.find_by_id(2))

    def test_that_all_contacts_can_be_cleared(self):
        self.contact1 = Contact()
        self.contact1.set_name('esther')
        self.contact_repository.save(self.contact1)

        self.assertEqual(1, self.contact_repository.count())
        self.assertEqual('esther', self.contact_repository.find_by_id(1).get_name())

        self.contact2 = Contact()
        self.contact2.set_name('Esther')
        self.contact_repository.save(self.contact2)

        self.assertEqual(2, self.contact_repository.count())
        self.assertEqual('Esther', self.contact_repository.find_by_id(2).get_name())

        self.contact3 = Contact()
        self.contact3.set_name('Esteri')
        self.contact_repository.save(self.contact3)

        self.assertEqual(3, self.contact_repository.count())
        self.assertEqual('Esteri', self.contact_repository.find_by_id(3).get_name())

        self.contact_repository.clear()
        self.assertIsNone(self.contact_repository.find_by_id(2))




