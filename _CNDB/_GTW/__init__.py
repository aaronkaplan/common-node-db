# -*- coding: utf-8 -*-
# Copyright (C) 2012 Mag. Christian Tanzer. All rights reserved
# Glasauergasse 32, A--1130 Wien, Austria. tanzer@swing.co.at
# ****************************************************************************
# This package is part of the package CNDB.
#
# This module is licensed under the terms of the BSD 3-Clause License
# <http://www.c-tanzer.at/license/bsd_3c.html>.
# ****************************************************************************
#
#++
# Name
#    CNDB.GTW.__init__
#
# Purpose
#    RESTful web services for CNDB
#
# Revision Dates
#     6-Jun-2012 (CT) Creation
#    ««revision-date»»···
#--

from   _TFL.Package_Namespace import Package_Namespace
from   _CNDB                   import CNDB

GTW = Package_Namespace ()
CNDB._Export ("GTW")

del Package_Namespace

### __END__ CNDB.GTW.__init__
