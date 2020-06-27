
from icepyx import icesat2data as ipd

short_name = 'ATL06'
date_range = ['2018-10-14','2020-04-04']
# bounding box for DEM
bbox = [-75, -76.5, -74.5, -76]
    #[-76.5, -79.5, -76, -79]
    #[-122, 47, -120, 48]
    #[-121.87893182746436, 48.70258466806347, -121.79542720391288, 48.7704252035505]

#bbox = [(-55, 68), (-55, 71), (-48, 71), (-48, 68), (-55, 68)]
#print (len(bbox))
#reg_a = ipd.Icesat2Data('ATL06', [-55, 68, -48, 71], ['2019-02-20', '2019-02-28'])
#print (reg_a.file_meta())

region = ipd.Icesat2Data(short_name, bbox, date_range)

print('product:    ', region.dataset)
print('dates:      ', region.dates)
print('start time: ', region.start_time)
print('end time:   ', region.end_time)
print('version:    ', region.dataset_version)
print('extent:     ', region.spatial_extent)

# search for available granules and provide basic summary info about them
print('\nDATA:')
print('\n'.join([str(item) for item in region.avail_granules().items()]))

# visualize data extents
region.visualize_spatial_extent(elevplot=True)
