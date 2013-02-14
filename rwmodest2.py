import sublime, sublime_plugin
import os
 
class WriteCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                File = self.view.file_name()
                os.chmod(File, 0777)
 
class ReadCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                File = self.view.file_name()
                os.chmod(File, 0555)


