import json

class Config:
    def __init__(self, filename, serverId=''):
        self.filename = f"{filename}.json"
        self.serverId = str(serverId)
        with open(f"{self.filename}", 'r') as f:
            self.data = json.load(f)
            if self.serverId != '':
                self.fileData = self.data
                self.data = self.data[serverId]
            
    
    def getServer(self):
        """getServer get the server name from config

        Returns:
            [str]: [server name]
        """
        return self.data['server_id']
    
    def getChannels(self):
        """getChannels get channel ID's from config

        Returns:
            list: channel ID's (ints)
        """
        return self.data["channels-id"]
    
    def getStartHour(self):
        """getStartHour get the start hour for slowmode start

        Returns:
            str: hour by 24h format (00:00)
        """
        return self.data["start-hour"]
    
    def getEndHour(self):
        """getEndHour get the end hour for slowmode end

        Returns:
            str: hour by 24h format (00:00)
        """
        return self.data["end-hour"]
    
    def getSeconds(self):
        """getSeconds get how many seconds to set the slowmode

        Returns:
            int: amount of seconds
        """
        return self.data['seconds']
    
    def getNotifyChat(self):
        """getNotifyChat get staff text chat ID

        Returns:
            int: ID number
        """
        return self.data['notify-chat-id']
    
    def getRoleNotifierId(self):
        """getRoleNotifierId get the role the bot tags when he notifies about a new user

        Returns:
            int: 0 for everyone, otherwise the ID, could be list if its several roles
        """
        return self.data['notify-role-id']
    
    def isCheckingAge(self):
        """isCheckingAge check if the bot check the user age and notify about it

        Returns:
            bool: true/false
        """
        return self.data['check-age']
    
    def getHighestMembers(self):
        """getHighestMembers get the highest member number in voice record from config.json

        Returns:
            int: number of members
        """
        return self.data['highest-members-in-voice']
    
    def setCheckingAge(self, value):
        """setCheckingAge set the value of checking age, true if the bot will check user age and notify and false otherwise

        Args:
            value (bool): the value
        """
        self.fileData[self.serverId]['check-age'] = value
        a_file = open(self.filename, "w")
        json.dump(self.fileData, a_file, indent=4)
        a_file.close()

    def setSeconds(self, seconds):
        """setSeconds set the number of seconds the slowmdoe will be

        Args:
            seconds (int): amount of seconds
        """
        self.fileData[self.serverId]['seconds'] = seconds
        a_file = open(self.filename, "w")
        json.dump(self.fileData, a_file, indent=4)
        a_file.close()
    
    def setNotifyChannel(self, channel_id):
        """setNotifyChannel set the channel to notify when a new user joins

        Args:
            channel_id (int): the channel ID
        """
        self.fileData[self.serverId]['notify-chat-id'] = channel_id
        a_file = open(self.filename, "w")
        json.dump(self.fileData, a_file, indent=4)
        a_file.close()
    
    def setHighestMembers(self, membercount):
        self.fileData[self.serverId]['highest-members-in-voice'] = int(membercount)
        a_file = open(self.filename, "w")
        json.dump(self.fileData, a_file, indent=4)
        a_file.close()
    
    

def getConfigs():
        configs = []
        config = Config("config")
        #print(type(config.data))
        for server in list(config.data.keys()):
            configs.append(Config("config", server))
        return configs

def get_channels(client, config):
    channels = config.getChannels()
    channels_utils = []
    for channel in channels:
        channel_util = client.get_channel(channel)
        channels_utils.append(channel_util)
    print(f"CHANNELS UTILS {channels_utils}")
    return channels_utils
        

