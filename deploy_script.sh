#!/bin/bash

#!/bin/bash

# Navigate to the app directory
cd GarbageGaugeSite

# Pull the latest changes from the production branch
git pull origin production

# Restart the application service (example for systemd)
sudo systemctl restart your-app-service
