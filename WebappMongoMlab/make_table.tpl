%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<html>
    <head>
        <title>To-Do Example</title>
        <link type="text/css" href="mystyle.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <div class="container">
          <h2><a href="/">To-Do List</a></h2><br/>
          <form action="/new" method="POST" class="form-inline">
            <div class="form-group">
              <label>Add New Task:</label>
            </div>
            <div class="form-group">
              <input type="text" size="100%" maxlength="100" name="task" class="form-control">
            </div>
            <input type="submit" name="save" value="save" class="btn btn-primary">
          </form>
          <br/>
          <form action="/search" method="POST" class="form-inline">
            <div class="form-group">
              <label>Search Task:</label>
            </div>
            <div class="form-group">
              <input type="text" size="100%" maxlength="100" name="searchtxt" class="form-control">
            </div>
            <input type="submit" name="search" value="search" class="btn btn-primary">
          </form>
          <br/>
          <h4>The open items are as follows:</h4>
          <table class="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Task</th>
                <th>Status</th>
                <th>Edit</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              %for row in rows:
                <tr>
                  <td>{{row["id"]}}</td>
                  <td>{{row["task"]}}</td>
                  <td>{{row["status"]}}</td>
                  <td><a href="/edit/{{row["id"]}}">Edit</a></td>
                  <td><a href="/delete/{{row["id"]}}">Delete</a></td>
                </tr>
              %end
            </tbody>
          </table>
          <br/>
          <h4>The closed items are as follows:</h4>
          <table class="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Task</th>
                <th>Status</th>
                <th>Edit</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              %for row in closed:
                <tr>
                    <td>{{row["id"]}}</td>
                    <td>{{row["task"]}}</td>
                    <td>{{row["status"]}}</td>
                    <td><a href="/edit/{{row["id"]}}">Edit</a></td>
                    <td><a href="/delete/{{row["id"]}}">Delete</a></td>
                </tr>
              %end
            </tbody>
          </table>
    </body>
</html>


