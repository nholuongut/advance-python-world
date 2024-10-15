import logging

# logging.basicConfig(
#     level= logging.DEBUG ,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
#     datefmt='%m/%d/%Y %H:%M:%S'
# )

# # types of loggings
# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

# # define logg handlers
# logger = logging.getLogger(__name__)

# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # level& format for each handler
# stream_h.setLevel(level=logging.WARNING)
# file_h.setLevel(level=logging.ERROR)

# formatter = logging.Formatter( '%(name)s - %(levelname)s - %(message)s' )
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# # add handler to the logger
# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# # log
# logger.warning("This is a warning")
# logger.error("This is a error")

#-------------------- loading from config ----------------------------

# import logging.config

# logging.config.fileConfig('logging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug("This is a debug message")


#------------------- error logging --------------------------------
# import traceback

# try :
#     a = [1,2,3]
#     val = a[4]
# except :
#     logging.error( "The error is %s" , traceback.format_exc() )


# --------------------- rotating handlers (for big application keep latest logs)-------------------------
from logging.handlers import RotatingFileHandler , TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# roll over after 2KB and keep backup logs app.log , app.log2
handler = RotatingFileHandler( 'app.log' , maxBytes=2000 , backupCount=5 )

# roll over preset time s,m.h,d,midnight 
handler_time = TimedRotatingFileHandler( 'timed_test.log', 
                                        when='s', 
                                        interval=5 , 
                                        backupCount=5 )

logger.addHandler(handler)

for _ in range(1000):
    logger.info('helo , world !')







