from googleapiclient import discovery
from httplib2 import Credentials

from interface_client import IClient


class ComputeClient(IClient):
  """ComputeClient class."""

  def get_service(self, credentials: Credentials) -> discovery.Resource:
    """Create compute client..

    Args:
      credentials: An google.oauth2.credentials.Credentials object.

    Returns:
      An objet discovery.Resource
    """
    return discovery.build(
      'compute',
      'v1',
      credentials=credentials,
      cache_discovery=False,
    )
