# ThankTank Backend

## Deployment
The `deploy.sh` script buidls the backend api in different deployment flavors. It uses the different docker-compose files to run the Docker containers.

### Development
Run `./deploy.sh dev` to create backend on machines with no NGINX/CertBot/Https protection.

### Production
Run `./deploy.sh prod` to create backend on machines with NGINX/CertBot/Https protection.

### Logging
Run `./deploy.sh logs {dev|prod}` to follow your containers' logs.
Run `./deploy.sh {dev|prod} -f` to follow your containers' logs during build.
