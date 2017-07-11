#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import orm
import asyncio
import time
from models import User


async def test_create(loop):
    await orm.create_conn_pool(loop, user='webapp', password='password', db='webapp')


async def test_insert():
    user = User(name='Test', email='test6@example.com', passwd='123123', image='about:blank', admin=False)
    await user.save()

async def test_select():
    # all = await User.findAll()
    # print(all)
    # num = await User.findNumber('email')
    # print(num)
    user = await User.find('0014992573733509d2cd0a66de4438dae4764cb252bd462000')
    print(user)

async def test_update():
    user = await User.find('0014992573733509d2cd0a66de4438dae4764cb252bd462000')
    user.passwd = '123212'
    await user.update()

async def test_delete():
    user = await User.find('001499307216539a2d8c49c81524e43875c03e6d2bb4d75000')
    await user.remove()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_create(loop))
loop.run_until_complete(test_delete())
loop.run_until_complete(orm.destory_conn_pool())
loop.close()
