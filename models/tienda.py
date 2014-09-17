# -*- coding:utf-8 -*-


from openerp.osv import osv, fields  


class tienda (osv.osv):
	_name = 'co.tienda'
	_description = 'CO tienda'
	_rec_name = 'nombre'
	
	_columns = {
		'nombre' : fields.char('Nombre'),
		'direccion' : fields.char('Direccion'),
	}	

tienda ()