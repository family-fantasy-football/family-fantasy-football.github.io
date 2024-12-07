from espn_api.football import League
import datetime
from typing import List, Tuple, Dict, Optional
import statistics
import numpy as np
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import math
import os
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import json

from utils import *
from fetch import *

def main():
    SWID = "{42614A28-F6F5-4052-A14A-28F6F52052AF}" 
    ESPN_S2 = "AECeHAkR7FZuTvVWSEnMRIA29wVeroZhvd7fHHy5tZvIUdIp4XIZaglA17V6g2rulDDFMCUiC%2BpeXNqWzEJTpjTJsz5Zv2DTMOIjeX0JrC6CYs8kDidYeF0HHkI78OG2O%2Bs6f%2FUPVSwXRBZEGMKPDdKl%2BE0a7na225JN4bC80tD9RXFv32kqqtEk%2Bgw1hgQ968ARiAdt69axAvjryW57rj58sYK4oMJPxjtPbh9tATi%2BSI2AmQ0dNPXZfRTA%2FFgCtgzyxWNwbKT2boYeDfFe7rm8idW47lnavsfYGwWjVpddVY6%2BcupF7uoc9AeVFQ5xNUY%3D"
    LEAGUE_ID = 697625923
    YEAR = 2024
    league=  League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    
    
    
    
if __name__ == "__main__":
    main()
