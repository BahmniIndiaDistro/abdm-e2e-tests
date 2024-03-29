# Merge Patient Visits
|mobileNumber|
|+91-9876543210|

## Should be able to get patient lab reports and prescriptions after merge
Tags:prescriptions, diagnostics
* Login to Bahmni location "General Ward" as a receptionist
* Open "Registration" module
* Create a new patient with random patient details
* Add this newly created patient as merge patient1
* Start an OPD Visit
* Doctor opens clinical tab
* Doctor enters basic clinical details
* visit is closed at the front desk
* Goto Clinical application
* Open "Registration" module
* Create a new patient with random patient details
* Add this newly created patient as merge patient2
* Start an IPD Visit
* Doctor issues an Admit disposition
* Goto Clinical application
* Admit a patient to general ward bed "305-b"
* Goto Clinical application
* Doctor opens clinical tab
* Doctor enters basic clinical details
* Doctor issues an Discharge disposition
* Goto Clinical application
* Open "InPatient" module
* Doctor at ADT gives discharge disposition
* visit is closed at the front desk
* Goto the openMRS Admin tab
* Merge the newly created patients
* Verify openmrs OPD patient details with mobileNumber <mobileNumber>
* Verify openmrs IPD patient details with mobileNumber <mobileNumber>

