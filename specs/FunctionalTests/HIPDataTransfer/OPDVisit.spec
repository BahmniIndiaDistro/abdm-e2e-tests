# OPD Visits
   |mobileNumber  |
   |--------------|
   |+91-9876543210|

## Should be able to get patient external lab reports and prescriptions

tags: prescriptions, diagnostics

* Login to Bahmni location "General Ward" as a receptionist
* Receptionist creates the patient and starts an OPD
* Doctor initiates clinical checkup
* Doctor advises medicines "opd/prescriptionFlow/prescriptions" and tests "opd/prescriptionFlow/labTests"
* lab technician uploads patient document and radiology reports
* visit is closed at the front desk
* Verify openmrs OPD patient details with mobileNumber <mobileNumber>

## Should be able to get OPConsultation notes of a patient

tags: OPConsultation

* Login to Bahmni location "General Ward" as a receptionist
* Receptionist creates the patient and starts an OPD
* Doctor opens clinical tab
* Doctor captures BP, sugar checkup
* Doctor captures the consultation notes "consultationNotes" for newly created patient
* Doctor advises medicines "opd/prescriptionFlow/prescriptions" and tests "opd/prescriptionFlow/labTests"
* lab technician uploads patient document and radiology reports
* visit is closed at the front desk
* Verify openmrs OPD patient details with mobileNumber <mobileNumber>

## Should be able to get in house lab reports and prescriptions of a patient

tags: prescriptions, diagnostics

* Login to Bahmni location "General Ward" as a receptionist
* Receptionist creates the patient and starts an OPD
* Doctor initiates clinical checkup
* Doctor captures the consultation notes "consultationNotes" for newly created patient
* Doctor advises medicines "opd/prescriptionFlow/prescriptions" and tests "opd/prescriptionFlow/labTests"
* Login to Open ELIS
* Collect Sample
* Enter blood Lab results
* Enter serum Lab results
* Validate lab result "details" in samples collected
* Goto Clinical application
* visit is closed at the front desk
* Verify openmrs OPD patient details with mobileNumber <mobileNumber>

