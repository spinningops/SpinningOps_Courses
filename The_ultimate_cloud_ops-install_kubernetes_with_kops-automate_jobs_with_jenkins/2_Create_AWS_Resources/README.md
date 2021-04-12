1. Create IAM User   
`aws iam create-user --user-name KOPS`   
`aws iam list-groups`   
`aws iam add-user-to-group --user-name KOPS --group-name Admins`   

2. Create EC2 SSH Key-Pair   
`aws ec2 create-key-pair --key-name KOPS_KeyPair`   
`chmod 400 my-key-pair.pem`   

3. Create S3 Bucket   
`aws s3 mb s3://newbucket –region us-east-1`   

4. Create Sub-Domain Route 53   
`aws route53 create-hosted-zone --name example.com --caller-reference 2014-04-01-18:47 --hosted-zone-config Comment="command-line version"`   

5. Create Sub-Domain at your DNS registrar