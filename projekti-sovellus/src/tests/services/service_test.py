import unittest
from src.entities.project import Project
from src.entities.user import User
from src.services.project_service import ProjectService, ValidProjectError
from src.services.user_service import UserService, UsernameAlreadyExistsError
from src.services.music_service import MusicService
from src.services.date_service import date_service

class FakeProjectRepository:
    def __init__(self):
        self.projects = []

    def find_all(self):
        return self.projects

    def find_by_username(self, username):
        return [project for project in self.projects if project.user and project.user.username == username]

    def create(self, project):
        self.projects.append(project)
        return project

class FakeUserRepository:
    def __init__(self):
        self.users = []

    def find_all(self):
        return self.users

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def create(self, user):
        self.users.append(user)
        return user

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService(FakeProjectRepository())
        self.project_service._user = User(username="muumimamma", password="muumilaakso1")
        self.project_service._project_repository.create(
            Project(name="Musikaali", description="Tämä on musikaali", user=self.project_service._user)
            )
        self.project_service._project_repository.create(
            Project(name="Näytelmä", description="Tämä on näytelmä", user=self.project_service._user)
            )

    def test_create_project(self):
        project = self.project_service.create_project("Uusi näytelmä", "Tämä on uusi näytelmä")
        self.assertEqual(project.name, "Uusi näytelmä")
        self.assertEqual(project.description, "Tämä on uusi näytelmä")

    def test_get_all_projects(self):
        projects = self.project_service.get_projects()
        self.assertEqual(len(projects), 2)
    
    def test_create_project_with_empty_name(self):
        with self.assertRaises(ValidProjectError):
            self.project_service.create_project("", "Tämä on projekti ilman nimeä")


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())
        self.user_service.create_user("muumimamma", "muumilaakso1")

    def test_create_user_accepted(self):
        user = self.user_service.create_user("muumipappa", "muumilaakso2")
        self.assertEqual(user.username, "muumipappa")
        self.assertEqual(user.password, "muumilaakso2")

    def test_username_already_exists(self):
        with self.assertRaises(UsernameAlreadyExistsError):
            self.user_service.create_user("muumimamma", "salasana1")

    def test_login_existing_user(self):
        user = self.user_service.login("muumimamma", "muumilaakso1")
        self.assertEqual(user.username, "muumimamma")
        self.assertEqual(user.password, "muumilaakso1")

class TestMusicService(unittest.TestCase):
    def setUp(self):
        self.music_service = MusicService()

    def test_get_music_score_image_with_valid_file(self):
        img = self.music_service.get_music_score_image("src/tests/test-music/maybe-this-time.pdf")
        self.assertIsNotNone(img)
    
    def test_get_music_score_image_with_invalid_file(self):
        img = self.music_service.get_music_score_image("src/tests/test-music/not-real-music.pdf")
        self.assertIsNone(img)

class TestDateService(unittest.TestCase):
    def test_date_service_with_valid_date(self):
        date = date_service("12.05.2026 18:00")
        self.assertIsNotNone(date)
        self.assertEqual(date.day, 12)
        self.assertEqual(date.month, 5)
        self.assertEqual(date.year, 2026)
        self.assertEqual(date.hour, 18)
        self.assertEqual(date.minute, 0)
    
    def test_date_service_with_invalid_date(self):
        date = date_service("-12.05.2026")
        self.assertIsNone(date)
