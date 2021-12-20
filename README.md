Technologies:
- Python
- Django
- SQLite
- Django Rest Framework
- drf Simple JWT


Django Admin:
- Use authentication
- Manage All Frontend Website Content
- Add/Edit/Delete User
- Add/Edit/Delete Gym 
- Add/Edit/Delete Program
- Add/Edit/Delete Order
- Make payment to add to balance
- Make charge after order 

API:
-    /api/auth/token - Retrieve jwt by username & password
-    /api/auth/token/verify - Check lifetime of jwt
-    /api/auth/me   - Retrieve current user attribute
-   /api/gym    - it returns list of gym and programs related of gym
-   /api/auth/payment - CRUD for payment
-   /api/auth/payment/:id/cancel - cancel payment
-   /api/auth/charges - List of charge
-   /api/gym/order - Make order to buy several program from gym