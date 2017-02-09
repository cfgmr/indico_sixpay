# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2014 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico;if not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, division
from MaKaC.webinterface import wcomponents
import os
import pkg_resources
import MaKaC.common.Configuration as Configuration

from .. import __init__ as pay_plugin


class WTemplated(wcomponents.WTemplated):
    def _setTPLFile(self):
        """Sets the TPL (template) file for the object. It will try to get
            from the configuration if there's a special TPL file for it and
            if not it will look for a file called as the class name+".tpl"
            in the configured TPL directory.
        """
        cfg = Configuration.Config.getInstance()
        tpl_dir = pkg_resources.resource_filename(pay_plugin.__name__, "tpls")
        tpl_file = cfg.getTPLFile(self.tplId)
        if tpl_file == "":
            tpl_file = "%s.tpl" % self.tplId
        self.tplFile = os.path.join(tpl_dir, tpl_file)
        hfile = self._getSpecificTPL(
            os.path.join(tpl_dir, 'chelp'),
            self.tplId,
            extension='wohl',
        )
        self.helpFile = os.path.join(tpl_dir, 'chelp', hfile)
