# -*- coding: utf-8 -*-
from openerp.osv import osv, fields  


class suscriptor (osv.osv) : 
	_name = 'co.suscriptor'
	_description = 'CO Suscriptor'

	_columns = { #estos nombres son los que debe tener en la base de datos,
	#EL primero es el nombre del campo en base de datos, el segundo el tipo de de dato, el tercero es la etiqueta del campo en la vista 
	#el campo id ya lo crea el orm por defecto	
		'nombre' : fields.char('Nombres'), 
		'cedula' : fields.char('N° Cédula'),
		'direccion' : fields.char('Direccion de Habitación'),
	}

suscriptor()