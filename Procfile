aptu: apt-get update
apti: apt-get install ca-certificates curl gnupg
keyi: install -m 0755 -d /etc/apt/keyrings
curlgpg: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmodgpg: chmod a+r /etc/apt/keyrings/docker.gpg
dockerconf: echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
dockeri: apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
web: docker compose up --build