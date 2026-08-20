
&AtClient
Procedure CommandProcessing(CommandParameter, CommandExecuteParameters)
	//Inclure le contenu du traitement.
	//FormParameters = New Structure("", );
	//OpenForm("DataProcessor.VentesEnDetail.Form", , CommandExecuteParameters.Source, CommandExecuteParameters.Uniqueness, CommandExecuteParameters.Window, CommandExecuteParameters.URL);
	ОткрытьФорму("DataProcessor.VentesEnDetail.Form", ,CommandExecuteParameters.Source, Новый УникальныйИдентификатор,, CommandExecuteParameters.URL,,РежимОткрытияОкнаФормы.Независимый);
EndProcedure
