
from faker import Faker
from typing import Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from random import Random

@dataclass
class Signup:
    name: str
    email: str
    country: str
    signup_source: str
    referral: str
    signup_purpose: str
    subscription_level: str
    payment_method: str
    sso_id: str
    email_verified: bool
    enabled: bool
    _registered_at: datetime = None

    @property
    def registered_at(self) -> datetime:
        return self._registered_at

    @registered_at.setter
    def registered_at(self, dt: datetime) -> None:
        self._registered_at = dt

    def __properties(self):
        return (
            self.name,
            self.email,
            self.country,
            self.signup_source,
            self.referral,
            self.signup_purpose,
            self.subscription_level,
            self.payment_method,
            self.sso_id,
            self.email_verified,
            self.enabled,
            self.registered_at,
        )

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__properties() == other.__properties()
        else:
            return False

    def __hash__(self):
        return hash(self.__properties())
    
    def __str__(self) -> str:
        return 

class DataGenerator:
    def __init__(self, seed: int = 0):
        self.seed = seed
        self.fake = Faker()
        self.random = Random(seed)

    def generate_signup(self) -> Signup:
        return Signup(
            name=self.fake.name(),
            email=self.fake.email(),
            country=self.fake.country(),
            signup_source=self.fake.random_element(["google", "facebook", "twitter", "other"]),
            referral=self.fake.uri(),
            signup_purpose=self.fake.random_element(["personal", "business", "education", "other"]),
            subscription_level=self.fake.random_element(["trial", "free", "premium", "enterprise"]),
            payment_method=self.fake.random_element(["credit_card", "paypal", "check", "other"]),
            sso_id=self.fake.uuid4(),
            email_verified=self.fake.boolean(),
            enabled=self.fake.boolean(),
        )
    
    def get_signups_for_date(self, date: datetime) -> Sequence[Signup]:
        date_to_seed = date.strftime("%Y%m%d")
        Faker.seed(date_to_seed)
        self.random = Random(date_to_seed)

        signups = []
        num_signups = self.random.randint(25, 100)

        for i in range(num_signups):
            signup = self.generate_signup()
            # TODO: `date_time_between_dates` is being hijacked by the Faker.seed call
            signup.registered_at = self.fake.date_time_between_dates(date, date + timedelta(days=1))
            signups.append(signup)

        new_seed = self.random.randint(0, 100000)
        Faker.seed(new_seed)
        self.random = Random(new_seed)
        return sorted(signups, key=lambda x: x.registered_at)
    
    def get_signups_for_dates(self, start_date: datetime, end_date: datetime) -> Sequence[Signup]:
        signups = []

        current_date = start_date

        while current_date <= end_date:
            signups.extend(self.get_signups_for_date(current_date))
            current_date += timedelta(days=1)
        
        return signups

    def get_signups(self, num_days: int = 7) -> Sequence[Signup]:
        signups = []

        current_date = datetime.now() - timedelta(days=num_days)

        for i in range(num_days):
            signups.extend(self.get_signups_for_date(current_date))
            current_date += timedelta(days=1)

        return signups
    
    
