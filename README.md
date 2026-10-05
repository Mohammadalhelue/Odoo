# Odoo Smart Inventory & Procurement Integrator

An end-to-end Odoo 17 ERP custom module designed to automate inventory tracking and procurement through external IoT device integration. This project demonstrates advanced Odoo ORM manipulation, REST/JSON-RPC API development, and automated business logic within a containerized PostgreSQL environment.

## 🚀 Business Use Case
In manufacturing or large corporate environments, tracking real-time material consumption is often delayed. This module allows external devices (like barcode scanners or IoT sensors) to hit an API endpoint whenever an employee consumes a material. The system automatically:
1. Deducts the consumed quantity from stock.
2. Validates the consumption against the employee's departmental budget.
3. Automatically triggers a Request for Quotation (RFQ) in the Purchase module if stock drops below predefined minimum thresholds.

## 🛠️ Tech Stack & Key Skills Demonstrated
*   **Framework:** Odoo 17.0 Community Edition
*   **Language:** Python 3.12, XML
*   **Database:** PostgreSQL 15
*   **Integration:** REST / JSON-RPC API Controllers
*   **Environment:** Docker, Docker Compose, Linux (WSL)
*   **Odoo Concepts:** Custom Models, ORM (Compute, Onchange, Constraints), Controller routing, Access Rights, Views (Tree/Form/Menus).

## ⚙️ Setup & Installation (Docker)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/odoo-smart-inventory-integrator.git](https://github.com/your-username/odoo-smart-inventory-integrator.git)
   cd odoo-smart-inventory-integrator
