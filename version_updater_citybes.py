from multiprocessing import Pool
from subprocess import call
import os, sys

NUM_OF_PROCESS = 4

work_folder = 'workfolder/SF_100'
model_name = 'model_origin'
model_list = os.listdir(work_folder)

def upgrade_idf(work_list):
	for bldg_name in work_list:
		cur_work_folder = os.path.join(work_folder, bldg_name)
		idf_name = os.path.join(cur_work_folder, model_name + '.idf')
		print(idf_name)
		if (os.path.isdir(cur_work_folder) and os.path.exists(idf_name)):
			
			idf_name_new = os.path.join(cur_work_folder, model_name + '.idfnew')
			idf_name_origin = os.path.join(cur_work_folder, model_name + '_origin.idf')
			call(["./Updater-9.3.0-9.5.0.sh", idf_name, idf_name_new, idf_name_origin])
			del_list = []
			for filename in os.listdir(cur_work_folder):
				if not filename.endswith(".idf"):	
					del_list.append(cur_work_folder + "/" + filename)
			for filename in del_list:
				os.remove(filename)

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


