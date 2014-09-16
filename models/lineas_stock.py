# -*- coding:utf-8 -*-

from openerp.osv import osv, fields  


class lineas_stock (osv.osv):
	_name = 'co.lineas.stock'
	_description = 'CO Lineas stock'

	_columns = {
		'multimedia_id' : fields.many2one('co.multimedia', 'Multimedia'),
		'medio_id' : fields.many2one('co.tipo.medios', 'Medios'),
		'tienda_id' : fields.many2one('co.tienda','Tienda'),
		'cantidad' : fields.integer('Cantidad'),

	}	

lineas_stock ()

class tienda (osv.osv):
	_inherit = 'co.tienda' ##heredo de tienda, este campo hace referencia a la clase tienda del archivo tienda.py

	_columns = {
		'lineas_ids' : fields.one2many('co.lineas.stock', 'tienda_id', 'stock'),
	} 

tienda ()