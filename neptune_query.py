from gremlin_python.driver import client
import backoff


def query(tokens):
    
    print(tokens)
    
    token_ls = [x[0] for x in tokens]
    
    print('wss://{}:{}/gremlin'.format(os.environ['neptuneEndpoint'], os.environ['neptunePort']))
    
    client_a = client.Client('wss://{}:{}/gremlin'.format(os.environ['neptuneEndpoint'], os.environ['neptunePort']),'g')
    
    result = []
    
    for token in token_ls:
        
        token = token.strip()
        
        # query 1
        
        query = """
        g.V().hasLabel("Tag").has("name", """ + token + """).out("found in").value("name").toList()
        """
        
    
        result = client_a.submit(query)
        future_results = result.all()
        results_url = future_results.result()
        
        query = """
        g.V().hasLabel("Tag").has("name", """ + token + """).outE("found in").value("confidence").toList()
        """
        
        result = client_a.submit(query)
        future_results = result.all()
        results_confidence = future_results.result()
        
        output = sorted(list(zip(results_url, results_confidence)), key = lambda x: x[1])
        
        result.extend([x[0] for x in output])
        
        print(result)
        
        for url in results_url:      
        
            query = """
            g.V().hasLabel("URL").has("name", """ + url + """).out("links to").value("name").toList()
            """
        
            result = client_a.submit(query)
            future_results = result.all()
            results_url = future_results.result()
            
            
            query = """
            g.V().hasLabel("URL").has("name", """ + url + """).outE("links to").value("confidence").toList()
            """
            
            result = client_a.submit(query)
            future_results = result.all()
            results_confidence = future_results.result()
            
            output = sorted(list(zip(results_url, results_confidence)), key=lambda x: x[1])
            
            result.extend([x[0] for x in output])
            
    client_a.close()
            
    return result