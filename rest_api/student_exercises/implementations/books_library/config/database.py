import os

import firebase_admin
from firebase_admin import credentials, firestore

CURR_DIR = os.path.dirname(__file__)
cred = credentials.Certificate(f"{CURR_DIR}/booksLibrary-creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()