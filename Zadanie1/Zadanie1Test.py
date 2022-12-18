import unittest

from Zadanie1 import statement

class TestStatement(unittest.TestCase):
    def test_statement_with_tragedy_play(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55,
                },
            ],
        }
        plays = {
            "hamlet": {
                "name": "Hamlet",
                "type": "tragedy",
            },
        }
        result = statement(invoice, plays)

        self.assertTrue(
            ('BigCo' in result) and ('Hamlet' in result) and ('$650.00' in result) and
            ('55 seats' in result) and ('25 credits' in result))

    def test_statement_with_comedy_play(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 35,
                },
            ],
        }
        plays = {
            "as-like": {
                "name": "As You Like It",
                "type": "comedy",
            },
        }

        result = statement(invoice, plays)

        self.assertTrue(
            ('BigCo' in result) and ('As You Like It' in result) and ('$580.00' in result) and
            ('35 seats' in result) and ('12 credits' in result))

    def test_statement_with_unknown_play_type(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "othello",
                    "audience": 40,
                },
            ],
        }
        plays = {
            "othello": {
                "name": "Othello",
                "type": "unknown",
            },
        }

        with self.assertRaises(ValueError) as context:
            statement(invoice, plays)

        self.assertEqual(str(context.exception), "unknown type: unknown")