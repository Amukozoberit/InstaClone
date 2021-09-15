from datetime import datetime
from instap.models import Employee, Followers, LikeClass, Post, UserProfile
from django.test import TestCase
from django.contrib.auth.models import User



class TestFollowers(TestCase):
    def setUp(self):
        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()
        self.berit=Followers(uname='Berit',user_id=1)
        self.berit.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.berit,Followers))


class TestLike(TestCase):
    def setUp(self):
        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()
        self.berit=LikeClass(user_id='Berit',user_id=1,post_id=1)
        self.berit.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.berit,Followers))


class TestDisLike(TestCase):
    def setUp(self):
        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()
        self.berit=LikeClass(user_id='Berit',user_id=1,post_id=1)
        self.berit.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.berit,Followers))

class TestEmployees(TestCase):
    def setUp(self):
        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()
        self.new_Employee=Employee(bio='developer',user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Employee,Employee))
    
class Testcommets(TestCase):
    def setUp(self):
        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()
        self.new_post=Post(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()

class Post(TestCase):
    def setUp(self):

        self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
        self.new_user.save()

        self.new_post=Post(caption='hello world',pub_date=datetime.now,owner=self.user)



    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_image(self):
        new_p=self.new_post
        new_p.save_image()
        posts=Post.get_images()
        self.assertTrue(len(posts)>0)


    def update_image(self):
        new_p=self.new_gal
        new_p.update_image()
        posts=Post.get_images()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_p=self.new_gal
        new_p.delete_image(new_p.id)
        posts=Post.get_images()
        self.assertTrue(len(posts)==0)

class TestUserProfile(TestCase):
        def setUp(self):
            self.new_user=User(username='Berit',email='mwasheberit@gmail.com',password='berit')
            self.new_user.save()

            self.profile=UserProfile(user=self.user,bio='this is me')



        def test_instance(self):
            self.assertTrue(isinstance(self.profile,UserProfile))







