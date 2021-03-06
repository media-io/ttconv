#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2020, Sandflow Consulting LLC
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''ttconv main'''

import logging
import sys
import argparse
import xml.etree.ElementTree as et
#import ttconv.model as model
import ttconv.imsc.imsc_reader as imsc_reader
import ttconv.imsc.imsc_writer as imsc_writer

LOGGER = logging.getLogger(__name__)

def parse_args(argv):
  '''Parses command line arguments. Returns inputfile, outputfile.'''

  parser = argparse.ArgumentParser()

  parser.add_argument("inputfile", help="Input file path")
  parser.add_argument("outputfile", help="Output file path")

  # Pass in argv such that it is processed based on 
  # what is passed into parse_args.
  # This allows the unit tests to pass in args through
  # the main function
  #
  args = parser.parse_args(argv)

  return args.inputfile, args.outputfile

def process(inputfile, outputfile):
  '''Process input and output through the reader, converter, and writer'''

  LOGGER.info("Input file is %s", inputfile)
  LOGGER.info("Output file is %s", outputfile)

  # 
  # Parse the xml input file into an ElementTree
  #
  tree = et.parse(inputfile)

  #
  # Pass the parsed xml to the reader
  #
  _model = imsc_reader.to_model(tree)

  #
  # Construct and configure the writer
  #
  writer = imsc_writer.Writer()

  #writer.from_model(_model)
  writer.from_xml(inputfile)
  writer.write(outputfile)

def main(argv):
  '''Main application processing'''

  #LOGGER.basicConfig(filename='main.log', level=LOGGER.INFO)
  
  inputfile = ""
  outputfile = ""
  
  inputfile, outputfile = parse_args(argv)
  
  process(inputfile, outputfile)

if __name__ == "__main__":
  main(sys.argv[1:])
