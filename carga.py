# -*- coding: utf-8 -*-
from odoolib.api import OdooLib

ol = OdooLib('http://serverms2:8069', 'GlobalShipping', 'admin', '123')

#Usuarios
ol.res_users.add({'name':'Equipos','login':'equipos','in_group_13':'True','in_group_16':'True','tz':'America/Caracas','lang':'es_VE'})
ol.res_users.add({'name':'Documentación','login':'documentacion','in_group_13':'True','in_group_17':'True','tz':'America/Caracas','lang':'es_VE'})
ol.res_users.add({'name':'Finanzas','login':'finanzas','in_group_13':'True','in_group_15':'True','tz':'America/Caracas','lang':'es_VE'})
ol.res_users.add({'name':'Administración','login':'administracion','in_group_13':'True','in_group_14':'True','tz':'America/Caracas','lang':'es_VE'})

# Buques
ol.buque.add({'nombre': 'COSCO AQABA 007E','siglas':'CAQABA007E'})
ol.buque.add({'nombre': 'COSCO HOUSTON 015E','siglas':'CH015E'})
ol.buque.add({'nombre': 'XIU HE 304S ','siglas':'XH304S'})

# Tipos de contenedores
ol.contenedor_tipo.add({'codigo': '2000 ','descripcion':'20GP '})
ol.contenedor_tipo.add({'codigo': '4000','descripcion':'40GP'})
ol.contenedor_tipo.add({'codigo': '4400','descripcion':'40HQ'})
ol.contenedor_tipo.add({'codigo': '2050 ','descripcion':'20OT'})
ol.contenedor_tipo.add({'codigo': '4050','descripcion':'40OT'})
ol.contenedor_tipo.add({'codigo': '4060','descripcion':'40FR'})
ol.contenedor_tipo.add({'codigo': '2270','descripcion':'20TK'})

#Materiales
ol.material.add({'codigo': 'M001','descripcion':'Material 1','hoja_seguridad':'Hoja 1'})
ol.material.add({'codigo': 'M002','descripcion':'Material 2','hoja_seguridad':'Hoja 2'})
ol.material.add({'codigo': 'M003','descripcion':'Material 3','hoja_seguridad':'Hoja 3'})

#Capitanias De Puertos
ol.puerto_capitania.add({'codigo': 'CP001','descripcion':'Capitanía La Guaira'})
ol.puerto_capitania.add({'codigo': 'CP002','descripcion':'Capitanía Guanta'})
ol.puerto_capitania.add({'codigo': 'CP003','descripcion':'Capitanía Pto Cabello'})

#Puertos
ol.puerto.add({'codigo': 'P001','descripcion':'La Guaira','direccion':'La Guaira','capitania':'1','correo':'laguaira@gmail.com'})
ol.puerto.add({'codigo': 'P002','descripcion':'Guanta','direccion':'Guanta','capitania':'2','correo':'guanta@gmail.com'})
ol.puerto.add({'codigo': 'P003','descripcion':'Pto Cabello','direccion':'Pto Cabello','capitania':'3','correo':'ptocabello@gmail.com'})

#Patios
ol.patio.add({'codigo':'PA001','descripcion':'Patio 1'})
ol.patio.add({'codigo':'PA002','descripcion':'Patio 2'})
ol.patio.add({'codigo':'PA003','descripcion':'Patio 3'})

#Rutas
ol.ruta.add({'codigo':'R001','descripcion':'Ruta 1'})
ol.ruta.add({'codigo':'R002','descripcion':'Ruta 2'})
ol.ruta.add({'codigo':'R003','descripcion':'Ruta 3'})

#Gastos
ol.gasto.add({'codigo':'G001','descripcion':'Gasto 1','valor':'1000','tipo':'Local','cuenta_contable':'Cuenta Contable 1'})
ol.gasto.add({'codigo':'G002','descripcion':'Gasto 2','valor':'1000','tipo':'Adicional','cuenta_contable':'Cuenta Contable 2'})
ol.gasto.add({'codigo':'G003','descripcion':'Gasto 3','valor':'1000','tipo':'Local','cuenta_contable':'Cuenta Contable 3'})

#Lineas
ol.linea.add({'codigo':'L001','descripcion':'Línea 1'})
ol.linea.add({'codigo':'L002','descripcion':'Línea 2'})
ol.linea.add({'codigo':'L003','descripcion':'Línea 3'})

