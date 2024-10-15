# base class
class Base:
    _instance = "hello"

    def service_context(self):
        print("service instance created")

    def llm(self):
        print("LLM inference")


class Service(Base):
    _service = None

    def __init__(self) -> None:
        super(Service, self).__init__()
        self.inedx = None
        self.vectorestore = None

    def load_docs(self):
        self.documents = "Docs Loaded !"

    def create_index(self, indexer=None):
        if indexer is not None:
            self.index = indexer
        else:
            self.index = "Index created !"

    def create_store(self, recreate=None):
        if recreate is not None:
            self.vectorestore = "Vector Store recreated !"
        else:
            self.vectorestore = "Vectror  Store !"

    def create_queryEngine(self):
        self.query_engine = "Create Query Engine !"

    @classmethod
    def get_singleton_instance(cls):
        if cls._service is None:
            print("Creating singleton service")
            cls._service = cls()

        return cls._service


if __name__ == "__main__":
    # define singleton instance
    Service.get_singleton_instance().create_index()

    print(Service.get_singleton_instance().index)

    Service.get_singleton_instance().create_index(indexer="1")

    print(Service.get_singleton_instance().index)
    Service.get_singleton_instance().create_queryEngine()
    print(Service.get_singleton_instance().query_engine)

    Service.get_singleton_instance().service_context()
    print(Service.get_singleton_instance()._instance)
