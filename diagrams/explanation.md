
# Health API: Tables, Relationships, and Data Flow

## 1. **User & Roles**

### **Tables & Relationships**
- **User**
  - Standalone (referenced by many tables)
- **Role**
  - Standalone (may be referenced by users or permissions)
- **AuditLog**
  - `user_id` → User

### **Data Flow**
- **User** is created when a new account is registered.
- **Role** is created by admins to define permissions.
- **AuditLog** is populated when a user performs an auditable action.

---

## 2. **Patient & Doctor**

### **Tables & Relationships**
- **Patient**
  - Standalone (referenced by appointments, medical records, etc.)
- **Doctor**
  - Standalone (referenced by appointments, medical records, etc.)

### **Data Flow**
- **Patient** and **Doctor** are created during onboarding or registration.

---

## 3. **Appointments & Medical Records**

### **Tables & Relationships**
- **Appointment**
  - `patient_id` → Patient
  - `doctor_id` → Doctor
- **MedicalRecord**
  - `patient_id` → Patient
  - `doctor_id` → Doctor

### **Data Flow**
- **Appointment** is created when a patient books a visit.
- **MedicalRecord** is created/updated after a visit.

---

## 4. **Telemedicine**

### **Tables & Relationships**
- **VirtualVisit**
  - `patient_id` → Patient
  - `doctor_id` → Doctor
- **ChatLog**
  - `patient_id` → Patient
  - `doctor_id` → Doctor
- **VideoSession**
  - `virtual_visit_id` → VirtualVisit

### **Data Flow**
- **VirtualVisit** is created for a telemedicine session.
- **VideoSession** is created when a video call starts.
- **ChatLog** is populated as messages are exchanged.

---

## 5. **Lab**

### **Tables & Relationships**
- **LabOrder**
  - `patient_id` → Patient
  - `doctor_id` → Doctor
- **LabResult**
  - `lab_order_id` → LabOrder
- **DiagnosticImage**
  - `patient_id` → Patient
  - `doctor_id` → Doctor

### **Data Flow**
- **LabOrder** is created when a test is ordered.
- **LabResult** is created when results are available.
- **DiagnosticImage** is created when an image is taken.

---

## 6. **Referral**

### **Tables & Relationships**
- **ReferralRequest**
  - `patient_id` → Patient
  - `referring_doctor_id` → Doctor
  - `specialist_id` → Doctor
  - `status_id` → ReferralStatus
- **ReferralStatus**
  - Standalone (referenced by ReferralRequest)
- **SpecialistNote**
  - `referral_request_id` → ReferralRequest
  - `specialist_id` → Doctor

### **Data Flow**
- **ReferralRequest** is created for a specialist referral.
- **ReferralStatus** is updated as the referral progresses.
- **SpecialistNote** is added by the specialist.

---

## 7. **Pharmacy**

### **Tables & Relationships**
- **Medication**
  - Standalone (referenced by Prescription)
- **Prescription**
  - `patient_id` → Patient
  - `doctor_id` → Doctor
  - `medication_id` → Medication
- **PharmacyOrder**
  - `prescription_id` → Prescription
  - `pharmacy_id` → Pharmacy (if exists)

### **Data Flow**
- **Medication** is managed by admins/pharmacists.
- **Prescription** is created by a doctor.
- **PharmacyOrder** is created when a prescription is sent to a pharmacy.

---

## 8. **Insurance & Billing**

### **Tables & Relationships**
- **InsurancePlan**
  - Standalone (referenced by InsuranceClaim)
- **InsuranceClaim**
  - `patient_id` → Patient
  - `plan_id` → InsurancePlan
- **Payment**
  - `claim_id` → InsuranceClaim
- **Invoice**
  - `patient_id` → Patient

### **Data Flow**
- **InsurancePlan** is created by admins.
- **InsuranceClaim** is created when a claim is filed.
- **Payment** is created when a claim is paid.
- **Invoice** is generated for billing.

---

## 9. **Device Integration**

### **Tables & Relationships**
- **WearableDevice**
  - `user_id` → User
