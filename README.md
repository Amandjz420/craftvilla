# craftvilla










# Api:

Api for searching truck with applicant name

http://localhost:8000/api/truck/applicant/

payload request: {"name": "MOMO INNOVATION LLC"}

response :
[
    [
        {
            "status": 1,
            "busy": false,
            "applicant": "MOMO INNOVATION LLC",
            "longitude": -122.400747494077,
            "cnn": 3527000,
            "locationid": 1221094,
            "full_address": "CALIFORNIA ST: BATTERY ST to SANSOME ST (300 - 399)",
            "permit": "18MFF-0107",
            "latitude": 37.7928707497415,
            "facilitytype": 1,
            "approved": null,
            "address": "351 CALIFORNIA ST",
            "expiration": null
        },
        {
            "status": 1,
            "busy": false,
            "applicant": "MOMO INNOVATION LLC",
            "longitude": -122.40103337535,
            "cnn": 9094000,
            "locationid": 1221093,
            "full_address": "MISSION ST: ANNIE ST to 03RD ST (663 - 699)",
            "permit": "18MFF-0107",
            "latitude": 37.7865580501799,
            "facilitytype": 1,
            "approved": null,
            "address": "667 MISSION ST",
            "expiration": null
        }
    ],
    {}
]