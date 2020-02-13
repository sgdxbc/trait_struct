import pytest
from trait_struct import (
    trait,
    trait_,
    InitializeTraitException,
    struct,
    InheritStructException,
    NotImplementSupertraitException,
)


@trait_
class Empty:
    pass


@struct
class EmptyImpl(Empty):
    pass


def test_cannot_initialize_trait():
    with pytest.raises(InitializeTraitException):
        _ = Empty()
    _ = EmptyImpl()


def test_cannot_inherit_struct():
    with pytest.raises(InheritStructException):

        class _MyEmpty(EmptyImpl):
            pass


def test_consistent_name():
    assert Empty.__name__ == "Empty"
    assert EmptyImpl.__name__ == "EmptyImpl"


@trait(Empty)
class AnotherEmpty:
    pass


def test_impl_require():
    with pytest.raises(NotImplementSupertraitException):

        class _WrongImpl(AnotherEmpty):
            pass

    class _CorrectImpl(Empty, AnotherEmpty):
        pass

    with pytest.raises(NotImplementSupertraitException):

        @trait_
        class _WrongTrait(AnotherEmpty):
            pass
