# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2019 - Oliver Oxtoby <oliveroxtoby@gmail.com>           *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import FreeCAD
import CfdTools
import os

if FreeCAD.GuiUp:
    import FreeCADGui
    from PySide import QtCore


class _CfdAnalysis:
    """ The CFD analysis group """
    def __init__(self, obj):
        obj.Proxy = self
        self.Type = "CfdAnalysis"
        self.initProperties(obj)

    def initProperties(self, obj):
        if 'OutputPath' not in obj.PropertiesList:
            obj.addProperty("App::PropertyPath", "OutputPath", "Path to write cases to (blank to use system default)")

    def onDocumentRestored(self, obj):
        self.initProperties(obj)
