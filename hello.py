from mpi4py import MPI
#=============================================================================
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()
#=============================================================================

#% Hello world
print("Hello, World! I am process %d of %d on %s.\n" % (rank, size, name))
