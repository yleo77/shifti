import sublime
import sublime_plugin

class ShiftiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        text = self.view.substr(selection)           

        filepath = self.view.file_name()
        # packages = sublime.packages_path()
        args = {
            "cmd": [
                "grep",
                '-n',
                text,
                filepath
            ]
        }
        self.view.window().run_command('exec', args)
        


