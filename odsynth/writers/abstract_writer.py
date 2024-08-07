from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractWriter(ABC):
    """Writers write generated data to desired mediums
    (Cloud Storage, REST Endpoints, Disc, etc)"""

    @abstractmethod
    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """Writes generated data to a desired medium.

        Parameters:
        -
        data (list[dict]): Data generated by odsynth.DataGenerator
        """
        raise NotImplementedError("'write_data' is to be implemented by its subclasses")

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Returns an identifying name for a writer class

        Returns:
        --------
        output (str): ID of the writer
        """
        raise NotImplementedError("'get_name' is to be implemented by its subclasses")
