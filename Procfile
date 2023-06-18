aptu: sudo apt-get update
apti: sudo apt-get install ca-certificates curl gnupg
keyi: sudo install -m 0755 -d /etc/apt/keyrings
curlgpg: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmodgpg: sudo chmod a+r /etc/apt/keyrings/docker.gpg
dockerconf: echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
dockeri: sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
web: sudo docker compose up --build