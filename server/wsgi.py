# WSGI config for SkillBridge application.
#
# This module creates the WSGI application that gunicorn will use.
# It ensures all routes from app.py are properly registered.

import sys
import os

# Add server directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import config first to initialize app, db, api
# config.py creates the Flask app and initializes extensions
from config import app as application

