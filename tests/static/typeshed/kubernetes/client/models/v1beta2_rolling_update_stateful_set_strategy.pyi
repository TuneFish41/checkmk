# Stubs for kubernetes.client.models.v1beta2_rolling_update_stateful_set_strategy (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta2RollingUpdateStatefulSetStrategy:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    partition: Any = ...
    def __init__(self, partition: Optional[Any] = ...) -> None: ...
    @property
    def partition(self): ...
    @partition.setter
    def partition(self, partition: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...