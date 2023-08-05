import pytest

from PageObjects.LoginPage import functions



@pytest.mark.usefixtures("setup")

class Test_001_Login:

    baseURL="https://www.naukri.com/mnjuser/homepage"

    @pytest.mark.regression
    def test_profile(self):

        self.lp=functions(self.driver,self.wait,self.a)
        self.lp.profil()
        self.lp.headertext()
        self.lp.resume()

    @pytest.mark.sanity
    def test_check(self):
        self.lp = functions(self.driver, self.wait, self.a)
        self.lp.checksanity()










