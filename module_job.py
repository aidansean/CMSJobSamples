class job_details:
    def __init__(self, name, inputDataset):
        self.name = name
        self.inputDataset = inputDataset
        self.publishDataName = self.inputDataset.replace('/','__')
        self.requestName = '%s_%s'%(date,self.name)

def add_job(name, DAS_string):
    jobs[name] = job_details(name, DAS_string)
