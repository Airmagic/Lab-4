'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, and asserts the student is removed. Use assertNotIn
    def test_add_and_remove_student(self):
        test_class = ClassList(1)
        test_class.add_student('Steve')
        self.assertIn('Steve', test_class.class_list)

        test_class.remove_student('Steve')
        self.assertNotIn('Steve', test_class.class_list)


    ## TODO write a test that removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Steve')
        with self.assertRaises(StudentError):
            test_class.remove_student('Clyde')

    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_student_empty_list(self):
        test_class = ClassList(1)
        with self.assertRaises(StudentError):
            test_class.remove_student('Clyde')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    def test_is_enrolled_for_student_not_enrolled(self):
    ## then, call is_enrolled for a student who is not enrolled. use assertFalse to verify is_enrolled returns false.
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertFalse(test_class.is_enrolled('Jason Staythum'))



    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## TODO write a test for index_of_student to assert it returns None if the student is not in the list if the list is empty. use assertIsNone.
    def test_index_of_students_for_none_if_list_is_empty(self):
        test_class = ClassList(4)
        self.assertIsNone(test_class.index_of_student("Billy Bob"))

    ## TODO write another test when the list is not empty but does not contain the student name, assert that the correct index is returned.
    def test_none_empty_list_but_not_student_name(self):
        test_class = ClassList(4)
        test_class.add_student('Snoop Dogg')
        self.assertIsNone(test_class.index_of_student("Robert Paulson"))

    ## TODO write a test for your new is_class_full method when the class is full. use assertTrue
    def test_is_class_full_method_is_full(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertTrue(test_class.is_class_full())

    ## TODO write a test for your new is_class_full method for when is empty, and when it is not full. Use assertFalse
    def test_is_class_full_method_is_empty(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        self.assertFalse(test_class.is_class_full())
