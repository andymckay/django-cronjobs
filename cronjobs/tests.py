from unittest import TestCase
from cronjobs import register, registered
from django.core.management import call_command


@register
def sample():
    pass


class CronTest(TestCase):
    def testRegister(self):
        assert 'sample' in registered.keys()

    def testCommand(self):
        call_command('cron', 'sample')
        self.assertRaises(SystemExit, call_command, 'cron', 'samplefoo')
        self.assertRaises(SystemExit, call_command, 'cron')

