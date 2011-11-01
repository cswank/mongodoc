from nose.tools import eq_
from doc import doc
from mongodoc import DocDoc

class TestDocDoc(object):

    def setup(self):
        self.md = DocDoc(doc, 'campaigns')

    def test_create(self):
        pass

    def test_text(self):
        eq_(len(self.md._subdocs), 2)
        print 'result:'
        text = self.md.text
        print text
        eq_(text," ________________________________________________________________________________________________________________________________________\n| campaigns                                                                                                                              |\n|________________________________________________________________________________________________________________________________________|\n| _id:                    <class 'bson.objectid.ObjectId'>       ________________________________________________________________________|\n| analysis_complete:                         <type 'bool'>     | trays <list>                                                           ||\n| campaign_name:                          <type 'unicode'>     |________________________________________________________________________||\n| catalyst:                               <type 'unicode'>     | barcodes:            <type 'list'>       ______________________________||\n| emailed_to_lims:                           <type 'bool'>     | glucose_absorbances: <type 'list'>     | rejections                   |||\n| enzyme_load:                            <type 'unicode'>     | glucose_standards:   <type 'list'>     |______________________________|||\n| enzymes:                                <type 'unicode'>     | masses:              <type 'list'>     | glucose: <type 'list'>       |||\n| hydrolysis_temperature:                 <type 'unicode'>     | notes:            <type 'unicode'>     | xylose:  <type 'list'>       |||\n| hydrolysis_time:                        <type 'unicode'>     | plate_number:     <type 'unicode'>     |______________________________|||\n| in_lims:                                   <type 'bool'>     | rejections:          <type 'dict'>                                     ||\n| name:                                   <type 'unicode'>     | xylose_absorbances:  <type 'list'>                                     ||\n| notes:                                  <type 'unicode'>     | xylose_standards:    <type 'list'>                                     ||\n| operator:                               <type 'unicode'>     |________________________________________________________________________||\n| pretreatment_temperature:               <type 'unicode'>                                                                               |\n| pretreatment_time:                      <type 'unicode'>         ______________________________________________________________________|\n| project:                <class 'bson.objectid.ObjectId'>       | results                                                              ||\n| results:                                   <type 'dict'>       |______________________________________________________________________||\n| run_start_date:               <type 'datetime.datetime'>       | data:       <type 'list'>               _____________________________||\n| sample_arrangements_id: <class 'bson.objectid.ObjectId'>       | junk:       <type 'dict'>             | junk                        |||\n| solids:                                 <type 'unicode'>       | rejections: <type 'list'>             |_____________________________|||\n| sop:                                    <type 'unicode'>       |                                       | address: <type 'str'>       |||\n| trays:                                     <type 'list'>       |                                       | first:   <type 'str'>       |||\n|                                                                |                                       | last:    <type 'str'>       |||\n|                                                                |                                       | mood:    <type 'str'>       |||\n|                                                                |                                       |_____________________________|||\n|                                                                |______________________________________________________________________||\n|________________________________________________________________________________________________________________________________________|")

    def test_get_width(self):
        eq_(self.md._get_width(), 136)



    
            
        


