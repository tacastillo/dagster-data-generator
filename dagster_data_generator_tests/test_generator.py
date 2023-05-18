from dagster_data_generator.generator import DataGenerator

def test_generate_signup():
    generator = DataGenerator()
    signup = generator.generate_signup()
    assert signup["user_id"]
    assert signup["name"]
    assert signup["email"]
    assert signup["phone_number"]
    assert signup["signup_date"]

def test_generate_signups_for_day():
    generator = DataGenerator()
    signups = generator.get_signups()
    assert len(signups) > 0