# -*- coding:utf-8 -*-

from openerp.osv import osv, fields  

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

suscripcion ()