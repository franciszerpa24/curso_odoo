# -*- coding:utf-8 -*-

from openerp.osv import osv, fields  
from datetime import datetime

TIPOS = [
	('oro','Plan ORO'),
	('plata', 'Plan PLATA'),
	('bronce', 'Plan BRONCE'),
]


class suscripcion (osv.osv):
	_name = 'co.suscripcion'
	_description = 'CO Suscripcion'
	

	_columns = {
		'codigo' : fields.char('Código'),
		'tipo' : fields.selection(TIPOS,'Tipos de suscripcion'),
		'fecha_inicio' : fields.date('Inicio Suscripcion'),
		'fecha_fin' : fields.date('Fin Suscripcion'),
		'activo' : fields.boolean('Activo'),
		'suscriptor_id' : fields.many2one('co.suscriptor', 'Afiliado'),

	}

	_defaults = {
		'activo' : True,
		'fecha_inicio' :  datetime.now().strftime('%Y-%m-%d'),
	}
	def create(self, cr, uid, values, context=None):
		if context is None:
			context = {}

		values.update({
			'codigo': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
		return super (suscripcion, self).create(cr, uid, values, context=context)

suscripcion ()