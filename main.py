import kubernetes
import os
import logging
logging.root.setLevel(logging.INFO)

def main():
    # Load the kubernetes config
    config_path="kube-config"
    kubernetes.config.load_kube_config(config_path)

    # Create a new Kubernetes client
    client = kubernetes.client.AppsV1Api()

    # Set the namespace,old tag and new tag to search for the deployment
    namespace = "namespace"
    old_tag = "old-tag"
    new_tag = "new-tag"
    container_image = "image"

    # List all deployments in the namespace
    deployments = client.list_namespaced_deployment(namespace)

    # Iterate through the deployments and find the one with the tag "OLD_TAG"
    deployment = None
    for d in deployments.items:
        for c in d.spec.template.spec.containers:
            if c.image == f"${container_image}:{old_tag}":
                deployment = d
                break

    # If the deployment was found, update the tag and restart the deployment
    if deployment is not None:
        logging.info(f"Found deployment with tag {old_tag}, updating to {new_tag} and restarting")

        # Update the deployment's image tag to "NEW_TAG"
        for i, c in enumerate(deployment.spec.template.spec.containers):
            if c.image == f"${container_image}:{old_tag}":
                logging.info(f"Updating to {new_tag}")
                deployment.spec.template.spec.containers[i].image = f"${container_image}:{new_tag}"
                break

        # Update the deployment in the cluster
        client.patch_namespaced_deployment(deployment.metadata.name, namespace, deployment)
    else:
        logging.warning(f"The deployment with tag {old_tag} is not found")

if __name__=="__main__":
    main()