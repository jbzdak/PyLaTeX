# -*- coding: utf-8 -*-
try:
    from collections import UserList
except ImportError as e:
    from user_list_impl import UserList
