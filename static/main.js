function dataImport() {
    d3.json("/api/mvf").then(function (data) {
		
        console.log(data);
		var chart = bb.generate({
			data: {
			  columns: [
			  ["Males with Heart Disease ", data['male']],
			  ["Males w/o Heart Disease", 1- data['male']]
			  ],
			  type: "pie", // for ESM specify as: pie()		  
			},
			bindto: "#m Chart"
		  });
		var chart = bb.generate({
		data: {
			columns: [
			["Females with Heart Disease", data['female']],
			["Females w/o Heart Disease", 1- data['female']]
			],
			type: "pie", // for ESM specify as: pie()		  
		},
		bindto: "#f Chart"
		  });
	
	})
}
dataImport()



