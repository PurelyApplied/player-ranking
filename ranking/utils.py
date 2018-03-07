
class Generated:
    _next_id = 0

    def __init__(self):
        self._generated_id = self.__tick_id()

    @classmethod
    def __tick_id(cls):
        this_id, cls._next_id = cls._next_id, cls._next_id + 1
        return this_id


class Retained(Generated):
    retained_instances = {}

    def __init__(self):
        super().__init__()
        self.add_to_retained_instances(self)

    @classmethod
    def add_to_retained_instances(cls, instance: Generated):
        cls.retained_instances[instance._generated_id] = instance

    @classmethod
    def remove_from_retained_instances(cls, instance_id):
        cls.retained_instances.pop(instance_id)
