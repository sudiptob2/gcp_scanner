import logging
import sys
from typing import List, Dict, Any

from googleapiclient import discovery


class CrawlCompute:
  """Crawler class for compute resources."""

  @classmethod
  def get_compute_instances_names(
      cls, project_name: str, service: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of Compute VMs available in the project.

    Args:
      project_name: A name of a project to query info about.
      service: A resource object for interacting with the Compute API.

    Returns:
      A list of instance objects.
    """

    logging.info("Retrieving list of Compute Instances")
    images_result = list()
    try:
      request = service.instances().aggregatedList(project=project_name)
      while request is not None:
        response = request.execute()
        if response.get("items", None) is not None:
          for _, instances_scoped_list in response["items"].items():
            for instance in instances_scoped_list.get("instances", []):
              images_result.append(instance)

        request = service.instances().aggregatedList_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to enumerate compute instances in the %s",
                   project_name)
      logging.info(sys.exc_info())
    return images_result

  @classmethod
  def get_compute_images_names(
      cls, project_name: str, service: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of Compute images available in the project.

    Args:
      project_name: A name of a project to query info about.
      service: A resource object for interacting with the Compute API.

    Returns:
      A list of image objects.
    """

    logging.info("Retrieving list of Compute Image names")
    images_result = list()
    try:
      request = service.images().list(project=project_name)
      while request is not None:
        response = request.execute()
        for image in response.get("items", []):
          images_result.append(image)

        request = service.images().list_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to enumerate compute images in the %s", project_name)
      logging.info(sys.exc_info())
    return images_result

  @classmethod
  def get_compute_disks_names(
      cls, project_name: str, service: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of Compute disks available in the project.

    Args:
      project_name: A name of a project to query info about.
      service: A resource object for interacting with the Compute API.

    Returns:
      A list of disk objects.
    """

    logging.info("Retrieving list of Compute Disk names")
    disk_names_list = list()
    try:
      request = service.disks().aggregatedList(project=project_name)
      while request is not None:
        response = request.execute()
        if response.get("items", None) is not None:
          for _, disks_scoped_list in response["items"].items():
            for disk in disks_scoped_list.get("disks", []):
              disk_names_list.append(disk)

        request = service.disks().aggregatedList_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to enumerate compute disks in the %s", project_name)
      logging.info(sys.exc_info())

    return disk_names_list

  @classmethod
  def get_static_ips(cls, project_name: str,
                     service: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of static IPs available in the project.

    Args:
      project_name: A name of a project to query info about.
      service: A resource object for interacting with the Compute API.

    Returns:
      A list of static IPs in the project.
    """

    logging.info("Retrieving Static IPs")

    ips_list = list()
    try:
      request = service.addresses().aggregatedList(project=project_name)
      while request is not None:
        response = request.execute()
        for name, addresses_scoped_list in response["items"].items():
          if addresses_scoped_list.get("addresses", None) is None:
            continue
          ips_list.append({name: addresses_scoped_list})

        request = service.addresses().aggregatedList_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to get static IPs in the %s", project_name)
      logging.info(sys.exc_info())

    return ips_list

  @classmethod
  def get_compute_snapshots(cls, project_name: str,
                            service: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of Compute snapshots available in the project.

    Args:
      project_name: A name of a project to query info about.
      service: A resource object for interacting with the Compute API.

    Returns:
      A list of snapshot objects.
    """

    logging.info("Retrieving Compute Snapshots")
    snapshots_list = list()
    try:
      request = service.snapshots().list(project=project_name)
      while request is not None:
        response = request.execute()
        for snapshot in response.get("items", []):
          snapshots_list.append(snapshot)

        request = service.snapshots().list_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to get compute snapshots in the %s", project_name)
      logging.info(sys.exc_info())

    return snapshots_list

  @classmethod
  def get_subnets(cls, project_name: str,
                  compute_client: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of subnets available in the project.

    Args:
      project_name: A name of a project to query info about.
      compute_client: A resource object for interacting with the Compute API.

    Returns:
      A list of subnets in the project.
    """

    logging.info("Retrieving Subnets")
    subnets_list = list()
    try:
      request = compute_client.subnetworks().aggregatedList(project=project_name)
      while request is not None:
        response = request.execute()
        if response.get("items", None) is not None:
          for name, subnetworks_scoped_list in response["items"].items():
            subnets_list.append((name, subnetworks_scoped_list))

        request = compute_client.subnetworks().aggregatedList_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to get subnets in the %s", project_name)
      logging.info(sys.exc_info())

    return subnets_list

  @classmethod
  def get_firewall_rules(
      cls, project_name: str, compute_client: discovery.Resource) -> List[Dict[str, Any]]:
    """Retrieve a list of firewall rules in the project.

    Args:
      project_name: A name of a project to query info about.
      compute_client: A resource object for interacting with the Compute API.

    Returns:
      A list of firewall rules in the project.
    """

    logging.info("Retrieving Firewall Rules")
    firewall_rules_list = list()
    try:
      request = compute_client.firewalls().list(project=project_name)
      while request is not None:
        response = request.execute()
        for firewall in response.get("items", []):
          firewall_rules_list.append((
            firewall["name"],
            # firewall['description'],
          ))

        request = compute_client.firewalls().list_next(
          previous_request=request, previous_response=response)
    except Exception:
      logging.info("Failed to get firewall rules in the %s", project_name)
      logging.info(sys.exc_info())
    return firewall_rules_list
