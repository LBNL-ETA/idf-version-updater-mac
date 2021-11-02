from multiprocessing import Pool
from subprocess import call 
import os, sys

NUM_OF_PROCESS = 1

work_folder = 'workfolder'
case_folder = 'ref-buildings'

# list of files to run in parallel
model_list = ['ASHRAE90.1_HotelLarge_STD2010_SanDiego_new']

def upgrade_idf(model_list):
	for model_name in model_list:
		idf_name = os.path.join(work_folder, case_folder, model_name + '.idf')
		
		if (os.path.isdir(work_folder) and os.path.exists(idf_name)):
			print(idf_name)
			idf_name_new = os.path.join(work_folder, case_folder, model_name + '.idfnew')
			idf_name_origin =os.path.join(work_folder, case_folder, model_name + '_origin.idf')

			call(["./Updater-9.2.0-9.5.0.sh", idf_name, idf_name_new, idf_name_origin])

if __name__ == '__main__':

	run_set = list()
	total_size = len(model_list)
	thread_size = int(total_size / NUM_OF_PROCESS) + 1

	end_num = 0
	for set_num in range(NUM_OF_PROCESS - 1):
	    start_num = set_num * thread_size
	    end_num = (set_num + 1) * thread_size
	    run_set.append(model_list[start_num: end_num])

	run_set.append(model_list[end_num: ])

	pool = Pool(NUM_OF_PROCESS) 
	results = pool.map(upgrade_idf, run_set)

	pool.close() 
	pool.join()