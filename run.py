#!/usr/bin/env python3.6
from user import User
from user import Account

def create_user(firstname,lastname,username,password):
    '''
    function to create new user
    '''
    new_user = User(firstname,lastname,username,password)
    return new_user