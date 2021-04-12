install kops:
`curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64`
make executable:
`chmod +x ./kops`
Move the binary in to your PATH:
`sudo mv ./kops /usr/local/bin/`


install kubctle:
`curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`
make executable:
`chmod +x ./kubectl`
Move the binary in to your PATH:
`sudo mv ./kubectl /usr/local/bin/kubectl`