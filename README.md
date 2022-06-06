# fermi-ngc2071

## Usage

1. Connect to the remote server via SSH with port forwarding (ignore this step if you are working locally)

    ```
    $ ssh -L 8888:localhost:8888 <username>@<host>
    ```

2. Clone the repository

    ```
    $ git clone https://github.com/epassaro/fermi-ngc2071.git
    ```

3. Build the Docker image

    > :warning: **WARNING:** If the download links are down, run [the query](./data/query.txt) again on [Fermi's website](https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi) and re-generate `wget.txt`.

    ```
    $ cd fermi-ngc2071
    $ docker build . -t epassaro/fermipy:latest
    ```

4. Run the Jupyter notebook from a new container

    ```
    $ docker run -p 8888:8888 epassaro/fermipy:latest
    ```

5. Paste the given URL in your browser

## Docker commands

See: https://docs.docker.com/engine/reference/commandline/docker/

- **List all images:** `docker image ls`
- **List all containers:** `docker ps -a`
- **List containers by image:** `docker ps -a --filter "ancestor=epassaro/fermipy:latest"`
- **Restart container:** `docker start -ia <container ID or NAME>`
- **Get container resource usage:** `docker stats <container ID or NAME>`
- **Remove container:** `docker rm <container ID or NAME>`
- **Remove unused data:** `docker system prune -a`
- **Remove unused data and volumes:** `docker system prune -a --volumes`
