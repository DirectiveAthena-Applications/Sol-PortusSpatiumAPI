# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Athena Packages
from AthenaDocumentor import AthenaDocumentorParser, OutputChoice, Settings

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    Settings(
        document_dunders=True,
        document_private=True,
        # print_unvisited=True,
        print_visited=True,
    )

    AthenaDocumentorParser(
        root_folder_path="../src",
        output_folder_path="../docs",
        output_choice=OutputChoice.JSON
    ).parse()

if __name__ == '__main__':
    main()