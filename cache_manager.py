from datetime import datetime, timedelta


class CacheItem:
    def __init__(self, key, value, current_time=datetime.now(), expiry_time=timedelta(minutes=60)):
        self.key = key
        self.value = value
        self.access_time = current_time
        self.expiry_time = expiry_time


class CacheManager:
    def __init__(self):
        self.items = {}

    def add(self, key, value, current_time=datetime.now(), expiry_time=timedelta(minutes=60)):
        if self.items.get(key, None):
            self.items[key].value = value
            self.items[key].access_time = current_time
            self.items[key].expiry_time = expiry_time
            self._update_item_time(current_time)
        else:
            self.items[key] = CacheItem(key, value, current_time, expiry_time)

    def get(self, key, current_time=datetime.now()):
        item = self.items.get(key, None)
        if item:
            if current_time - item.access_time < item.expiry_time:
                self._update_item_time(item, current_time)
                return item.value
            else:
                print('item {} is expired'.format(item.key))
                self.remove(key)
        return None

    def remove(self, key):
        if key in self.items:
            print('item {} is removed'.format(key))
            self.items.pop(key)

    def _update_item_time(self, item, time):
        item.access_time = time
