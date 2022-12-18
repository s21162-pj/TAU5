import unittest
# from assertpy import assert_that
from Zadanie4 import return_song, return_verse



class MyTestCase(unittest.TestCase):

    def test_third_line(self):
        self.assertEqual(return_verse(3),
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_last_line(self):
        self.assertEqual(return_verse(12),
                         "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_out_of_scope(self):
        self.assertRaises(Exception, return_verse(12))


    def test_out_of_scope(self):
        self.assertRaises(Exception, return_verse(15))