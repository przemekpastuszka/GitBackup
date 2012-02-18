import os
import subprocess
import time
import configparser


class Repository:
    def __init__(self, f):
        self.location = ""
        self.tracked = dict()

    def send_data_to(storage_name):
        pass

    @staticmethod
    def read_repos_from_file(path):
        repos = dict()
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(path)
        for section in config.sections():
            repo = GitRepository(config[section])
            repos[repo.location] = repo
        return repos

class GitRepository(Repository):
    def __init__(self, data):
        self.location = data.name
        self.need_sudo = data.getboolean("use_sudo")
        data.pop('use_sudo')
        self.tracked = dict()

        for (path, extensions) in data.items():
            self.tracked[path] = set(extensions.strip().split())

    def send_data_to(self, storage_name):
        os.chdir(self.location)
        for directory, exts in self.tracked.items():
            print("Current dir: " + directory)
            if exts:
                for root, _, filenames in os.walk(directory):
                    for f in filenames:
                        (_, ext) = os.path.splitext(f)
                        if ext in exts:
                            path = '/'.join([root, f])
                            self.call_process('git add ' + path)
            else:
                self.call_process('git add ' + directory)
        self.call_process('git commit -m ' + str(time.time()))
        self.call_process('git push ' + storage_name + ' master')

    def call_process(self, command):
        if self.need_sudo:
            command = "sudo " + command
        subprocess.call([command], shell=True)
