from dagster import ConfigurableResource, Config
from dagster._utils.cached_method import cached_method
from pydantic import Field
from datetime import datetime, timedelta

from .generator import DataGenerator

class DataGeneratorResource(ConfigurableResource):
    """Resource for generating simulated data for experimenting with Dagster.
    
    Examples:
        .. code-block:: python
            from dagster import Definitions, asset
            from dagster_data_generator import DataGeneratorResource, DataGeneratorConfig

            @asset
            def my_table(data_gen: DataGeneratorConfig):
                return data_gen.get_signups()

            defs = Definitions(
                assets=[my_table],
                resources={"data_gen": DataGeneratorResource()}
            )
    """

    seed: int = Field(
        description="Seed for the random number generator. If not provided, a static seed will be used.",
        default=0,
    )

    num_days: int = Field(
        description="Number of days to generate data for. Defaults to 7",
        default=7
    )

    @property
    def generator(self) -> DataGenerator:
        return DataGenerator(self.seed)

    def get_signups(self):
        result = []
        today = datetime.now()

        for i in range(self.num_days):
            yday = today - timedelta(days=i)
            result.extend(self.generator.get_signups_for_date(yday))

        return result
    
    def get_signups_for_date(self, date: str):
        date_obj = datetime.strptime(date, "%m-%d-%Y")
        return self.generator.get_signups_for_date(date_obj)