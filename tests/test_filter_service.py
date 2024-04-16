from services import filter_service
import unittest


class TestFilterService(unittest.TestCase):
    
    def setUp(self) -> None:
        self.service = filter_service.FilterService()

    def test_get_task_information_should_get_task_number(self):
        task_details = [
            'Task 7 -  Handling Strings, Lists and Dictionaries',
            'Task 2 -  Getting Started with Your Bootcamp',
            'Task 1 -  Pre-Assessment MCQ'
        ]

        for task in task_details:
            task_number, task_name = self.service.get_task_information(task)
            
            self.assertIsInstance(task_number, int)

    def test_get_task_information_should_get_task_name(self):
        task_details = [
            ('Task 7 -  Handling Strings, Lists and Dictionaries', 'Handling Strings, Lists and Dictionaries'),
            ('Task 2 -  Getting Started with Your Bootcamp', 'Getting Started with Your Bootcamp'),
            ('Task 1 -  Pre-Assessment MCQ', 'Pre-Assessment MCQ')
        ]

        for original, expcted in task_details:
            task_number, task_name = self.service.get_task_information(original)

            self.assertEqual(task_name, expcted)

    def test_get_score(self):
        score_inputs_and_expected = [
            ('100', 100),
            ('N/A', None)
        ]

        for input, expected in score_inputs_and_expected:
            score = self.service.get_score(input)

            self.assertEqual(score, expected)


        

if __name__ == '__main__':
    unittest.main()