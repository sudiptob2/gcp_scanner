import logging

from gcp_scanner.client.compute import ComputeClient


class ClientFactory:
  """Factory class for getting generating SVG."""

  @classmethod
  def get_client(cls, name):
    """Returns the appropriate client."""

    if name == "compute":
      return ComputeClient()

    logging.error("Client not supported.")
    return None