#Beneficiarios
ol.beneficiario.add({'codigo':'B001','nombre':'Beneficiario 1'})
ol.beneficiario.add({'codigo':'B002','nombre':'Beneficiario 2'})
ol.beneficiario.add({'codigo':'B003','nombre':'Beneficiario 3'})

#Viajes
ol.viaje.add({'codigo': 'V001','descripcion':'Viaje 1','buque_id':'1','fecha_registro':'06/01/2015',
				'fecha_inicio':'06/02/2015','fecha_trasbordo':'06/03/2015','fecha_arribo':'06/04/2015',
				'linea':'1','ruta':'1','puerto_origen':'1','puerto_trasbordo':'2','puerto_arribo':'3'})
ol.viaje.add({'codigo': 'V002','descripcion':'Viaje 2','buque_id':'2','fecha_registro':'06/02/2015',
				'fecha_inicio':'06/03/2015','fecha_trasbordo':'06/05/2015','fecha_arribo':'06/10/2015',
				'linea':'2','ruta':'2','puerto_origen':'3','puerto_trasbordo':'1','puerto_arribo':'2'})	
ol.viaje.add({'codigo': 'V003','descripcion':'Viaje 3','buque_id':'3','fecha_registro':'06/09/2015',
				'fecha_inicio':'06/11/2015','fecha_trasbordo':'06/13/2015','fecha_arribo':'06/15/2015',
				'linea':'3','ruta':'3','puerto_origen':'2','puerto_trasbordo':'3','puerto_arribo':'1'})

#Servicios
ol.servicio.add({'codigo':'S001','descripcion':'Servicio 1','monto':'1000','beneficiario':'1','viaje_id':'1'})
ol.servicio.add({'codigo':'S002','descripcion':'Servicio 2','monto':'1000','beneficiario':'2','viaje_id':'1'})
ol.servicio.add({'codigo':'S003','descripcion':'Servicio 3','monto':'1000','beneficiario':'3','viaje_id':'1'})
				
#Contenedores viaje 1
ol.contenedor.add({'numero':'CBHU4046212','no_precinto':'1','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6049000610','peso':'1000','tipo_material':'1',
					'viaje_id':'1','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'1','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'TCNU5700548','no_precinto':'2','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6049094250','peso':'1000','tipo_material':'2',
					'viaje_id':'1','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'2','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'CBHU8246142','no_precinto':'3','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049094250','peso':'1000','tipo_material':'1',
					'viaje_id':'1','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'3','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU8211491','no_precinto':'4','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049109210','peso':'1000','tipo_material':'2',
					'viaje_id':'1','entrada_salida':'entrada'})					
ol.contenedor_movimiento.add({'contenedor_id':'4','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TCNU6183120','no_precinto':'5','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049109210','peso':'1000','tipo_material':'3',
					'viaje_id':'1','entrada_salida':'entrada'})		
ol.contenedor_movimiento.add({'contenedor_id':'5','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'UETU5126400','no_precinto':'6','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049109210','peso':'1000','tipo_material':'3',
					'viaje_id':'1','entrada_salida':'salida'})	
ol.contenedor_movimiento.add({'contenedor_id':'6','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CXDU1260364','no_precinto':'7','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049109211','peso':'1000','tipo_material':'2',
					'viaje_id':'1','entrada_salida':'salida'})	
ol.contenedor_movimiento.add({'contenedor_id':'7','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU9536721','no_precinto':'8','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049109211','peso':'1000','tipo_material':'2',
					'viaje_id':'1','entrada_salida':'salida'})	
ol.contenedor_movimiento.add({'contenedor_id':'8','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'BSIU9445360','no_precinto':'9','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049115610','peso':'1000','tipo_material':'1',
					'viaje_id':'1','entrada_salida':'salida'})	
ol.contenedor_movimiento.add({'contenedor_id':'9','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU8658068','no_precinto':'10','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049115630','peso':'1000','tipo_material':'3',
					'viaje_id':'1','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'10','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TCNU8456538','no_precinto':'11','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049115630','peso':'1000','tipo_material':'3',
					'viaje_id':'1','entrada_salida':'salida'})	
ol.contenedor_movimiento.add({'contenedor_id':'11','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU9588350','no_precinto':'32','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6088110790','peso':'1000','tipo_material':'1',
					'viaje_id':'1','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'12','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TTNU4567705','no_precinto':'33','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6088545310','peso':'1000','tipo_material':'3',
					'viaje_id':'1','entrada_salida':'salida'})		
