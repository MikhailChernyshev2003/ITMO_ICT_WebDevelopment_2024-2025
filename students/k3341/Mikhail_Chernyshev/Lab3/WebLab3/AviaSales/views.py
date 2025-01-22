from django.db.models import F, Count
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from AviaSales.models import Airline, Airport, Plane, Maintenance, Employee, CrewMember, Crew, Route, Flight, Seat, TransitStop
from AviaSales.serializers import AirlineSerializer, AirportSerializer, PlaneSerializer, MaintenanceSerializer, EmployeeSerializer, CrewMemberSerializer, CrewSerializer, RouteSerializer, FlightSerializer, SeatSerializer, TransitStopSerializer


class AirlineListView(ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class AirportListView(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class PlaneListView(ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class MaintenanceListView(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class EmployeeListView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CrewMemberListView(ModelViewSet):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer


class CrewListView(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class RouteListView(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class FlightListView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class SeatListView(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class TransitStopListView(ModelViewSet):
    queryset = TransitStop.objects.all()
    serializer_class = TransitStopSerializer


def most_frequent_plane(request):
    most_frequent = (
        Plane.objects.annotate(flight_count=Count('flights'))
        .order_by('-flight_count')
        .first()
    )
    if most_frequent:
        return JsonResponse({'plane_model': most_frequent.model, 'flight_count': most_frequent.flight_count})
    return JsonResponse({'message': 'Нет данных'}, status=404)


def low_occupancy_routes(request, percentage):
    routes = (
        Route.objects.filter(
            flights__sold_tickets_number__lt=F('flights__plane__seats_capacity') * (percentage / 100)
        )
        .distinct()
    )
    data = [{'route': str(route), 'flight_count': route.flights.count()} for route in routes]
    return JsonResponse({'low_occupancy_routes': data})


def check_free_seats(request, flight_id):
    free_seats = Seat.objects.filter(flight_id=flight_id, is_sold=False).count()
    return JsonResponse({'free_seats': free_seats})


def planes_in_maintenance(request):
    planes_in_repair = Maintenance.objects.filter(status__in=['Scheduled', 'In Progress']).count()
    return JsonResponse({'planes_in_maintenance': planes_in_repair})


def company_employees_count(request, airline_id):
    airline = Airline.objects.filter(id=airline_id).first()
    if airline:
        employee_count = airline.employees.count()
        return JsonResponse({'airline': airline.name, 'employee_count': employee_count})
    return JsonResponse({'message': 'Авиакомпания не найдена'}, status=404)