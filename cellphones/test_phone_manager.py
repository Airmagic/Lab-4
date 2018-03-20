import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        # Assigning people to emplyee numbers
        testEmployee1 = Employee(1, "Micky")
        testEmployee2 = Employee(2, "Richard")

        # entering them into a list
        testEmployees = [testEmployee1, testEmployee2]

        # passing the employees
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        # checking to see if the are more than one in the list
        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)
        self.fail()


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id

        # Assigning people to emplyee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(1, "Richard")

        # passing the employee
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmply1)

        # makeing the error
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmlyp2)



    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        # adding names to employee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(2, "Richard")
        testEmply3 = Employee(3, "Steve")

        # passing the assignements
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(testEmply1)
        testAssignmentMgr.add_employee(testEmply2)
        testAssignmentMgr.add_employee(testEmply3)

        # testing the assignements
        testAssignmentMgr.assign(testPhone1.id, testEmply1)
        self.assertEqual(testPhone1.employee_id, testEmply.id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        # adding names to employee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(2, "Richard")
        testEmply3 = Employee(3, "Steve")

        # passing the assignements
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmply1)
        testAssignmentMgr.add_employee(testEmply2)
        testAssignmentMgr.add_employee(testEmply3)

        # testing if the phone has been assigned already
        testAssignmentMgr.assign(testPhone1.id, testEmply1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmply2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        # adding names to employee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(2, "Richard")
        testEmply3 = Employee(3, "Steve")

        # passing the assignements
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmply1)
        testAssignmentMgr.add_employee(testEmply2)
        testAssignmentMgr.add_employee(testEmply3)

        # test to assign two phones to one person
        testAssignmentMgr.assign(testPhone1.id, testEmply1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, testEmply1)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        # adding names to employee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(2, "Richard")
        testEmply3 = Employee(3, "Steve")

        # passing the assignements
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmply1)
        testAssignmentMgr.add_employee(testEmply2)
        testAssignmentMgr.add_employee(testEmply3)

        # test to assigned a phone twice to the same person
        testAssignmentMgr.assign(testPhone1.id, testEmply1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmply1)


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmply1 = Employee(1, "Micky")

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_employee(testEmply1)

        self.assertFalse(testAssignmentMgr.phones[0].is_assigned())


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # assigning to the variables
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        # adding names to employee numbers
        testEmply1 = Employee(1, "Micky")
        testEmply2 = Employee(2, "Richard")
        testEmply3 = Employee(3, "Steve")

        # passing the assignements
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmply1)
        testAssignmentMgr.add_employee(testEmply2)
        testAssignmentMgr.add_employee(testEmply3)

        
        testAssignmentMgr.assign(testPhone1.id, testEmply1)
        testAssignmentMgr.assign(testPhone2.id, testEmply2)

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        # testing if the employee has a phone and if they exist
        self.assertEqual(testAssignmentMgr.phone_info(testEmply1), testPhone1)
        self.assertEqual(testAssignmentMgr.phone_info(testEmply2), testPhone2)
        self.assertIsNone(testAssignmentMgr.phone_info(testEmply3))
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testAssignmentMgr.phone_info(None))
