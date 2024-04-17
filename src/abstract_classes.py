from abc import ABC, abstractmethod


class HHAbstract(ABC):

    @abstractmethod
    def get_vacancy(self):
        pass


class AbstractVacancy(ABC):
    @abstractmethod
    def save_vacancy_to_file(self):
        pass

    @abstractmethod
    def read_vacancy_from_file(self):
        pass

    @abstractmethod
    def del_vacancy_from_file(self):
        pass
