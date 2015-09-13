#sparqlwrapper test Chris Pool

from SPARQLWrapper import SPARQLWrapper, JSON

class Sparql:
	
	def __init__(self):
		pass


	def test(self):
		sparql = SPARQLWrapper("http://dbpedia.org/sparql")
		sparql.setQuery("""
		    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
			PREFIX dbpprop: <http://dbpedia.org/property/>
			PREFIX dbres: <http://dbpedia.org/resource/>
		   

		    SELECT ?country ?capital
			WHERE  {
			 ?country a dbpedia-owl:Country .
			
			}
		""")

		# JSON example
		
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		for result in results["results"]["bindings"]:
		    print(result["label"]["value"])






s = Sparql()

s.test()