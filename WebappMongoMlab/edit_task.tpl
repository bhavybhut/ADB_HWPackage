%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<html>
    <head>
        <title>To-Do Example</title>
        <link type="text/css" href="../mystyle.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <div class="container">
            <h2><a href="/">To-Do List</a></h2>
            <form action="/edit/{{no}}" method="post">
                <div class="form-group row">
                    <div class="col-md-12">
                        <label>Edit the task with ID = {{no}}:</label>
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-md-2">
                        <label>Task:</label>
                    </div>
                    <div class="col-md-10">
                        <input type="text" name="task" value="{{old["task"]}}" size="100%" maxlength="100" class="form-control">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-md-2">
                        <label>Status:</label>
                    </div>
                    <div class="col-md-10">
                        <select name="status" class="form-control">
                            <option>Open</option>
                            <option>Closed</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-md-2">
                    </div>
                    <div class="col-md-10">
                        <input type="submit" name="save" value="save" class="btn btn-primary">
                    </div>
                </div>
            </form>
        </div>
    </body>
</html>