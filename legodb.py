#!/usr/bin/python3

import logging
import sqlite3
from datetime import datetime, timezone

class LegoDb:
    def __init__(self):
        self.createlogger('lego')

    def createlogger(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler( name + '.log', mode='a')
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

    def ispacketregistered(self, name, version):
        self.cur.execute("SELECT deploy FROM dbpacket WHERE module = ? AND version = ?", ( name ,version))
        if self.cur.fetchone() == None:
            return False
        self.logger.debug('Row fetched from deploy')
        return True

    def registerpacket(self, name, version):
        time = datetime.now(timezone.utc)
        self.cur.execute("INSERT INTO dbpacket (module, version, deploy) VALUES (?, ?, ?)", (name, version, int(datetime.now(timezone.utc).timestamp())))

    def deploypacket(self, name, version, script):
        if not self.ispacketregistered(name, version):
            try:
                if isinstance (script, list):
                    for s in script:
                        self.cur.execute(s)
                else:
                    self.cur.execute(script)
                self.registerpacket(name, version)
                self.db.commit()
                self.logger.info('Packet %s version %s registered', name, version)
            except:
                self.db.rollback()
                raise

    def open(self, name = 'lego'):
        self.db = sqlite3.connect(name + '.db')
        self.cur = self.db.cursor()
        self.checkregistry()

    def deploy(self):
        self.deployitems()

    def deployitems(self):
        self.logger.debug('About to deploy packet 1')
        self.deploypacket('lego',1,
            ["CREATE TABLE legocategory (id INTEGER NOT NULL, name TEXT NOT NULL, PRIMARY KEY (id))",
            ("CREATE TABLE legoitems (id TEXT NOT NULL, name TEXT NOT NULL, category INTEGER NOT NULL, material TEXT NOT NULL, PRIMARY KEY (id), "
            "FOREIGN KEY (category) REFERENCES legocategory (id))") ] )

    def close(self):
        self.db.close()

db = LegoDb()
db.open()
db.deploy()
db.close()


