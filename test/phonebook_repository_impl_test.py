from unittest import TestCase

from data.models.phonebook import Phonebook
from data.repository.phonebook_repository_impl import PhonebookRepositoryImpl


class TestCaseForPhonebookRepositoryClass(TestCase):
    def setUp(self) -> None:
        self.phonebook_repository = PhonebookRepositoryImpl()

    def test_that_one_phonebook_can_be_added(self):
        self.phonebook = Phonebook()
        self.phonebook_repository.save(self.phonebook)

        self.assertEqual(1, self.phonebook_repository.count())

    def test_that_one_phonebook_can_be_added_and_found(self):
        self.phonebook = Phonebook()
        self.phonebook.set_username('esther')
        self.phonebook_repository.save(self.phonebook)

        self.assertEqual(1, self.phonebook_repository.count())
        self.assertEqual(self.phonebook.get_username(), self.phonebook_repository.find_by_id(1).get_username())

    def test_that_one_phonebook_can_be_added_and_updated(self):
        self.phonebook = Phonebook()
        self.phonebook.set_username('esther')
        self.phonebook_repository.save(self.phonebook)

        self.assertEqual(1, self.phonebook_repository.count())
        self.assertEqual(self.phonebook.get_username(), self.phonebook_repository.find_by_id(1).get_username())

        self.updated_phonebook = self.phonebook_repository.find_by_id(1)
        self.updated_phonebook.set_username('Esther')

        self.assertEqual('Esther', self.phonebook_repository.find_by_id(1).get_username())

    def test_that_phonebooks_can_be_added_and_can_all_be_printed_at_the_same_time(self):
        self.phonebook1 = Phonebook()
        self.phonebook1.set_username('esther')
        self.phonebook_repository.save(self.phonebook1)

        self.assertEqual(1, self.phonebook_repository.count())
        self.assertEqual('esther', self.phonebook_repository.find_by_id(1).get_username())

        self.phonebook2 = Phonebook()
        self.phonebook2.set_username('Esther')
        self.phonebook_repository.save(self.phonebook2)

        self.assertEqual(2, self.phonebook_repository.count())
        self.assertEqual('Esther', self.phonebook_repository.find_by_id(2).get_username())

        self.phonebook3 = Phonebook()
        self.phonebook3.set_username('Esteri')
        self.phonebook_repository.save(self.phonebook3)

        self.assertEqual(3, self.phonebook_repository.count())
        self.assertEqual('Esteri', self.phonebook_repository.find_by_id(3).get_username())

        self.expected_list = [self.phonebook1, self.phonebook2, self.phonebook3]
        self.assertEqual(self.expected_list, self.phonebook_repository.find_all())

    def test_that_a_phonebook_can_be_added_can_be_deleted(self):
        self.phonebook1 = Phonebook()
        self.phonebook1.set_username('esther')
        self.phonebook_repository.save(self.phonebook1)

        self.assertEqual(1, self.phonebook_repository.count())
        self.assertEqual('esther', self.phonebook_repository.find_by_id(1).get_username())

        self.phonebook2 = Phonebook()
        self.phonebook2.set_username('Esther')
        self.phonebook_repository.save(self.phonebook2)

        self.assertEqual(2, self.phonebook_repository.count())
        self.assertEqual('Esther', self.phonebook_repository.find_by_id(2).get_username())

        self.phonebook3 = Phonebook()
        self.phonebook3.set_username('Esteri')
        self.phonebook_repository.save(self.phonebook3)

        self.assertEqual(3, self.phonebook_repository.count())
        self.assertEqual('Esteri', self.phonebook_repository.find_by_id(3).get_username())

        self.phonebook_repository.delete(self.phonebook3)
        self.assertIsNone(self.phonebook_repository.find_by_id(3))

    def test_that_all_phonebooks_can_be_cleared(self):
        self.phonebook1 = Phonebook()
        self.phonebook1.set_username('esther')
        self.phonebook_repository.save(self.phonebook1)

        self.assertEqual(1, self.phonebook_repository.count())
        self.assertEqual('esther', self.phonebook_repository.find_by_id(1).get_username())

        self.phonebook2 = Phonebook()
        self.phonebook2.set_username('Esther')
        self.phonebook_repository.save(self.phonebook2)

        self.assertEqual(2, self.phonebook_repository.count())
        self.assertEqual('Esther', self.phonebook_repository.find_by_id(2).get_username())

        self.phonebook3 = Phonebook()
        self.phonebook3.set_username('Esteri')
        self.phonebook_repository.save(self.phonebook3)

        self.assertEqual(3, self.phonebook_repository.count())
        self.assertEqual('Esteri', self.phonebook_repository.find_by_id(3).get_username())

        self.phonebook_repository.clear()
        self.assertIsNone(self.phonebook_repository.find_by_id(3))



