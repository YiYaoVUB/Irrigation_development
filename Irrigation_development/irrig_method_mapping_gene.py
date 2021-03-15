import netCDF4 as nc
import numpy

file_obj = nc.Dataset('E:\Irrigation\codes_making_data\data_new\mksrf_gdp_0.5x0.5_AVHRR_simyr2000.c130228.nc','w')
file_obj.createDimension('lat', size = 360)
file_obj.createDimension('lon', size = 720)
file_obj.createDimension('cft', size = 64)



floor = file_obj.createVariable('floor_fraction', 'f8', ('lat', 'lon', 'cft'))
floor.long_name = 'fractional floor irrigation method'
floor.units = ' '
floor.mode = ' '

sprinkler = file_obj.createVariable('sprinkler_fraction', 'f8', ('lat', 'lon', 'cft'))
sprinkler.long_name = 'fractional sprinkler irrigation method'
sprinkler.units = ' '
sprinkler.mode = ' '

drip = file_obj.createVariable('drip_fraction', 'f8', ('lat', 'lon', 'cft'))
drip.long_name = 'fractional drip irrigation method'
drip.units = ' '
drip.mode = ' '


file_obj2 = nc.Dataset('E:\Irrigation\\cft1900_2005_irrigation_systems_64bands_baseline.nc','r')

Eb = file_obj2.variables['variable']
var_Eb = numpy.array(Eb)


for i in range(4, 8):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48, :, :]

for i in range(10, 18):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48, :, :]

for i in range(46, 48):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16+1, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32+1, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48+1, :, :]

for i in range(0, 4):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 2, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 2, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 2, :, :]

for i in range(60, 62):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 2, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 2, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 2, :, :]

for i in range(36, 38):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 3, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 3, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 3, :, :]

for i in range(48, 50):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 3, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 3, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 3, :, :]

for i in range(42, 44):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 4, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 4, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 4, :, :]

for i in range(50, 52):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 5, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 5, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 5, :, :]

for i in range(18, 20):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 6, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 6, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 6, :, :]

for i in range(54, 56):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 7, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 7, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 7, :, :]

for i in range(8, 10):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 8, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 8, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 8, :, :]

for i in range(62, 64):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 8, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 8, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 8, :, :]

for i in range(34, 36):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 9, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 9, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 9, :, :]

for i in range(44, 46):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 10, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 10, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 10, :, :]

for i in range(52, 54):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 11, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 11, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 11, :, :]

for i in range(20, 30):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 12, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 12, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 12, :, :]

for i in range(32, 34):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 12, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 12, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 12, :, :]

for i in range(38, 42):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 12, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 12, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 12, :, :]

for i in range(30, 32):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 13, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 13, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 13, :, :]

for i in range(56, 60):
    file_obj['floor_fraction'][:, :, i] = var_Eb[16 + 14, :, :]
    file_obj['sprinkler_fraction'][:, :, i] = var_Eb[32 + 14, :, :]
    file_obj['drip_fraction'][:, :, i] = var_Eb[48 + 14, :, :]
print('test')