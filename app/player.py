"""
Player class that sets up user id and name
"""

class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid
    @property
    def name(self) -> str:
        return self._name
    
    
    def __str__(self) -> str:
        return f"Player ID: {self._uid}, with the name of: {self._name}"
    