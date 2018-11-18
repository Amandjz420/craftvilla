from shapely.geometry import MultiPoint

from django.db.models import F

from elapi import CreateView, RetrieveView, ListView, UpdateView, DeleteView
from .schema import ApplicantSchema, TruckSchema, ExpirationSchema, StreetSchema, AssignTruckSchema
from .models import Truck


class ApplicantApi(CreateView):
    """
    Api for searching truck by applicant's name
    """
    schema_class = ApplicantSchema

    def perform_create(self, data):
        return TruckSchema().dump(Truck.objects.filter(applicant__icontains=data["name"]), many=True).data


class StreetApi(CreateView):
    """
    Api for searching truck by Street's name
    """
    schema_class = StreetSchema

    def perform_create(self, data):
        return TruckSchema().dump(Truck.objects.filter(address__icontains=data["street"]), many=True).data


class ExpirationApi(CreateView):
    """
    Api for searching truck by expiration's date
    """
    schema_class = ExpirationSchema

    def perform_create(self, data):
        date = data["date"].date()
        return TruckSchema().dump(Truck.objects.filter(
            expiration__year=date.year,
            expiration__month=date.month,
            expiration__day=date.day,
        ), many=True).data


class TruckListApi(ListView, CreateView):
    """
    Api for Listing Trucks and creating a new one
    """
    schema_class = TruckSchema

    def get_queryset(self):
        return Truck.objects.all()

    def perform_create(self, data):
        truck = Truck.objects.create(**data)
        return {"created": truck.id}


class TruckRetrieveApi(RetrieveView, UpdateView, DeleteView):
    """
    Api for getting a detail of a Truck,also updating and deleting
    """
    schema_class = TruckSchema

    def get_schema_kwargs(self):
        kwargs = super(TruckRetrieveApi, self).get_schema_kwargs()
        if self.request.method == 'DELETE':
            kwargs.update({'partial': True})
        return kwargs

    def get_queryset(self):
        return Truck.objects.all()

    def perform_update(self, instance, data):
        for key, value in data.iteritems():
            if value:
                setattr(instance, key, value)
        instance.save()
        return TruckSchema().dump(instance).data

    def perform_delete(self, instance, data):
        instance.delete()
        return {"status": "Deleted"}


class AssignTruckApi(CreateView):
    """
    Api for assigning a job to a truck
    """

    schema_class = AssignTruckSchema

    def perform_create(self, data):
        pts = []
        for point in data['points']:
            pts.append((point['x'], point['y']))
        centroid = MultiPoint(pts)
        x = centroid.centroid.x
        y = centroid.centroid.y
        truck = Truck.objects.filter(busy=False, status=2, facilitytype=1).\
            annotate(abs_diff=pow(F('latitude')-x, 2) + pow(F('longitude')-y, 2)).order_by("abs_diff").first()
        if truck:
            truck.busy = True
            truck.save()
            return TruckSchema().dump(truck).data
        else:
            return {"status": "No truck free for job"}
