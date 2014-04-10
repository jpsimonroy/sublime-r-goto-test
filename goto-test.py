import sublime, sublime_plugin
import os.path

class GotoTestCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view();
        file_path = view.file_name()
        file_name = os.path.basename(file_path)
        if file_name.startswith("test"):
            file_name_to_open = file_name.replace("test_","")
        else:
            file_name_to_open = "test_"+file_name
        self.window.run_command("show_overlay",{"overlay": "goto", "show_files": True, "text": file_name_to_open})
