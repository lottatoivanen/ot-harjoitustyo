import unittest
import os
from src.config import DATABASE_DIRECTORY
from src.database_connection import get_database_connection, reset_database_connection
from src.initialize_database import initialize_database
from src.repositories.project_repository import project_repository
from src.repositories.user_repository import user_repository
from src.entities.project import Project
from src.entities.user import User

class TestProjectRepository(unittest.TestCase):
    def setUp(self):
        test_database = os.path.join(DATABASE_DIRECTORY, "test-database.sqlite")
        reset_database_connection()
        initialize_database(test_database)
        connection = get_database_connection(test_database)
        user_repository._connection = connection
        project_repository._connection = connection
        self.user = user_repository.create(User(username="muumimamma", password="muumilaakso1"))
    
    def test_create(self):
        project = project_repository.create(Project(name="Näytelmä", description="Tämä on näytelmäprojekti", user=self.user))
        self.assertEqual(project.name, "Näytelmä")
        self.assertEqual(project.description, "Tämä on näytelmäprojekti")
        self.assertEqual(project.user.username, "muumimamma")

    def test_find_all(self):
        project_repository.create(Project(name="Näytelmä", description="Tämä on näytelmäprojekti", user=self.user))
        projects = project_repository.find_all()
        self.assertEqual(len(projects), 1)
    
    def test_find_by_username(self):
        project_repository.create(Project(name="Näytelmä", description="Tämä on näytelmäprojekti", user=self.user))
        projects = project_repository.find_by_username("muumimamma")
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0].name, "Näytelmä")
        self.assertEqual(projects[0].description, "Tämä on näytelmäprojekti")
        self.assertEqual(projects[0].user.username, "muumimamma")
    
    def test_delete(self):
        project = project_repository.create(Project(name="Näytelmä", description="Tämä on näytelmäprojekti", user=self.user))
        project_repository.delete(project.id)
        projects = project_repository.find_all()
        self.assertEqual(len(projects), 0)
    
    def test_update(self):
        project = project_repository.create(Project(name="Näytelmä", description="Tämä on näytelmäprojekti", user=self.user))
        project.name = "Uusi näytelmä"
        project.description = "Tämä on uusi näytelmäprojekti"
        project_repository.update(project)
        projects = project_repository.find_all()
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0].name, "Uusi näytelmä")
        self.assertEqual(projects[0].description, "Tämä on uusi näytelmäprojekti")
        self.assertEqual(projects[0].user.username, "muumimamma")