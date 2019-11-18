from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class DatabaseAdapter(object, ABC):
    @abstractmethod
    def get_key(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about a key, such as ratelimit information and whether it's unlimited.

        Returns
        -------
        None if non-existent, or a dict.
        """
        raise NotImplementedError

    @abstractmethod
    def get_keys_for(self, user_id: str) -> Optional[List[Dict[str, Any]]]:
        """
        Retrieves all keys belonging to the user_id.

        Returns
        -------
        A list of dicts.
        """
        raise NotImplementedError

    @abstractmethod
    def create_application(self, application: dict):
        """
        Creates an application with the provided information.
        """
        raise NotImplementedError

    @abstractmethod
    def create_key(self, key: dict):
        """
        Creates a key with the provided information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_keys_sorted_by(self, order_key: str, ordering: str) -> List[Dict[str, Any]]:
        """
        Retrieves all keys and sorts them by the given key, using the given ordering method.

        Parameters
        ----------
        order_key: str
            The key to order the documents by.
        ordering: str
            How the documents should be ordered. This should only be either `ascending`
            or `descending`.

        Returns
        -------
        A list of dicts.
        """
        raise NotImplementedError


    @abstractmethod
    def get_applications_ordered_by(self, order_key: str) -> List[Dict[str, Any]]:
        """
        Retrieves all applications, ordered by the given key.

        Returns
        -------
        A list of dicts.
        """
        raise NotImplementedError

    @abstractmethod
    def get_application(self, application_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the application with the given id.

        Returns
        -------
        None, if non-existent, or a dict.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_application(self, application_id: str):
        """
        Deletes the application with the given id.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_key(self, key: str):
        """
        Deletes the document with the given key.
        """
        raise NotImplementedError

    @abstractmethod
    def is_key_valid(self, key: str) -> bool:
        """
        Checks whether the key is valid.

        Returns
        -------
        True, if the key is valid.
        """
        raise NotImplementedError

    @abstractmethod
    def update_key_data(self, key: str, data: dict):
        """
        Updates data associated with a key.
        """
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """
        Closes the database connection.
        """
        raise NotImplementedError
