#! /usr/bin/python

import os
from storage import PendriveStorage
from storage import DropboxStorage
import argparse
from repository import Repository

def backup():
    parser = argparse.ArgumentParser(description="Backup utility")
    parser.add_argument("repos", nargs='+')
    parser.add_argument('--pendrive', action='store_const', const=PendriveStorage(), default=DropboxStorage(), help="use pendrive as storage", dest="storage")
    args = parser.parse_args()

    args.storage.start()
    for (location, repo) in Repository.read_repos_from_file("/etc/gitbackup.conf").items():
        if any([os.path.samefile(location, rep_dir) for rep_dir in args.repos]):
            repo.send_data_to(args.storage.name)
    args.storage.stop()

backup()
