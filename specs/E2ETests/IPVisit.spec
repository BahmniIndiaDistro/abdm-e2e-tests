# IPD Visits E2E Tests
|mobileNumber|
|9845348122|
## Should be able to get patient lab reports
Tags: prescriptions, diagnostics
* Login to Bahmni location "General Ward" as a receptionist
* Open "Registration" module
* Put first name "Automation" middleName "OPD" last name "prescription" gender "M" mobileNumber <mobileNumber> with yearof birth "2001"
* Put "GAN205238" as patient identifier
* Put healthID "automationopdprescription@sbx"
* Open newly created patient details by healthID
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
* Login to Open ELIS
* Collect Sample
* Enter blood Lab results
* Enter serum Lab results
* Validate lab result "details" in samples collected
* Goto Clinical application
* Open "Patient Documents" module
* Choose newly created patient
* Add a report "labReport1" to "Patient Documents"
* Goto Clinical application
* Open "InPatient" module
* Nurse at ADT gives discharge disposition
* visit is closed at the front desk
* Verify openmrs IPD patient details with mobileNumber <mobileNumber>
* Login to the consent request management system
* Create a consent request for the healthID "automationopdprescription"
|Health Info Types|
|Prescription|
|Discharge Summary|
* Login to PHR app
* approve the consent request of "automationopdprescription@sbx" and password "P@ssw0rd"
|Health Info Types|
|Prescription|
|Discharge Summary|
* wait for "20000"

