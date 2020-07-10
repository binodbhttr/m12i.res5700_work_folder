import gizmo_analysis as gizmo
import utilities as ut

simname = 'm12i_res7100_mhdcv'
simdir = '/scratch/projects/xsede/GalaxiesOnFIRE/mhdcv/m12i_res7100_mhdcv/1Myr/'
snapnumber = 696

part = gizmo.io.Read.read_snapshots(['star'],'snapshot_index', snapnumber, simulation_name=simname, simulation_directory=simdir, assign_hosts=True, assign_hosts_rotation=True)  

