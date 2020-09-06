from apscheduler.schedulers.blocking import BlockingScheduler

print('open')

scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval', seconds=3)
def job_0():
        print('3秒毎に実行')

print('done')
scheduler.start()