# Here I am showing the DevOps Project Day 4

import docker

# Initialize the Docker client
client = docker.from_env()

# Define container names and images
nginx_container_name = "nginx_container"
nginx_image = "nginx:latest"
mysql_container_name = "mysql_container"
mysql_image = "mysql:latest"
wordpress_container_name = "wordpress_container"
wordpress_image = "wordpress:latest"

# Function to start containers
def start_containers():
    # Start the MySQL container
    client.containers.run(
        image=mysql_image,
        name=mysql_container_name,
        environment=["MYSQL_ROOT_PASSWORD=mysecretpassword"],
        detach=True,
    )
    
    # Start the WordPress container
    client.containers.run(
        image=wordpress_image,
        name=wordpress_container_name,
        ports={"80/tcp": 8080},
        environment=[
            "WORDPRESS_DB_HOST=" + mysql_container_name,
            "WORDPRESS_DB_PASSWORD=mysecretpassword",
        ],
        detach=True,
    )
    
    # Start the Nginx container (proxying to WordPress)
    client.containers.run(
        image=nginx_image,
        name=nginx_container_name,
        ports={"80/tcp": 80},
        volumes={
            "/server.conf": {"bind": "/etc/nginx/conf.d", "mode": "ro"}
        },
        links={wordpress_container_name: "wordpress"},
        detach=True,
    )
    print("Containers started successfully.")

# Function to stop and remove containers
def stop_containers():
    for container_name in [nginx_container_name, wordpress_container_name, mysql_container_name]:
        try:
            container = client.containers.get(container_name)
            container.stop()
            container.remove()
            print(f"Container {container_name} stopped and removed.")
        except docker.errors.NotFound:
            print(f"Container {container_name} not found.")

# Example usage
start_containers()  # Start containers
# Additional actions can be added, such as scaling or monitoring
stop_containers()  # Stop and remove containers when done
