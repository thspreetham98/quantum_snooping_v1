import time
from datetime import datetime, timedelta
import pickle
import sys
from qiskit_ibm_provider import IBMProvider
from qiskit.providers import JobStatus

job = None
try:
    job_id = sys.argv[1]
except Exception:
    print('pass job_id as argument')
    print('Usage: python fetch_calibration_data.py [job_id]')
    raise Exception('Wrong usage')


try:
    print('Getting provider...')
    provider = IBMProvider()
    print('fetching job: ', job_id)
    job = provider.backend.retrieve_job(job_id)
except Exception:
    print('Failed to fetch job. Please check the provided jobID')
    sys.exit(-1)

job_status = job.status()
print('Current status of job', job_status)

if job_status in [JobStatus.DONE, JobStatus.CANCELLED, JobStatus.ERROR]:
    print('Job is done executing. Try this script with a job that is in queue.')
    sys.exit(0)


backend = job.backend()
prev_last_update = datetime.min
next_update = datetime.now() - timedelta(minutes=5)

while True:
    current_time = datetime.now()
    if current_time > next_update:
        job_status = job.status()
        backend_properties = backend.properties()
        print("Job status:", job_status, ", Checking.................", end='\r')
        last_update = backend_properties.last_update_date
        if last_update != prev_last_update:
            print('Last Calibrated at:', last_update)
            prev_last_update = last_update
            fname = "pickles/backend_properties/{}_{}.p".format(backend.name, str(last_update.timestamp()))
            print('Saved to: ', fname)
            pickle.dump(backend_properties, open(fname, "wb" ) )
        next_update = current_time + timedelta(minutes=10)
    else:
        time_diff = str(next_update - current_time)
        print("Job status:", job_status, ", Next Attempt in: ", time_diff[0:7], end='\r')
    if job_status in [JobStatus.DONE, JobStatus.CANCELLED, JobStatus.ERROR]:
        break


    time.sleep(1)