ol.contenedor_movimiento.add({'contenedor_id':'13','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
#Contenedores viaje 2					
ol.contenedor.add({'numero':'FCIU9848482','no_precinto':'12','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6049116550','peso':'1000','tipo_material':'2',
					'viaje_id':'2','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'14','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'FSCU8455828','no_precinto':'13','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049116550','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'entrada'})		
ol.contenedor_movimiento.add({'contenedor_id':'15','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'FSCU9317757','no_precinto':'14','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6049116550','peso':'1000','tipo_material':'3',
					'viaje_id':'2','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'16','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'TGHU8914740','no_precinto':'15','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6049116550','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'17','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'BMOU4940577','no_precinto':'16','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6049119170','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'18','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'TCNU8071449','no_precinto':'17','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6049121040','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'19','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'TCNU8623086','no_precinto':'18','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6049121050','peso':'1000','tipo_material':'2',
					'viaje_id':'2','entrada_salida':'salida'})					
ol.contenedor_movimiento.add({'contenedor_id':'20','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'BMOU5657089','no_precinto':'19','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049122930','peso':'1000','tipo_material':'3',
					'viaje_id':'2','entrada_salida':'salida'})					
ol.contenedor_movimiento.add({'contenedor_id':'21','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'CBHU3704010','no_precinto':'20','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6049123560','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'22','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'CBHU4036699','no_precinto':'34','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6089685440','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'23','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'CBHU5866900','no_precinto':'34','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6089685440','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'24','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
ol.contenedor.add({'numero':'UETU2267364','no_precinto':'34','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6089685440','peso':'1000','tipo_material':'1',
					'viaje_id':'2','entrada_salida':'salida'})					
ol.contenedor_movimiento.add({'contenedor_id':'25','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})					
#Contenedores viaje 3	
ol.contenedor.add({'numero':'CBHU5578436','no_precinto':'21','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6049124210','peso':'1000','tipo_material':'2',
					'viaje_id':'3','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'26','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'FSCU8461137','no_precinto':'22','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6076033330','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'entrada'})		
ol.contenedor_movimiento.add({'contenedor_id':'27','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU5542460','no_precinto':'23','tipo':'3','observaciones':'Sin observaciones.','no_bl':'COSU6076033340','peso':'1000','tipo_material':'3',
					'viaje_id':'3','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'28','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TCNU4146869','no_precinto':'24','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6079253880','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'29','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU8610059','no_precinto':'25','tipo':'2','observaciones':'Sin observaciones.','no_bl':'COSU6082292830','peso':'1000','tipo_material':'2',
					'viaje_id':'3','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'30','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU3851433','no_precinto':'26','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'entrada'})	
ol.contenedor_movimiento.add({'contenedor_id':'31','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU5888895','no_precinto':'27','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'3',
					'viaje_id':'3','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'32','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'FCIU3581090','no_precinto':'28','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'2',
					'viaje_id':'3','entrada_salida':'entrada'})
ol.contenedor_movimiento.add({'contenedor_id':'33','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'GESU3887450','no_precinto':'29','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'34','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'GLDU5765328','no_precinto':'30','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'2',
					'viaje_id':'3','entrada_salida':'salida'})		
ol.contenedor_movimiento.add({'contenedor_id':'35','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'UETU2117657','no_precinto':'31','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'2',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'36','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'AMFU3195487','no_precinto':'32','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'37','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TCKU3013430','no_precinto':'33','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'3',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'38','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'TTNU3949935','no_precinto':'34','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6084671407','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'salida'})		
ol.contenedor_movimiento.add({'contenedor_id':'39','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'MAGU5263088','no_precinto':'32','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6088109800','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'40','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CXDU1232043','no_precinto':'33','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6088110650','peso':'1000','tipo_material':'3',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'41','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										
ol.contenedor.add({'numero':'CBHU8439223','no_precinto':'34','tipo':'1','observaciones':'Sin observaciones.','no_bl':'COSU6088110780','peso':'1000','tipo_material':'1',
					'viaje_id':'3','entrada_salida':'salida'})
ol.contenedor_movimiento.add({'contenedor_id':'42','movimiento':'descargado','fecha':'2015-08-14','hora':'08:00','puerto':'1','patio':'1'})										