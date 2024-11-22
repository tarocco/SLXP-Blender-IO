# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper, ExportHelper, poll_file_object_drop


bl_info = {
    "name": "SLXP format",
    "author": "Tarocco",
    "description": "",
    "version": (0, 0, 1),
    "blender": (4, 3, 0),
    "location": "File > Import-Export",
    "warning": "",
    "category": "Import-Export",
}

from . import auto_load

auto_load.init()


def register():
    auto_load.register()
    print(__name__, "registered")


def unregister():
    auto_load.unregister()
    print(__name__, "unregistered")


class ImportSLXP(Operator, ImportHelper):
    pass
