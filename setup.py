import subprocess

def run_shell_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}")
        print(stderr.decode())
    else:
        print(stdout.decode())

# Run the installation script from ollama.com
run_shell_command("curl -fsSL https://ollama.com/install.sh | sh")

# Run the docker container with the specified parameters
docker_command = """
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
"""
run_shell_command(docker_command)

# Install Python dependencies
run_shell_command("pip install -r requirements.txt")
run_shell_command("ollama pull mxbai-embed-large")
run_shell_command("pip install --upgrade pip")
run_shell_command('pip install "psycopg[binary,pool]"')