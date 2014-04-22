import json

class GetYearsHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            response = get_years(self.get_argument("dataset_id"))
            result = {'status':'success', 'response': response}
            kk = tornado.escape.json_encode(result)
            kk = wrap_callback(self, kk)
            self.write(kk)
        except Exception, e:
            print >> sys.stderr, "Error occured:\n%s" % format_exc()
            self.write(json.dumps({'status': 'fail', 'error': "Error occured:\n%s" % format_exc()}))

def get_years (dataset_id):
    dates=[]
    years=[]
    conn = condb()
    cur = conn.cursor()
    data = {'dataset_id':dataset_id}
    cur.execute("SELECT layers.start_time FROM layers, datasets WHERE (layers.dataset_id=datasets.id) AND (datasets.business_id=%(dataset_id)s)",data)
    for row in cur.fetchall():
        dates.append(row[0])
    date=""
    for date in dates:
        year = int(date.year)
        if not year in years:
            years.append(year)
    conn.close()
    years.sort()
    return years

def main(db_fn=None):
    tornado.options.parse_command_line()
    application = tornado.web.Application([
    (r"/get_datasets", GetDatasetsHandler),
    (r"/get_years", GetYearsHandler),
)
