# Canteen Food Pre-Ordering System

A comprehensive Django-based canteen management system with role-based authentication, order management, and receipt generation.

## Features

### 🌐 Front Page
- Welcome screen with role-based login options
- Customer and Shop Owner signup/login

### 🔐 Authentication (Role-Based)
- Customer Signup: Name, Email/Roll No., Password
- Shop Owner Signup: Name, Shop Name, Email, Password
- Session-based authentication

### 🧑‍🎓 Customer Panel
- Browse menu with food images, prices, and stock
- Schedule orders with delivery/pickup time
- Place orders with shopping cart
- Track order status (Pending/Accepted/Ready)
- View order history
- Download PDF receipts

### 🧑‍🍳 Shop Owner Panel
- View and manage incoming orders
- Accept/Reject/Mark as Ready
- Manage food items (Add/Edit/Delete)
- Upload food images
- Update stock and availability
- Daily sales dashboard
- Generate receipts
- Auto stock alerts

### 🖼 UI & UX Features
- Responsive design for mobile and desktop
- Modern Bootstrap-based interface
- Real-time cart management
- Status badges and notifications

## Installation

1. **Clone the repository**
\`\`\`bash
git clone <repository-url>
cd canteen-system
\`\`\`

2. **Create virtual environment**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt 
\`\`\`

4. **Setup MySQL Database**
\`\`\`bash
# Create database
mysql -u root -p
CREATE DATABASE canteen_db;
\`\`\`

5. **Configure environment variables**
\`\`\`bash
cp .env.example .env
# Edit .env with your database credentials
\`\`\`

6. **Run migrations**
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

7. **Create superuser**
\`\`\`bash
python manage.py createsuperuser
\`\`\`

8. **Run the server**
\`\`\`bash
python manage.py runserver
\`\`\`

## Database Schema

### Users Table
- id, username, password, email, role (customer/shop_owner)

### CustomerProfile
- id, user_id (FK), name, roll_no

### ShopOwnerProfile
- id, user_id (FK), name, shop_name

### Food Table
- id, name, price, stock, available (bool), image (URL), shop_id (FK)

### Order Table
- id, customer_id (FK), shop_id (FK), order_time, scheduled_time, total_amount, status

### OrderItem Table
- id, order_id (FK), food_id (FK), quantity, item_status

## Usage

1. **Access the application**: http://localhost:8000
2. **Sign up** as Customer or Shop Owner
3. **Customers**: Browse menu, add items to cart, schedule orders
4. **Shop Owners**: Add food items, manage orders, track sales
5. **Admin Panel**: http://localhost:8000/admin

## Key Features Implemented

✅ Role-based authentication
✅ Responsive UI (mobile & desktop)
✅ Order scheduling
✅ Food image upload
✅ PDF receipt generation
✅ Stock management with auto-alerts
✅ Real-time order tracking
✅ Sales dashboard

## Technologies Used

- **Backend**: Python Django 4.2
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **PDF Generation**: ReportLab
- **Image Handling**: Pillow

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
