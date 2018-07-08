angular.module('swController', [])

	// inject the Todo service factory into our controller
	.controller('mainController', ['$scope','$http','Todos', function($scope, $http, Todos) {
		$scope.formData = {};
		$scope.loading = false;
		$scope.Appointment = {};
		$scope.temp;
		$scope.patients = {},
		$scope.medis = {},
		$scope.finalAppointment = {};
		$scope.freeSlots = {};
		$scope.freeSlotsAdd = {};
		$scope.doctor = {};
		$scope.edit = true;
        $scope.mediID;

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
		Todos.getAllPatients
            .success(data){
                $scope.patients = data;
                console.log(data);
        }



		Todos.get(mediId)
			.success(function(data){
				console.log(data);
				$scope.doctor = data.objects;

			});

			Todos.getFreeSlots(mediId,day,nextDay)
			.success(function(data){
				console.log(data);
				$scope.freeSlots = data.objects;
			});

			Todos.getAppointment(mediId,day,nextDay)
			.success(async function(data){
				$scope.Appointment = data.objects;
				for(var i =0 ;i<data.objects.length;++i){
				await	 Todos.getPatient(data.objects[i].patient)
						.success(function(data){

							$scope.temp = data.name;

						});

				$scope.Appointment[i].patientName = $scope.temp;
				console.log($scope.Appointment[i]);

			}
			$scope.finalAppointment = $scope.Appointment;
			$scope.loading = false;

		});


			Todos.get()
			.success(function(data) {
				console.log(data);
				$scope.parking = data;
				$scope.loading = false;
			});


			// FUNCTIONS..........................//
		$scope.createFreeSlot = function(freeSlotsAdd) {
			console.log()
			freeSlotsAdd.medi = 'api/v1/medi/'+$scope.doctor[0].id+'/';
			var temparray = freeSlotsAdd.start_time.split('-');
			var timetemp = temparray[2].split('T');
			freeSlotsAdd.start_time = temparray[0]+'-'+temparray[1]+'-'+timetemp[0]+' '+timetemp[1];
			var temparray = freeSlotsAdd.end_time.split('-');
			var timetemp = temparray[2].split('T');
			freeSlotsAdd.end_time = temparray[0]+'-'+temparray[1]+'-'+timetemp[0]+' '+timetemp[1];
			console.log(freeSlotsAdd.startTime);
			Todos.createFreeSlot(freeSlotsAdd)
				.success(function(data){
					Todos.getFreeSlots(mediId,day,nextDay)
					.success(function(data){
					console.log(data);
					$scope.freeSlots = data.objects;
				});
				});

		}

		$scope.deleteFreeSlot = function (id){
			Todos.deleteFreeSlot(id)
				.success(function(data){
				Todos.getFreeSlots(mediId,day,nextDay)
					.success(function(data){
					console.log(data);
					$scope.freeSlots = data.objects;
				});
			});
		}

		$scope.editFreeSlot = function (id) {
			$scope.edit = false;

		}


		$scope.editFreeSlotSave = function(todo){
			Todos.update(todo)
				.success(function(data){
					Todos.getFreeSlots(mediId,day,nextDay)
					.success(function(data){
					console.log(data);
					$scope.freeSlots = data.objects;
					$scope.edit = true;
				});
				});
		}
		//END FUNCTIONS.....//

		// CREATE ==================================================================
		// when submitting the add form, send the text to the node API
		/*$scope.turnOffFan = function(id) {

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


		};

*/
		// DELETE ==================================================================
		// delete a todo after checking it

	}]);