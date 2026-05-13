import __common__

import logging
import sys

from pyrot import ro_interface
from pyrot.config import Config
from pyrot.eye_modelling.datamodels import model_import

# to set logging level in only this script (note that sys needs to be imported for this as well):
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)], force=True)
logger = logging.getLogger(__name__)


# --- user input

import_method = "to_existing_eye_model"  # either 'to_existing_eye_model' or 'create_new_eye_model'
new_eyemodel_name = "imported eye model"  # must be unique an non-empty
new_eyemodel_description = "imported eye model"  # no requirements

# --- end user input

logger.debug("commencing import")

patient = ro_interface.load_current_patient()
import_path = Config.IMPORT_PATH  # TODO: search the correct .json file from the directory
structure_set = ro_interface.load_current_structureset()
geometry_generators, _ = ro_interface.load_eyemodel(structure_set=structure_set, eyemodelnr=Config.EYE_MODEL_NR)

# import the eye model to the relevant structure_set and geometry_generators object

model_import.import_eye_model(geometry_generators, import_path)


logger.debug("import complete")
