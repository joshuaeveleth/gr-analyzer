#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest, uhd
from gnuradio import blocks
import pmt
import usrpanalyzer_swig as usrpanalyzer


class qa_controller_cc(gr_unittest.TestCase):
    def setUp(self):
        self.tb = top_block()

    def tearDown(self):
        self.tb = None



if __name__ == '__main__':
    #import os
    #print("Blocked waiting for GDB attach (pid = {})".format(os.getpid()))
    #raw_input("Press Enter to continue...")

    gr_unittest.run(qa_controller_cc, "qa_controller_cc.xml")
