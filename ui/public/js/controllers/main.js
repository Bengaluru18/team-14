angular.module('todoController', [])

	// inject the Todo service factory into our controller
	.controller('mainController', ['$scope','$http','Todos', function($scope, $http, Todos) {
		$scope.formData = {};
		$scope.loading = true;

		// GET =====================================================================
		// when landing on the page, get all todos and show them
		// use the service to get all the todos

		
		
		

		// var temp = date.getDate() + 1;
		// var tomdate = date.getFullYear() + '-' + date.getMonth() + '-' + temp;
		// console.log(tomdate);

		var day = new Date();
		
		

		var nextDay = new Date(day);
		nextDay.setDate(day.getDate()+1);
		

		day = day.getFullYear() + '-' + day.getMonth() + '-' + day.getDate();
		nextDay = nextDay.getFullYear() + '-' + nextDay.getMonth() + '-' + nextDay.getDate();
		console.log(day);
		console.log(nextDay);

		mediId=1;

		Todos.get(mediId,day,nextDay)
			.success(function(data){
				console.log(data);
			});

			Todos.getAppointment(mediId,day,nextDay)
			.success(function(data){
				console.log(data);
			});
			Todos.getAppointment1(mediId,day,nextDay)
			.success(function(data){
				console.log(data);
				Todos.getPatient(data.objects[0].patient)
					.success(function(data){
					console.log(data);
				});
		});


		
		// CREATE ==================================================================
		// when submitting the add form, send the text to the node API
		$scope.turnOffFan = function(id) {

			Todos.getByID(id)
				.success(function(data){
					var update = data;
					if(data.fan == true){
						update.fan = false ;
						$http.put('/api/smarthome/' +id, update)
						.success(function(data){
							console.log(data);
							});
						
					}
			
			});
			Todos.get()
			.success(function(data) {
				console.log(data);
				
			});

		};
		
		$scope.turnOnLight = function(id) {

			Todos.getByID(id)
				.success(function(data){
					var update = data;
					if(data.light == false){
						update.light = true ;
						$http.put('/api/smarthome/' +id, update)
						.success(function(data){
							console.log(data);
							});
						
					}
			
			});
			Todos.get()
			.success(function(data) {
				console.log(data);
				$scope.parking = data;
				$scope.loading = false;
			});

		};
		

		// DELETE ==================================================================
		// delete a todo after checking it
		
	}]);