# TEST PLAN


| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** | **Pass/Fail** |
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  T_01_A     | correct pin to enter the system  | 3412 |SUCCESS | SUCCESS | PASS |
|  T_02_B     | wrong pin is entered | 7865 | FAIL | FAIL |PASS |
|  T_03_A     | add book with correct input| (1). Unique id (2). Book name (3). Author name (4). Category (5). No. of pages (6). price | SUCCESS | SUCCESS | PASS |
|  T_04_A     | Search book on basis of book name| (1). Book name | (1). Book name (2). Author name  | (1). Book name (2). Author name | PASS |
|  T_05_B     | Search book which is not available | (1). Book name | BOOK_NOT_AVAILABLE | BOOK_NOT_AVAILABLE | PASS |
|  T_06_A     | List of book present in the system | Enter choice | SUCCESS | SUCCESS | PASS |
|  T_07_A     | Update the bbook record which exists | (1). Book id (3). Book name (4). Author name (5). Category (6). No. of pages (7). price  | SUCCESS | SUCCESS | PASS |
|  T_08_A     | Count of particular book on the basis on category which exists| (1). Book Category  | count = 2 | count = 2 | PASS |
|  T_09_B      | Count of particular book on the basis on category which doesnit exist| (1). Book Category  | count = 0 | count = 0 | PASS |
