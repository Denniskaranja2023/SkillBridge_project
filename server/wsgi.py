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
from config import app

# Import routes from app.py - this registers all API routes
# We do this AFTER importing config so the app instance is ready
import app

# Print registered routes for debugging
print("=" * 50)
print("SKILLBRIDGE API ROUTES:")
print("=" * 50)
for rule in app.url_map.iter_rules():
    methods = ','.join(sorted([m for m in rule.methods if m not in ['HEAD', 'OPTIONS']]))
    print(f"{methods:15} {rule.rule}")
print("=" * 50)

# Export the app for gunicorn
application = app

