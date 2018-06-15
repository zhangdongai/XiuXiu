#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Common.Common.ServiceDefine import *
from Service.BaseService import *

class Service(BaseService):
    def __init__(self):
        super(Service, self).__init__()
        self.serviceId = SERVICE_ID_INVALID
        pass

    def getId(self):
        return self.serviceId