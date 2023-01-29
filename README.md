# Update Kubernetes deployment tag in specific namespace.

The first search tag on the namespace example old tag is ` v1.0.0, if have with v1.0.0 tags deployment will be changed example v2.0.0.

## Notice `
 - Will be change all deployments with tag v1.0.0 in the namespace which you specify.
 - Ensure all variables are true before running on production.

## Installation
 Debian/Ubuntu
 ```
 sudo apt-get install python3 python3-pip
 sudo pip3 install kubernetes
 sudo pip3 install logging
 ```

## Variables
 - `namespace`
 - `old_tag`
 - `new_tag`
 - `container_image`