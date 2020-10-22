import unittest
from school_report import student_average


class SchoolReportTests(unittest.TestCase):

    def test_student_average_approved(self):
        average, result = student_average(9, 8, 7, 6)
        self.assertEqual([average, result], [7.5, "aprovado"])

    def test_student_average_reproved(self):
        average, result = student_average(5, 5, 5, 5)
        self.assertEqual([average, result], [5, "reprovado"])


if __name__ == "__main__":
    unittest.main()
