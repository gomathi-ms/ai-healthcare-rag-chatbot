from langchain_community.graphs import Neo4jGraph

def connect_graph():

    graph = Neo4jGraph(
        url="bolt://localhost:7687",
        username="neo4j",
        password="password"
    )

    return graph
