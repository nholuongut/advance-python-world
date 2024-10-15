from typing import Dict, List
from serializers import JsonSerializer, XmlSerializer


class ObjectFactory:
    """
    The central idea in Factory Method is to provide a separate component with the responsibility to
    decide which concrete implementation should be used based on some specified parameter.
    That parameter in our example is the format
    """

    def __init__(self) -> None:
        pass

    def get_serializer(self, format: str):
        """output serializer class object

        Args:
            format (str): serializable format

        Raises:
            ValueError: if format not defined output error

        Returns:
            _type_: respective object
        """
        if format == "JSON":
            return JsonSerializer()
        elif format == "XML":
            return XmlSerializer()
        else:
            raise ValueError(format)
