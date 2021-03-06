from Products.Five.browser import BrowserView
from plone import api
from Products.CMFCore.utils import getToolByName


class connection(BrowserView):
    """ A list of Database Connections
    """
    def connList(self):
        results = []
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        brains = portal_catalog(portal_type="connection")
        for brain in brains:
            conn = brain.getObject()
            r = dict(
                id = conn.id,
                title = conn.title,
                url = conn.absolute_url(),
                conn_string = conn.conn_string,
                schema = conn.db_schema,
                table = conn.db_table
            )
            results.append(r)
        return results