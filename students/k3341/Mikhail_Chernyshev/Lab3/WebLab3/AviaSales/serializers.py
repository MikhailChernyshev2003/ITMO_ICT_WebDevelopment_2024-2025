from rest_framework import serializers
from .models import Airline, Airport, Plane, Maintenance, Employee, CrewMember, Crew, Route, Flight, Seat, TransitStop


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer(read_only=True)

    class Meta:
        model = Plane
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    plane = PlaneSerializer(read_only=True)

    class Meta:
        model = Maintenance
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    employer = AirlineSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class CrewMemberSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = CrewMember
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
    captain = CrewMemberSerializer(read_only=True)
    co_pilot = CrewMemberSerializer(read_only=True)
    navigator = CrewMemberSerializer(read_only=True)
    attendants = CrewMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Crew
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    departure_airport = AirportSerializer(read_only=True)
    destination_airport = AirportSerializer(read_only=True)
    stops = AirportSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    crew = CrewSerializer(read_only=True)
    route = RouteSerializer(read_only=True)
    plane = PlaneSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = '__all__'


class TransitStopSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    airport = AirportSerializer(read_only=True)

    class Meta:
        model = TransitStop
        fields = '__all__'