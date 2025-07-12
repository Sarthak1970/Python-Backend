# Bank Branches API Server

This project implements an API server to query bank and branch details using Python. We opt for **REST API** . The data for this project can be found in the provided repository database files - https://github.com/Amanskywalker/indian_banks

## 🚀 Features
- **REST API**:
  - Endpoints to retrieve:
    - A list of all banks.
    - Branch details for a specific branch using the IFSC code.
    - Filter branches by bank name and city.
- Clean, modular, and well-commented code for easy extension and maintenance.

### REST API Endpoints:

| Method | Endpoint                               | Description                                   |
|--------|----------------------------------------|-----------------------------------------------|
| GET    | `/banks`                               | Get a list of all banks                       |
| GET    | `/branches/<ifsc>`                     | Get branch details by IFSC                   |
| GET    | `/branches?bank=<bank_name>&city=<city>` | Filter branches by bank name and city         |


