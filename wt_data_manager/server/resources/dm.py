#!/usr/bin/env python
# -*- coding: utf-8 -*-

from girder.api.rest import Resource


class DM(Resource):
    def __init__(self, sessionModel, cacheManager):
        super(DM, self).__init__()
        self.resourceName = 'dm'
        self.sessionModel = sessionModel
        self.cacheManager = cacheManager

    def createSession(self, user, dataSet):
        return self.sessionModel.createSession(user, dataSet)

    def deleteSession(self, user, sessionId=None, session=None):
        if session is None:
            if sessionId is None:
                raise ValueError('One of sessionId or session must be non-null')
            session = self.sessionModel.load(sessionId, user=user)
        self.sessionModel.deleteSession(user, session)
