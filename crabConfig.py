date = '20150108'
job_to_submit = 'PHYS14_DYToEE_20BX25'

from jobs_PHYS14 import jobs

job = jobs[job_to_submit]

from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = job.requestName
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'IIHE.py'
config.JobType.outputFiles = ['outfile.root']

config.section_('Data')
config.Data.inputDataset = job.inputDataset
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
if 'sharper' in job.name:
    config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.publication = True
#config.Data.publishDbsUrl = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
#config.Data.publishDataName = job.publishDataName
config.Data.ignoreLocality = True

config.section_('Site')
config.Site.storageSite = 'T2_BE_IIHE'
if 'sharper' in job.name:
    config.Site.whitelist = ['T2_UK_SGrid_RALPP']

config.section_('User')
config.User.voGroup = 'becms'
