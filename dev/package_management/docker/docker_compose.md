# [Docker Compose](https://docs.docker.com/compose/)

Es una herramienta para definir y ejecutar aplicaciones Docker multicontenedor. Permite configurar la infraestructura de una aplicación a través de un archivo YAML (docker-compose.yml)

- No es ideal para entornos de producción a gran escala
- No proporciona características avanzadas de orquestación como autoescalado o autoreparación.

```bash
# Check the system Docker version
docker --version
> Docker version 20.10.22, build 3a2c30b

# Check the system Docker Compose version
 docker compose version 
> Docker Compose version v2.27.1-desktop.1

# List running compose projects
docker compose ls

# Create and start containers
docker compose up

# Stop and remove containers, networks
docker compose donw
```




