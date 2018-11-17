from django.db import models


FacilityType = (
    (1, 'Truck'),
    (2, 'Push Cart')
)

Status = (
    (1, 'REQUESTED'),
    (2, 'APPROVED'),
    (3, 'EXPIRED'),
    (4, 'SUSPEND')
)


class Truck(models.Model):

    locationid = models.IntegerField(null=True, blank=True)
    applicant = models.CharField(max_length=140)
    facilitytype = models.SmallIntegerField(choices=FacilityType, default=1)
    status = models.SmallIntegerField(choices=Status, null=True, blank=True)
    cnn = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    address = models.CharField(max_length=140)
    full_address = models.CharField(max_length=140, default=address)
    permit = models.CharField(max_length=140)
    busy = models.BooleanField(default=False)
    approved = models.DateTimeField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    # location = models.PointField(srid=4326, spatial_index=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.applicant
