# IPD Visits
|mobileNumber|
|+91-9876543210|
## Should be able to get patient lab reports
Tags: prescriptions, diagnostics
* Login to Bahmni location "General Ward" as a receptionist
* Open "Registration" module
* Create a new patient with gender "Female" with random name, aged "29" with mobile number <mobileNumber>
* Start an IPD Visit
* Doctor issues an Admit disposition
* Goto Clinical application
* Admit a patient to general ward bed "304-d"
* Goto Clinical application
* Nurse opens clinical tab
* Nurse enters basic clinical details
* Doctor prescribes tests "opd/prescriptionFlow/labTests"
* Doctor prescribes medications "opd/prescriptionFlow/prescriptions"
* Doctor issues an Discharge disposition
* Goto Clinical application
* Open "Patient Documents" module
* Choose newly created patient
* Add a report "labReport1" to "Patient Documents"
* Goto Clinical application
* Open "InPatient" module
* Nurse at ADT gives discharge disposition
___
* visit is closed at the front desk
* Verify openmrs IPD patient details with mobileNumber <mobileNumber>

