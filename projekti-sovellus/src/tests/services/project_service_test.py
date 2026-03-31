import unittest
from services.project_service import ProjectService

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService()

    def test_create_project(self):
        project = self.project_service.create_project("Musikaali", "Tämä on musikaali", "Mimmi Musikaali")
        self.assertEqual(project.name, "Musikaali")
        self.assertEqual(project.description, "Tämä on musikaali")
        self.assertEqual(project.user, "Mimmi Musikaali")
        self.assertIsNotNone(project.id)

    def test_get_all_projects(self):
        self.project_service.create_project("Musikaali", "Tämä on musikaali", "Mimmi Musikaali")
        self.project_service.create_project("Näytelmä", "Tämä on näytelmä", "Niina Näytelmä")

        projects = self.project_service.get_all_projects()
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[0].name, "Musikaali")
        self.assertEqual(projects[1].name, "Näytelmä")