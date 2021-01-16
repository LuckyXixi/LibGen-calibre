__license__ = 'GPL 3'
__copyright__ = '2017, MCOfficer <mcofficer@gmx.de>'
__docformat__ = 'restructuredtext en'

from calibre.customize import StoreBase
from .libgen_plugin import LibGen_Store

class B_OK_Store(StoreBase):
    name = 'Library Genesis'
    description = 'Access LibGen directly from calibre.'
    author = 'MCOfficer'
    version = (1, 3, 0)
    drm_free_only = True
    def load_actual_plugin(self, gui):
        """This method must return the actual interface action plugin object.
        """
        self.actual_plugin_object  = LibGen_Store(gui, self.name)
        return self.actual_plugin_object
