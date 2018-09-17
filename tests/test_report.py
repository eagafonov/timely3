import timely3


class TestReport:
    def test_module_report(self):
        """
        Just test we can call a module-level report()
        """
        timely3.report()

    def test_class_report(self):
        """
        Just test we can call a module-level report()
        """
        timely3.timely3.report()
