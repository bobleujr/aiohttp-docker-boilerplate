# -*- coding: utf-8 -*-
from aiohttp import web
from aiohttp.web import json_response

from .models import MyClass
from .db import get_objects

import logging


logger = logging.getLogger(__name__)


# This example used to use a peewee ORM but now it is up to every microservice
class Index(web.View):
    async def get(self):
        user_agent = self.request.headers.get('User-Agent')
        status = 200
        if not user_agent:
            user_agent = 'missing'
            status = 400

        objects = get_objects(self.request.app)

        async with objects.atomic():
            history, _ = await objects.get_or_create(
                History,
                defaults={'user_agent': user_agent},
                user_agent=user_agent
            )
            await objects.create(MyClass, history=history)
            times = await objects.count(history.entries)

        return json_response({
            'user-agent': user_agent,
            'times': times
        }, status=status)
