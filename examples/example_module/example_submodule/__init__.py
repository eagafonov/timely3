from timely3 import timely3


@timely3()
def func_from_pkg_01():
    pass

@timely3("function_from_package")
def func_from_pkg_02():
    pass

