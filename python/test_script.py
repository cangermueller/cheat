import sys
import os
import os.path as pt

__dir = pt.dirname(pt.realpath(__file__))
sys.path.insert(0, pt.join(__dir, '.'))
import script


class TestModule(object):

    def setup_class(self):
        self.cwd = os.getcwd()

    def teardown_class(self):
        os.chdir(self.cwd)

    def goto(self, test_dir):
        os.chdir(pt.join(self.cwd, 'data', 'test_script', test_dir))

    def run(self, args):
        args = args.split()
        args.insert(0, 'script.py')
        return script.Script().run(args)

    def test_run(self):
        # self.goto('test_fun')
        assert self.run('in_file.txt') == 0
