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
        return self.data['server_id']
    
    def getChannels(self):
        return self.data["channels-id"]
    
    def getStartHour(self):
        return self.data["start-hour"]
    
    def getEndHour(self):
        return self.data["end-hour"]
    
    def getSeconds(self):
        return self.data['seconds']

    def setSeconds(self, seconds):
        #config = Config(filename, "246691336776843265")
        self.fileData[self.serverId]['seconds'] = seconds
        
        a_file = open(self.filename, "w")
        json.dump(self.fileData, a_file, indent=2)
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
        


# configs = getConfigs()
# for config in configs:
#     print(type(config))
#     print(config.getChannels())