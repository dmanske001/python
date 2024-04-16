class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    saved_volume = 0

    def __init__(self) -> None:
        """
        Method to set default values of Television object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to change status of Television to on (True) if off(False) or to off(False) if on(True)
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to change muted status to True if False, or False if True.
        This method also changes the saved_volume variable to whatever
        the current volume is, so that it can be accessed by the volume
        methods.
        """
        if self.__status:
            self.saved_volume = self.__volume

            if self.__muted == False:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            elif self.__muted == True:
                self.__volume = self.saved_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        This method changes the channel up and includes
        logic to "wrap" around if the maximum channel size
        is reached.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
            This method changes the channel down and includes
            logic to "wrap" around if the minimum channel size
            is reached.
            """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This method adjusts the volume up, as long as the volume is
        not already at maximum. It also will unmute if muted==True and
        set the volume to the saved_volume
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.saved_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """This method adjusts the volume down, as long as the volume is
        not already at minimum. It also will unmute if muted==True and
        set the volume to the saved_volume"""
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.saved_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:

            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
