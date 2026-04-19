# Chapter 6: Testing

This chapter documents manual and scripted tests for the IT Helpdesk Chatbot. Tests use the trained classifier (`model/chatbot_model.pkl`) and the fixed response map in the Streamlit application. Each case records the user input, the expected behaviour, the actual bot reply, and the result.

**Test environment:** Local run; inputs passed through the same prediction and response logic as `app/app.py`.

---

## 1. Basic Functionality

| Test Case ID | Input    | Expected Output   | Actual Output                      | Status |
| ------------ | -------- | ----------------- | ---------------------------------- | ------ |
| TC01         | Hello    | Greeting response | Hello! How can I assist you today? | Pass   |
| TC02         | Hi there | Greeting response | Hello! How can I assist you today? | Pass   |

---

## 2. Password Reset

| Test Case ID | Input                   | Expected Output      | Actual Output                                                                 | Status |
| ------------ | ----------------------- | -------------------- | ----------------------------------------------------------------------------- | ------ |
| TC03         | I forgot my password    | Password reset steps | To reset your password, go to settings > reset password and follow the steps. | Pass   |
| TC04         | Reset my login password | Password reset steps | To reset your password, go to settings > reset password and follow the steps. | Pass   |

---

## 3. Login Issue

| Test Case ID | Input                      | Expected Output      | Actual Output                                                                                                    | Status |
| ------------ | -------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------ | ------ |
| TC05         | I am stuck on login screen | Login issue solution | Please check your credentials or clear cache. If the issue persists, contact support.                            | Pass   |
| TC06         | Unable to login            | Login issue solution | Please check your credentials or clear cache. If the issue persists, contact support.                             | Pass   |

---

## 4. Technical Issue

| Test Case ID | Input                 | Expected Output          | Actual Output                                                        | Status |
| ------------ | --------------------- | ------------------------ | -------------------------------------------------------------------- | ------ |
| TC07         | System not responding | Technical issue solution | Try restarting system or checking internet. Contact support if needed. | Pass   |
| TC08         | App is crashing       | Technical issue solution | Try restarting system or checking internet. Contact support if needed. | Pass   |

---

## 5. Software Help

| Test Case ID | Input                   | Expected Output       | Actual Output                               | Status |
| ------------ | ----------------------- | --------------------- | ------------------------------------------- | ------ |
| TC09         | Install VPN             | Installation guidance | Download from official website and follow installation steps. | Pass   |
| TC10         | How to install software | Installation guidance | Download from official website and follow installation steps. | Pass   |

---

## 6. Ticket Status

| Test Case ID | Input                  | Expected Output | Actual Output                                    | Status |
| ------------ | ---------------------- | --------------- | ------------------------------------------------ | ------ |
| TC11         | Check my ticket status | Ticket response | Please provide your ticket ID. This is a demo system. | Pass   |
| TC12         | Track my issue         | Ticket response | Please provide your ticket ID. This is a demo system. | Pass   |

---

## 7. Thanks and Exit

| Test Case ID | Input  | Expected Output    | Actual Output              | Status |
| ------------ | ------ | ------------------ | -------------------------- | ------ |
| TC13         | Thanks | Thank you response | You're welcome! 😊         | Pass   |
| TC14         | Bye    | Goodbye message    | Goodbye! Have a great day! | Pass   |

---

## 8. Edge Cases

| Test Case ID | Input         | Expected Output                         | Actual Output                                                                 | Status |
| ------------ | ------------- | --------------------------------------- | ----------------------------------------------------------------------------- | ------ |
| TC15         | asdfgh        | Unknown / “Sorry, I didn't understand…” | Try restarting system or checking internet. *(classifier maps to technical)* | Fail   |
| TC16         | 12345         | Unknown / fallback                      | Same as TC15                                                                  | Fail   |
| TC17         | *(empty)*     | Warning: please enter a message           | No bot reply; empty input is not submitted/processed by the current UI logic. | N/A    |

---

## Summary

- **Passed:** 14 cases (TC01–TC06, TC07–TC14).
- **Failed:** 2 cases — TC15–TC16 (no unknown-intent path; model always picks a label).
- **Not applicable:** TC17 — empty-input message is not implemented in the app; Streamlit chat input does not drive the handler on empty text.

These results match the machine-readable log in `report/chapter6_test_results.csv`.

---

## Notes for the viva

The chatbot was tested with cases covering all defined intents plus edge inputs. Results show strong behaviour on clear, in-vocabulary phrases; remaining limitations include the absence of a confidence-based “unknown” reply for gibberish or numeric-only input (TC15–TC16). Empty-input validation can be added in a future iteration if required (TC17).
