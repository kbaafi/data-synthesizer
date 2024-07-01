from typing import Any, Dict, List
from .base_publisher import BasePublisher
from ..data_generator import DataGenerator
from ..utils import load_yaml
import json
import time

class JsonPublisher(BasePublisher):
    def __init__(self, schema_file: str, plugins_dir: str, output_dir: str, num_examples: int = 100, batch_size: int = 10, run_as_daemon: bool = False):
        super().__init__(schema_file, plugins_dir, num_examples, batch_size, run_as_daemon)
        self._output_dir = output_dir

    def publish_data(self):
        def write_batch(batch: List[Dict[str, Any]]):
            timestamp = int(time.time() * 1e6)
            filename = f"{self._output_dir}/odsynth_{timestamp}.json"
            with open(filename, 'w') as file:
                for item in batch:
                    json.dump(item, file)
                    file.write('\n')

        schema = load_yaml(self._schema_file)
        if self._run_as_daemon:
            generator = DataGenerator(
                schema=schema,
                plugins_dir=self._plugins_dir,
                num_examples=self._batch_size,
                batch_size=self._batch_size,
            )
            while (True):
                for batch in generator.yield_data():
                    write_batch(batch)
        else:
            generator = DataGenerator(
                schema=schema,
                plugins_dir=self._plugins_dir,
                num_examples=self._num_examples,
                batch_size=self._batch_size,
            )
            for batch in generator.yield_data():
                write_batch(batch)

