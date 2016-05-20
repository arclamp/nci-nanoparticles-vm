import girder_client
import json
import sys


# Log into Girder.
gc = girder_client.GirderClient(apiUrl="http://localhost:8080/api/v1")
gc.authenticate("admin", "adminadmin")

# Find the Resonant Lab main collection.
collection = gc.get("collection", {"text": "ResonantLaboratory"})
if len(collection) == 0:
    print >>sys.stderr, "FATAL ERROR: No such collection 'ResonantLaboratory'"

cID = collection[0]["_id"]

# Create an item.
folder = gc.load_or_create_folder('Data', cID, 'collection')
item = gc.load_or_create_item('nanoparticles.json', folder["_id"])

# Activate the item as database-backed.
gc.post("item/%s/database" % (item["_id"]), data=json.dumps({"type": "mongo",
                                                             "url": "mongodb://localhost",
                                                             "database": "NanoDB3",
                                                             "collection": "Nano_combined_0301_filled"}))
