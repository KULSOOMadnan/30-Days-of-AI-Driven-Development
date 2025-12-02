# Data Model for Basic Python Calculator

**Date**: 2025-12-02

## Entities

### Number

-   **Description**: Represents a numerical value used in calculations.
-   **Attributes**:
    -   `value`: integer or float
-   **Validation Rules**:
    -   Must be a valid number.
    -   If an integer, must be within the range of -1000 to 1000.

### Operation

-   **Description**: Represents an arithmetic operation.
-   **Attributes**:
    -   `operator`: string (`+`, `-`, `*`, `/`)
-   **Validation Rules**:
    -   Must be one of the supported operators.
