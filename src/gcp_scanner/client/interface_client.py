from abc import ABCMeta, abstractmethod

from googleapiclient import discovery
from httplib2 import Credentials


class IClient(metaclass=ABCMeta):
  """Interface for Client Classes."""

  @staticmethod
  @abstractmethod
  def get_service(credentials: Credentials) -> discovery.Resource:
    """Create a client.

    Args:
      credentials: An google.oauth2.credentials.Credentials object.

    Returns:
      An objet of discovery.Resource
    """

    raise NotImplementedError("Child class must implement create_client")
