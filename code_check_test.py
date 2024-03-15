import unittest
import user,sound_process

class MyTestCase(unittest.TestCase):
    def test_something(self):
        '''


        self.assertFalse(user.see_user_infor("baowuxi","123456"),"Error")
        self.assertTrue(user.register_search('baowuxi','A1v$','A1v$','2228703731@qq.com'),"Error")
        self.assertTrue(user.import_guest(),"Error")
        self.assertTrue(user.search_for_songs('A'),'error')
        self.assertTrue(user.get_user_id("bao","123"),"error")
        self.assertTrue(user.update_count_songs('Alone'),"error")
        self.assertTrue(sound_process.optimization("Alone"),"error")
        self.assertTrue(sound_process.show_song())
        self.assertTrue(user.computer_user_loved_song(),"error")
        self.assertTrue(user.get_username(),"error")
        self.assertTrue(user.check_status(),"error")
        :return:
        '''
        #self.assertTrue(user.check_status_true(),"Not ing")
        #self.assertTrue(sound_process.optimization("Alone"),"error")
        self.assertTrue(sound_process.show_song())
if __name__ == '__main__':
    unittest.main()

