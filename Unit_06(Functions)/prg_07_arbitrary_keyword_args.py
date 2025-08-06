#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        06/08/2025           Write a python function that accepts arbitrary number 
#                                                of arguments for a user profile. E.g. first_name, last_name,
#                                                location, field etc.. 

# user_info is arbitrary argument. **user_info tells python to make a dictionary. 
# Any number of key/value pair can be passed to this argument
def create_profile(**user_info):
    print(user_info)

create_profile (
    first_name = 'Suryakant', 
    last_name = 'Baluni', 
    location = 'Dehradun', 
    field = 'Computer Science'
);