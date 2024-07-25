import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ['Diogo Faria']
usernames = ['diogo.faria']
passwords = ['Fadababaca']

hashed_passwords = stauth.hash_passwords(passwords).generate()
