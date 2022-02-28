
## Recipies Web App - Backend

### Installation
On the `app_back/app_back` folder you may find `4` scripts.
- `.install.sh` -- Installs `poetry` version `1.1.12` with `pip3`, installs dependencies with poetry, and activates virtual environment.
- `.create.sh` -- Creates database, all its tables, and populates it.
- `.destroy.sh` -- Destroy database.
- `.start.sh` -- Starts the application.
- `.reset.sh` -- Uses `destroy` then `create` and finally `start`.

For simplicity execute file `.install.sh` and then `.reset.sh`.

##### Notes:
- In case of running into trouble running the scripts, you may use the following command on mentioned scripts. 
    ```
    sudo chmod 777 <script_name>
    ```