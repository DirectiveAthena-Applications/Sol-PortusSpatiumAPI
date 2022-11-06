# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class ApiResponse:
    result:Any = None
    errors:list = field(default_factory=list)
    status:int = 500

    def to_dict(self) -> dict:
        if self.errors:
            return {
                "result": self.result,
                "errors": self.errors
            }
        else:
            return {
                "result": self.result,
            }
