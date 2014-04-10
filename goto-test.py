import sublime, sublime_plugin
import os.path
import fnmatch
import os

class GotoTestCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view();
        file_path = view.file_name()
        file_name = os.path.basename(file_path)
        if file_name.startswith("test"):
            file_name_to_open = file_name.replace("test_","")
        else:
            file_name_to_open = "test_"+file_name
        matches = self.find_files(self.window.folders(),file_name_to_open)
        if len(matches)==1:
            self.window.open_file(matches[0])
        else:
            self.show_overlay(file_name_to_open)
                
    def show_overlay(self, file_name_to_open):
        self.window.run_command("show_overlay",{"overlay": "goto", "show_files": True, "text": file_name_to_open})

    def find_files(self,folders,file_pattern):
        matches = []
        for folder in folders:
            for root, dirnames, filenames in os.walk(folder):
                for filename in fnmatch.filter(filenames, file_pattern):
                    for ig in ['.git','/tmp/']:
                        if ig in filename:
                            break
                    else:
                        matches.append(os.path.join(root, filename))
        return(matches)
