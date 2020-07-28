from app import App
class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        pass

    def test_addcontact(self):
        """
        添加联系人
        :return:
        """
        name = "霍格name1"
        gender = "女"
        phonenum = "15811111111"
        mypage = self.main.goto_contactlist().add_contact().add_menual().\
            set_name(name).set_gender(gender).set_phonnum(phonenum).click_save()
        text = mypage.get_toast()
        assert '成功' in text
