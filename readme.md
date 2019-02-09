This is three small program for Ormuco, tested in Python 3.7

###Question 3 design considerations:

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.
Add/put, get, remove, check_expiry
To make it more usable, in the longer run, we could support some data events. For example, a event handler can be added when a cached item expires so we can refresh the cache items automatically
  

 2 - Resilient to network failures or crashes.
Multiple distributed instance with hot/hot or hot/backup cache data. One consideration is about persistence. If supported, the instance itself will be able survive machine crash/restart and rebuild most of the cached items 

    
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
Cache need to be in RAM, at least frequently used items. If the latency should be very low, we may need to consider location affinity to get cache from closest nodes(see below too)
    

4 - Data consistency across regions
Data replication between nodes, exception handling cases such as node crash and rebuild, communication between nodes disconnected and resync after connection restore
   

 5 - Locality of reference, data should almost always be available from the closest region
Cache node need to marked and manged with locality info. Client get the node from a node manager who knows the 
   

 6 - Flexible Schema
We do not enforce schema for it. It is just key/value store, and client can use/validate  schema they like
    

7 - Cache can expire 
time check when getting the cached value
timer/background thread will scan the caches, and release the item to GC
to avoid memory overlow, we set cache memory usage limit, and persist the least used items (need to consider pickling) to disk or simply delete them if overflow to disk is not supported

a short summary of the components:
Cache master  manager nodes and find service node for clients
service nodes store the real caches and reply back to clients, the interface can be REST based if that’s appropriate
Client can continue to use that node if it feels appropriate or request a new node info from the master

this is a big project, I will just implement a simple version covering 1,6, 7 demonstrating the simple usage