- **DeviceData**
  - `device_id` → WearableDevice
- **RemoteMonitoringLog**
  - `device_id` → WearableDevice

### **Data Flow**
- **WearableDevice** is registered by a user.
- **DeviceData** is uploaded from the device.
- **RemoteMonitoringLog** is created for monitoring events.

---

## 10. **Patient Portal**

### **Tables & Relationships**
- **Message**
  - `sender_id` → User
  - `receiver_id` → User
- **EducationalResource**
  - Standalone
- **Feedback**
  - `user_id` → User
- **Survey**
  - Standalone

### **Data Flow**
- **Message** is sent between users.
- **EducationalResource** is created by admins.
- **Feedback** is submitted by users.
- **Survey** is created/administered by admins.

---

## 11. **Consent Management**

### **Tables & Relationships**
- **ConsentForm**
  - Standalone
- **ConsentHistory**
  - `consent_form_id` → ConsentForm
  - `user_id` → User

### **Data Flow**
- **ConsentForm** is created by admins.
- **ConsentHistory** is updated when a user gives/revokes consent.

---

## 12. **Notifications**

### **Tables & Relationships**
- **Notification**
  - `user_id` → User

### **Data Flow**
- **Notification** is created when a user receives a system message.

---

# Summary Table

| Table                   | Main Foreign Keys                                      | Populated When...                                 |
|-------------------------|--------------------------------------------------------|---------------------------------------------------|
| **User**                | —                                                      | User registers                                    |
| **Role**                | —                                                      | Role is created                                   |
| **AuditLog**            | user_id → User                                         | User performs auditable action                    |
| **Patient**             | —                                                      | Patient registers                                 |
| **Doctor**              | —                                                      | Doctor registers                                  |
| **Appointment**         | patient_id, doctor_id                                  | Appointment is booked                             |
| **MedicalRecord**       | patient_id, doctor_id                                  | After a visit                                     |
| **VirtualVisit**        | patient_id, doctor_id                                  | Telemedicine session scheduled                    |
| **ChatLog**             | patient_id, doctor_id                                  | Message sent in virtual visit                     |
| **VideoSession**        | virtual_visit_id                                       | Video call started                                |
| **LabOrder**            | patient_id, doctor_id                                  | Lab test ordered                                  |
| **LabResult**           | lab_order_id                                           | Lab result available                              |
| **DiagnosticImage**     | patient_id, doctor_id                                  | Diagnostic image taken                            |
| **ReferralRequest**     | patient_id, referring_doctor_id, specialist_id, status_id | Referral made                                 |
| **ReferralStatus**      | —                                                      | Referral status created/updated                   |
| **SpecialistNote**      | referral_request_id, specialist_id                     | Specialist adds note                              |
| **Medication**          | —                                                      | Medication added                                  |
| **Prescription**        | patient_id, doctor_id, medication_id                   | Doctor prescribes medication                      |
| **PharmacyOrder**       | prescription_id, pharmacy_id                           | Prescription sent to pharmacy                     |
| **InsurancePlan**       | —                                                      | Insurance plan created                            |
| **InsuranceClaim**      | patient_id, plan_id                                    | Insurance claim filed                             |
| **Payment**             | claim_id                                               | Payment made for claim                            |
| **Invoice**             | patient_id                                             | Invoice generated                                 |
| **WearableDevice**      | user_id                                                | Device registered                                 |
| **DeviceData**          | device_id                                              | Device uploads data                               |
| **RemoteMonitoringLog** | device_id                                              | Monitoring event logged                           |
| **Message**             | sender_id, receiver_id                                 | User sends message                                |
| **EducationalResource** | —                                                      | Resource created                                  |
| **Feedback**            | user_id                                                | User submits feedback                             |
| **Survey**              | —                                                      | Survey created                                    |
| **ConsentForm**         | —                                                      | Consent form created                              |
| **ConsentHistory**      | consent_form_id, user_id                               | User gives/revokes consent                        |
| **Notification**        | user_id                                                | Notification sent                                 |

