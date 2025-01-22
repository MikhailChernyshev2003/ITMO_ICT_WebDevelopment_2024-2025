from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AirlineListView, AirportListView, PlaneListView, MaintenanceListView, EmployeeListView, \
    CrewMemberListView, CrewListView, RouteListView, FlightListView, SeatListView, TransitStopListView, \
    most_frequent_plane, low_occupancy_routes, check_free_seats, planes_in_maintenance, company_employees_count

router = DefaultRouter()
router.register('airlines', AirlineListView)
router.register('airports', AirportListView)
router.register('planes', PlaneListView)
router.register('maintenances', MaintenanceListView)
router.register('employees', EmployeeListView)
router.register('crew-members', CrewMemberListView)
router.register('crews', CrewListView)
router.register('routes', RouteListView)
router.register('flights', FlightListView)
router.register('seats', SeatListView)
router.register('transit-stops', TransitStopListView)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('analytics/most-frequent-plane/', most_frequent_plane, name='most_frequent_plane'),
    path('analytics/low-occupancy-routes/<int:percentage>/', low_occupancy_routes, name='low_occupancy_routes'),
    path('analytics/check-free-seats/<int:flight_id>/', check_free_seats, name='check_free_seats'),
    path('analytics/planes-in-maintenance/', planes_in_maintenance, name='planes_in_maintenance'),
    path('analytics/company-employees-count/<int:airline_id>/', company_employees_count, name='company_employees_count'),
]