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
        eq_(text, " ________________________________________________________________________________________________________________________________________\n| campaigns                                                                                                                              |\n|________________________________________________________________________________________________________________________________________|\n| run_start_date:               <type 'datetime.datetime'>       ________________________________________________________________________|\n| enzyme_load:                            <type 'unicode'>     | trays <list>                                                           ||\n| analysis_complete:                         <type 'bool'>     |________________________________________________________________________||\n| sop:                                    <type 'unicode'>     | plate_number:     <type 'unicode'>       ______________________________||\n| pretreatment_time:                      <type 'unicode'>     | xylose_standards:    <type 'list'>     | rejections                   |||\n| operator:                               <type 'unicode'>     | glucose_absorbances: <type 'list'>     |______________________________|||\n| campaign_name:                          <type 'unicode'>     | rejections:          <type 'dict'>     | xylose:  <type 'list'>       |||\n| trays:                                     <type 'list'>     | notes:            <type 'unicode'>     | glucose: <type 'list'>       |||\n| in_lims:                                   <type 'bool'>     | xylose_absorbances:  <type 'list'>     |______________________________|||\n| emailed_to_lims:                           <type 'bool'>     | glucose_standards:   <type 'list'>                                     ||\n| hydrolysis_time:                        <type 'unicode'>     | masses:              <type 'list'>                                     ||\n| hydrolysis_temperature:                 <type 'unicode'>     | barcodes:            <type 'list'>                                     ||\n| results:                                   <type 'dict'>     |________________________________________________________________________||\n| catalyst:                               <type 'unicode'>                                                                               |\n| sample_arrangements_id: <class 'bson.objectid.ObjectId'>         ______________________________________________________________________|\n| name:                                   <type 'unicode'>       | results                                                              ||\n| pretreatment_temperature:               <type 'unicode'>       |______________________________________________________________________||\n| enzymes:                                <type 'unicode'>       | junk:       <type 'dict'>               _____________________________||\n| notes:                                  <type 'unicode'>       | data:       <type 'list'>             | junk                        |||\n| project:                <class 'bson.objectid.ObjectId'>       | rejections: <type 'list'>             |_____________________________|||\n| solids:                                 <type 'unicode'>       |                                       | address: <type 'str'>       |||\n| _id:                    <class 'bson.objectid.ObjectId'>       |                                       | last:    <type 'str'>       |||\n|                                                                |                                       | mood:    <type 'str'>       |||\n|                                                                |                                       | first:   <type 'str'>       |||\n|                                                                |                                       |_____________________________|||\n|                                                                |______________________________________________________________________||\n|________________________________________________________________________________________________________________________________________|")

    def test_get_width(self):
        eq_(self.md._get_width(), 136)



    
            
        


