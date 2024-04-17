class EditingVacancies:
    name: str
    alternate_url: str
    salary_from: int
    salary_to: int
    requirement: str
    experience: str

    def __init__(self, name, alternate_url, salary_from, salary_to, currency, requirement, experience):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.requirement = requirement
        self.experience = experience
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self) -> str:
        return (f"Профессия: {self.name},"
                f" заработная плата: {self.salary_from} - {self.salary_to} {self.__currency}"
                f" Опыт работы: {self.experience.lower()}")

    @property
    def __currency(self) -> str:
        match self.currency:
            case 'RUR':
                return f'рублей.'
            case 'EUR':
                return f'евро.'
            case 'USD':
                return f'долларов США.'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def to_json(self):
        return {"name": self.name,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "currency": self.currency,
                "requirement": self.requirement,
                "experience": self.experience,
                "alternate_url": self.alternate_url}
