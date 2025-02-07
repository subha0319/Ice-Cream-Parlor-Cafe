# Ice-Cream-Parlor-Cafe

Welcome to the **Ice Cream Cafe** project! This repository now contains a modern microservices implementation of the Ice Cream Cafe application, with each service containerized using Docker and orchestrated with Docker Compose.

## **Overview:**
The application simulates an ice cream parlor's operations through a set of independent microservices. Each service is built with Flask and handles a specific domain:

- **Flavor Service:** Manages flavors and customer suggestions.
- **Inventory Service:** Manages inventory, ingredients, and allergens.
- **Order Service:** Manages customer orders (cart operations).

## **Structure**

      Ice-Cream-Parlor-Cafe/
        ├── docker-compose.yml
        ├── README.md
        ├── main.py
        ├── requirments.txt
        ├── flavor_service/
        │   ├── app.py
        │   ├── database.py
        │   ├── requirements.txt
        │   └── Dockerfile
        ├── inventory_service/
        │   ├── app.py
        │   ├── database.py
        │   ├── requirements.txt
        │   └── Dockerfile
        └── order_service/
            ├── app.py
            ├── database.py
            ├── requirements.txt
            └── Dockerfile

## **Features:**
- **Flavor Service:**
  - View all flavors.
  - View seasonal flavors.
  - Add a new flavor.
  - Submit flavor suggestions.
  
- **Inventory Service:**
  - View current inventory.
  - Update inventory for flavors.
  - Manage ingredients and allergens.
  
- **Order Service:**
  - Create new orders.
  - View all orders.

## **Setup and Installation:**

### **Pre-requisites:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine.
- Basic knowledge of command-line tools.
- (Optional) [Postman](https://www.postman.com/downloads/) for testing the REST APIs.

### **Steps to Run the Application:**

1. **Clone this Repository:**

   ```cmd
   git clone https://github.com/subha0319/Ice-Cream-Parlor-Cafe.git
   cd Ice-Cream-Parlor-Cafe

2. **Build and Run the Microservices with Docker Compose:**

    ```cmd
    docker-compose up --build

This command builds and starts all three services:

- **Flavor Service** on port 5000
- **Inventory Service** on port 5001
- **Order Service** on port 5002

---

## **Testing the Services**

You can test the REST API endpoints using your web browser or Postman:

### **Flavor Service Endpoints:**
- `GET http://localhost:5000/flavors` – **Retrieve all flavors**.
- `POST http://localhost:5000/flavors` – **Add a new flavor** (provide a JSON payload, e.g., `{ "name": "Mint", "seasonal": false }`).
- `POST http://localhost:5000/suggestions` – **Submit a flavor suggestion** (if implemented as a separate endpoint).

### **Inventory Service Endpoints:**
- `GET http://localhost:5001/inventory` – **View current inventory**.
- `PUT http://localhost:5001/inventory/<flavor>` – **Update inventory for a specific flavor** (provide a JSON payload, e.g., `{ "quantity": 30 }`).

### **Order Service Endpoints:**
- `GET http://localhost:5002/orders` – **Retrieve all orders**.
- `POST http://localhost:5002/orders` – **Create a new order** (provide a JSON payload, e.g., `{ "flavor_id": 1, "quantity": 2 }`).

---

## **Application Flow**

Each microservice provides dedicated endpoints for its domain:

### **Flavor Service:**
- `GET /flavors`: **List all available flavors**.
- `GET /flavors?seasonal=true`: **List seasonal flavors**.
- `POST /flavors`: **Add a new flavor**.
- `POST /suggestions`: **Submit a flavor suggestion**.

### **Inventory Service:**
- `GET /inventory`: **Retrieve inventory details**.
- `PUT /inventory/{flavor}`: **Update stock quantity for a specific flavor**.

### **Order Service:**
- `GET /orders`: **List all orders**.
- `POST /orders`: **Create a new order**.

---

## **Testing the Application:**

### **Using Postman:**

#### **Create a New Collection:**
- **Organize** your API endpoints (e.g., "Ice Cream Cafe APIs").

#### **Add Requests for Each Endpoint:**

For the **Flavor Service**:
- `GET`: `http://localhost:5000/flavors`
- `POST`: `http://localhost:5000/flavors` (with a JSON body)

For the **Inventory Service**:
- `GET`: `http://localhost:5001/inventory`
- `PUT`: `http://localhost:5001/inventory/{flavor}`

For the **Order Service**:
- `GET`: `http://localhost:5002/orders`
- `POST`: `http://localhost:5002/orders`

#### **Run Tests:**
- Use **Postman's Collection Runner** or **Newman** to automate your API testing.

---

## **Future Enhancements:**

- **Enhance error handling and validations**.
- **Implement authentication and authorization** for secure access.
- **Expand inter-service communication** (e.g., using message queues).
- **Add functionality for updating and deleting entries**.
- **Convert CLI-based features** into additional web-based interfaces.

By following these instructions, you'll be able to run and test the Ice Cream Cafe application using a scalable microservices architecture. Enjoy exploring and enhancing the project!

---

