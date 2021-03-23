#!/usr/bin/python3

import logging
import sqlite3

class LegoDb:
    def __init__(self):
        self.createlogger('lego')

    def createlogger(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler( name + '.log', mode='w')
        fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s:%(message)s'))
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter())
        self.logger.addHandler(ch)

    def checkregistry(self):
        try:
            self.cur.execute("SELECT * FROM dbpacket WHERE module = 'init'")
        except sqlite3.OperationalError:
            self.cur.execute("CREATE TABLE dbpacket (module TEXT NOT NULL, version INTEGER NOT NULL, deploy INTEGER, PRIMARY KEY (module, version))")
            self.db.commit()
            self.logger.info("Packet registry created")

    def open(self, name = 'lego'):
        self.db = sqlite3.connect(name + '.db')
        self.cur = self.db.cursor()
        self.checkregistry()

    def close(self):
        self.db.close()

db = LegoDb()
db.open()
db.close()




