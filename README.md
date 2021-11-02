# idf-version-updater-mac

Workflow for batch version update of IDF files from and to arbitrary versions.

1. Bash scripts should follow the format of `Updater-9.x.0-9.x.0.sh`.

2. `version_update.py` and `version_updater_citybes.py` are the python wrapper to call the bash scripts with a multiprocess workflow.

3. For new release of the EnergyPlus, files in the `/EnergyPlus-9-x-0/PreProcess/IDFVersionUpdater` folder (the installed release version) should be copied to the root folder of the repo.


