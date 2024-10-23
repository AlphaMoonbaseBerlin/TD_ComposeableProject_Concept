'''Info Header Start
Name : GeneralConfig_callbacks
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.11880
Info Header End'''

def GetConfigSchema(configModule:"SchemaObjects", configComp:"JsonConfig") -> dict:
	
	
	return {
		"Global" : configModule.CollectionDict({
			"TransportPort" : configModule.ConfigValue(
				9500, comment ="The port that is used for the transport using TouchIn/Out"
			)
		}),
		"Plugins" : configModule.CollectionDict({
			operator.name : configModule.CollectionDict({
				"Active" : configModule.ConfigValue( False ),
				"Settings" : configModule.CollectionDict({
					parameter.name : configModule.ConfigValue( parameter.eval() ) for parameter in operator.customPars if parameter.page.name == "Settings"
				})
			}) for operator in iop.Store.Pluginmanager.Plugins.values()
		})
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""