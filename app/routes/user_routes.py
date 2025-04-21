# app/routes/user_routes.py
from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint('user', __name__)
users_bp = Blueprint('users', __name__)
user_controller = UserController()

user_bp.route('/users', methods=['GET'])(user_controller.get_all_users)
user_bp.route('/user/create', methods=['GET', 'POST'])(user_controller.register_user)

