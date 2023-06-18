worker: apt-get update
worker: apt-get install ca-certificates curl gnupg
worker: install -m 0755 -d /etc/apt/keyrings
worker: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
worker: chmod a+r /etc/apt/keyrings/docker.gpg
worker: echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
worker: apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
web: docker compose up --build