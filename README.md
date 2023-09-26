# Smart support form

This is the code for the blog article "Use Milvus and Airbyte for similarity search on all your data".

<img width="750" alt="Screenshot 2023-09-26 at 16 24 09" src="https://github.com/airbytehq/tutorial-similarity-search/assets/1508364/08257911-e892-47d1-ab5d-361dde143628">


To run the examples, follow these steps:
* Follow the linked article to set up Milvus and Airbyte and sync your data
* `pip install openai pymilvus streamlit`
* `export OPENAI_API_KEY=<your key>`
* `export MILVUS_URL=<your host with protocol>`
* `export MILVUS_TOKEN=<your access token>`
* `streamlit run 1_basic_support_form.py` for the basic form
* `streamlit run 2_open_ticket.py` for adding the duplicate ticket check
* `streamlit run 3_relevant_articles.py` for showing relevant articles from the knowledge base
