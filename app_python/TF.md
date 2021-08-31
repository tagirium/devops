# Best practices for Terraform
Don’t commit the .tfstate file

Configure a backend

Back up your state files

Keep your backends small

Use one state per environment

Setup backend state locking

Execute Terraform in an automated build

Manipulate state only through the commands

Use variables (liberally)

Use modules (only where necessary)

#Problems with Terraform
There was no good provider for VirtualBox, and no documentation. Code snippet that was provided by by developer, didn't 
work and even didn't provide any logs.