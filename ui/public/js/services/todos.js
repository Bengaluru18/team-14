angular.module('todoService', [])

	// super simple service
	// each function returns a promise object 
	.factory('Todos', ['$http',function($http) {
		return {
			get : function(mediId) {
				return $http.get('http://54.254.144.216:8000/api/v1/medi?medi__id='+mediId);
			},
			getFreeSlots : function(mediId,day,nextDay) {
				return $http.get('http://54.254.144.216:8000/api/v1/mediavailability?medi__id='+mediId+'&start_time__gte='+day+'&end_time__gte='+nextDay);
			},
			getAppointment : function(mediId,day,nextDay) {
				return $http.get('http://54.254.144.216:8000/api/v1/appointment?medi__id='+mediId+'&start_time__gte='+day+'&end_time__gte='+nextDay);
			},
			getPatient : function(patientId) {
				
				return $http.get('http://54.254.144.216:8000'+patientId);
			},
			createFreeSlot : function(todoData) {
				return $http.post('http://54.254.144.216:8000/api/v1/mediavailability', todoData);
			},
			delete : function(id) {
				return $http.delete('/api/smarthome/' + id);
			},
			update : function(id) {
				return $http.put('/api/smarthome/' + id);
			},
			getByID : function(id) {
				return $http.get('/api/smarthome/' + id);
			}
		}
	}]);