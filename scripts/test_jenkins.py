import allure


class TestJen:

    @allure.step("测试步骤")
    def test_001(self):
        allure.attach("测试名称", "测试中内容")
        assert True
