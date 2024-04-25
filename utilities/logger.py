import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="automation.log", level=logging.INFO,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
