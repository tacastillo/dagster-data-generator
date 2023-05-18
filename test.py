if __name__ == "__main__":
    from dagster_data_generator import DataGenerator
    from datetime import datetime, timedelta

    generator = DataGenerator()

    for i in range (10):
        yday = datetime.now() - timedelta(days=i)
        old = generator.get_signups_for_date(yday)
        new = generator.get_signups_for_date(yday)

        # assert that each record is the same, but also old
        for j in range(len(old)):
            assert old[j] == new[j]

        assert len(old) == len(set(old))
        assert len(old) == len(set(old))

        # assert that each record's registered_at property is the same
        for j in range(len(old)):
            assert old[j].registered_at != new[j].registered_at
        