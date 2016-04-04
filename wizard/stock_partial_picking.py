# -*- coding: utf-8 -*-
######################################################################################################
#
# Copyright (C) B.H.C. sprl - All Rights Reserved, http://www.bhc.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including but not limited to the implied warranties
# of merchantability and/or fitness for a particular purpose
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
######################################################################################################


import time
from osv import fields, osv
from tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from tools.translate import _

class stock_partial_picking_line(osv.TransientModel):
    _inherit = "stock.partial.picking.line"
    _columns = {
        'description': fields.char('Description', size=1048),
    }

class stock_partial_picking(osv.osv_memory):
    _inherit = "stock.partial.picking"
    _columns = {
        'description': fields.char('Description', size=1048),
     }

    def default_get(self, cr, uid, fields, context=None):
        if context is None: context = {}
        res = super(stock_partial_picking, self).default_get(cr, uid, fields, context=context)
        picking_ids = context.get('active_ids', [])
        if not picking_ids or (not context.get('active_model') == 'stock.picking') \
            or len(picking_ids) != 1:
            # Partial Picking Processing may only be done for one picking at a time
            return res
        picking_id, = picking_ids
        if 'picking_id' in fields:
            res.update(picking_id=picking_id)
        if 'move_ids' in fields:
            picking = self.pool.get('stock.picking').browse(cr, uid, picking_id, context=context)
            moves = [self._partial_move_for(cr, uid, m) for m in picking.move_lines if m.state not in ('done','cancel')]
            res.update(move_ids=moves)
        if 'date' in fields:
            res.update(date=time.strftime(DEFAULT_SERVER_DATETIME_FORMAT))
        return res

    def _partial_move_for(self, cr, uid, move):
        print 'partial'
        partial_move = {
            'product_id' : move.product_id.id,
            'quantity' : move.state in ('assigned','new') and move.product_qty or 0,
            'product_uom' : move.product_uom.id,
            'prodlot_id' : move.prodlot_id.id,
            'move_id' : move.id,
            'description':move.name,
            'location_id' : move.location_id.id,
            'location_dest_id' : move.location_dest_id.id,
        }
        if move.picking_id.type == 'in' and move.product_id.cost_method == 'average':
            partial_move.update(update_cost=True, **self._product_cost_for_average_update(cr, uid, move))
        return partial_move

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

