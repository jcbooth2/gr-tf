#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2019 Jayden Booth.
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

import numpy
import tensorflow
from gnuradio import gr

class model_ff(gr.basic_block):
    """
    docstring for block model_ff
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="model_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

        self.sess = tensorflow.Session()
        self.op = tf.saved_model.loader.load(sess, [tag_constants.TRAINING], export_dir)


    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = input_size*noutput_items/output_size

    def general_work(self, input_items, output_items):
        rv = self.sess.run([self.op], feed_dict={input_items[0]})
        output_items[0][:] = rv[0]
        consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
