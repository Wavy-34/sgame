import time as tm


class Log:

    def __init__(self, keep_in_logs: bool = False) -> None:
        self.__keep_in_logs: bool = keep_in_logs

    def __get_time(
        self,
    ) -> (
        str
    ):  # get the current time and return a str with the following format "YYYY-MM-DD HH:MM:SS"
        self.__current_time: tm.struct_time = tm.localtime()
        self.__normalized_time: str = (
            f"[{self.__current_time.tm_year:04}-{self.__current_time.tm_mon:02}"
            f"-{self.__current_time.tm_mday:02} {self.__current_time.tm_hour:02}"
            f":{self.__current_time.tm_min:02}:{self.__current_time.tm_sec:02}]"
        )

        return self.__normalized_time

    def __add_to_logs(
        self, time: str, text: str, loglvl: str
    ) -> None:  # add to a txt files the log lines, default False
        if self.__keep_in_logs:
            with open("./logfile.txt", "a") as t:
                t.write(f"{time} [{loglvl}]: {text}")

    def linfo(self, text: str) -> None:  # log with lvl=INFO
        time: str = self.__get_time()

        print(f"{time} [INFO]: {text}")
        self.__add_to_logs(time, text, "INFO")

    def lerror(self, text: str) -> None:  # log with lvl=ERROR
        time: str = self.__get_time()

        print(f"{time} [ERROR]: {text}")
        self.__add_to_logs(time, text, "ERROR")

    def ldebug(self, text: str) -> None:  # log with lvl=DEBUG
        time: str = self.__get_time()

        print(f"{time} [DEBUG]: {text}")
        self.__add_to_logs(time, text, "DEBUG")

    def ladmin(self, text: str) -> None:  # log with lvl=ADMIN
        time: str = self.__get_time()

        print(f"{time} [ADMIN]: {text}")
        self.__add_to_logs(time, text, "ADMIN")


if __name__ == "__main__":
    pass
