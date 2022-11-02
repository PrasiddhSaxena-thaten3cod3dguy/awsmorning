import logging

logging.basicConfig(filename="awsmorning.log",filemode="w",format='[%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("just a debug message in line 9")
logger.info("This is just for your FYI")
logger.warning("This is my last warning before everthing goes bad")
logger.error("This is an error at Line 12")
logger.critical("Your weekend is ruined by line 13")
