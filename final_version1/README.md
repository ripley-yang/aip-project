This project has several repositories:

The "static" repository contains "js" folder and "style" folder. The js folder is used when we need to use tree table in the result page. While the style folder contains several css files. Those css files control the web pages' colors, layout, and fonts. 

Then, there is a "templates" repository. The layout.html file is the layout of index page and the reempty page. And the reslayout.html file is  the layout of other result pages.

1. Index.html file is the searching page.
2. reempty.html file is the page that will be shown when there is no search results returned from google custom search engine.
3. result.html is a page with tree table function and will be displayed when all the input data is found from the google custom search engine.
4. results2.html is a page with tree table function and will be dispayed when some of the input information could not be found.

The app.py is the back-end of this project. We use the Flask framework to design this project.

In the app.py file, the function "google_search(search_term)" is to connect with the Google custom search engine.

The index() function is to call the searching page.

the @app.route is to react the form fuction that writes in index.html file.

the user() function will happen after clients click the search button in the searching page. 


