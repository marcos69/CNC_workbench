################################################################################
# siegkx1.py
#
# Post Processor for the Sieg KX1 machine
# It is just an ISO machine, but I don't want the tool definition lines
#
# Dan Heeks, 5th March 2009
# This program is released under the New BSD license. See the file COPYING for details.
################################################################################
import nc
import iso_modal
import math

################################################################################
class CreatorSieg(iso_modal.CreatorIsoModal):

    def __init__(self):
        iso_modal.CreatorIsoModal.__init__(self)

    def tool_defn(self, id, name='', radius=None, length=None, gradient=None):
        pass
            
################################################################################

nc.creator = CreatorSieg()
