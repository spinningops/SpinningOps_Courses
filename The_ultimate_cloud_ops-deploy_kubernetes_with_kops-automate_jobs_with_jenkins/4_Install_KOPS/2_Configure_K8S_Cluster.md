add the var name cluster name:
`export NAME=k8s.spinningops.com`


add S3:
`export KOPS_STATE_STORE=s3://kops-state`


list the AZ (here it's for us-east-1):
`aws ec2 describe-availability-zones --region us-east-1`


create configuration files for the cluster, and add the zones:
`kops create cluster --zones us-east-1a,us-east-1b,us-east-1c ${NAME} --yes`


creates kops secret ssh:
`ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa`
`kops create secret --name ${NAME} sshpublickey admin -i ~/.ssh/id_rsa.pub`


edit the cluster:
`kops edit cluster ${NAME}`


edit nodes number:
`kops edit ig nodes --name ${NAME}`


list the master and nodes min, max and zones:
`kops get ig --name ${NAME}`


edit the number of nodes master:
`kops edit ig master-us-east-1a --name ${NAME}`