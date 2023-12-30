from airflow import DAG
from airflow.providers.neo4j.operators.neo4j import Neo4jOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='neo4j_schema_implementation',
    default_args=default_args,
    description='DAG to implement the Neo4J schema for arXiv dataset',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Define tasks to create nodes
    create_papers_node = Neo4jOperator(
        task_id='create_papers_node',
        sql="""
            CREATE CONSTRAINT ON (p:Paper) ASSERT p.id IS UNIQUE;
            CREATE (:Paper {id: 'ID', versions: 'versions', update_date: 'update_date', submitter: 'submitter'});
        """,
    )

    create_authors_node = Neo4jOperator(
        task_id='create_authors_node',
        sql="""
            CREATE CONSTRAINT ON (a:Author) ASSERT a.id IS UNIQUE;
            CREATE (:Author {name: 'name', id: 'ID'});
        """,
    )

    create_categories_node = Neo4jOperator(
        task_id='create_categories_node',
        sql="""
            CREATE CONSTRAINT ON (c:Category) ASSERT c.id IS UNIQUE;
            CREATE (:Category {name: 'name', id: 'ID'});
        """,
    )

    create_publications_node = Neo4jOperator(
        task_id='create_publications_node',
        sql="""
            CREATE CONSTRAINT ON (pub:Publication) ASSERT pub.id IS UNIQUE;
            CREATE (:Publication {journal_ref: 'journal_ref', DOI: 'DOI', id: 'ID'});
        """,
    )

    create_details_node = Neo4jOperator(
        task_id='create_details_node',
        sql="""
            CREATE CONSTRAINT ON (d:Detail) ASSERT d.id IS UNIQUE;
            CREATE (:Detail {title: 'title', abstract: 'abstract', comments: 'comments', id: 'ID'});
        """,
    )

    # Define tasks to create relationships
    create_paper_author_relationship = Neo4jOperator(
        task_id='create_paper_author_relationship',
        sql="""
            MATCH (p:Paper), (a:Author)
            WHERE p.id = a.id
            CREATE (p)-[:WAS_WRITTEN_BY]->(a);
        """,
    )

    create_paper_category_relationship = Neo4jOperator(
        task_id='create_paper_category_relationship',
        sql="""
            MATCH (p:Paper), (c:Category)
            WHERE p.id = c.id
            CREATE (p)-[:BELONGS_TO]->(c);
        """,
    )

    create_paper_publication_relationship = Neo4jOperator(
        task_id='create_paper_publication_relationship',
        sql="""
            MATCH (p:Paper), (pub:Publication)
            WHERE p.id = pub.id
            CREATE (p)-[:WAS_PUBLISHED_IN]->(pub);
        """,
    )

    create_detail_paper_relationship = Neo4jOperator(
        task_id='create_detail_paper_relationship',
        sql="""
            MATCH (d:Detail), (p:Paper)
            WHERE d.id = p.id
            CREATE (d)-[:BELONGS_TO]->(p);
        """,
    )

    # Define task dependencies
    create_papers_node >> create_authors_node >> create_categories_node >> create_publications_node >> create_details_node
    create_papers_node >> [create_paper_author_relationship, create_paper_category_relationship, create_paper_publication_relationship]
    create_details_node >> create_detail_paper_relationship
