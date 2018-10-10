# -*- coding: utf-8 -*-
from myapp.app.config import get_config


async def test_conf(app):
    conf = get_config(app)
    assert conf.test is True
