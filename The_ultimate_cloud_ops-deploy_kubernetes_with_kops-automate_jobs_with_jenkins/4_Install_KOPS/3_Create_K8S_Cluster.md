create the cluster:
`kops update cluster ${NAME} --yes`

validate:
`kops validate cluster`

restart instances:
`kops rolling-update cluster`


`kubectl get all`
`kubectl get nodes`
`kubectl apply -f .`