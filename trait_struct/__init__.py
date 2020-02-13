from __future__ import annotations
from typing import List, Callable, TypeVar, Type, Any


T = TypeVar("T")


class InitializeTraitException(Exception):
    def __init__(self, trait_t: Type[T]):
        super().__init__(f"initialize trait {trait_t}")


class NotImplementSupertraitException(Exception):
    def __init__(self, impl_t: Type[T], supertrait_t: Type[T]):
        super().__init__(f"{impl_t} not implement supertrait {supertrait_t}")

def trait(*inherited_traits: Type[Any]) -> Callable[[Type[T]], Type[T]]:
    def proc(trait_t):
        class Trait(trait_t):
            def __init__(self):
                if self.__class__ is Trait:
                    raise InitializeTraitException(Trait)
                super().__init__()

            def __init_subclass__(cls, **kwargs):
                for inherited_t in inherited_traits:
                    if not issubclass(cls, inherited_t):
                        raise NotImplementSupertraitException(cls, inherited_t)

        Trait.__name__ = trait_t.__name__
        return Trait

    return proc


def trait_(trait_t: Type[T]) -> Type[T]:
    return trait()(trait_t)


class InheritStructException(Exception):
    def __init__(self, struct_t: type):
        super().__init__(f"inherit struct {struct_t}")


def struct(struct_t: Type[T]) -> Type[T]:
    class Struct(struct_t):
        def __init_subclass__(cls, **kwargs):
            raise InheritStructException(Struct)

    Struct.__name__ = struct_t.__name__
    return Struct
