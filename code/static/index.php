<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>UW Events</title>

    <!-- Bootstrap Core CSS -->
    <link href="/static/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href='/static/index.css' rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='http://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/~/about">About UW Events</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="/~/signup">Sign Up</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Header -->
    <header class="intro-header" style="background-image: url('/static/waterloo1.png')">
        <div class="container">
                    <div class="site-heading">
                        <h1>uWaterloo Event Notifications:</h1>
                        <ul class="button">
                            <li class="next">
                                <a href="/~/signup">Sign Up</a>
                            </li>
                        </ul>
                    </div>
                </div>
           
    </header>
    <!-- Main Content -->
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                <div class="post-preview">
                    <a href='https://uwaterloo.ca/events/events'>
                        <h1 class="post-title">
                            Upcoming Events
                        </h1>
                        <br>
                    </a>
                    <hr>
                </div>
    <?php
        include('rss.php');
        $feed_url = 'https://uwaterloo.ca/events/events/events.xml';
        $feedlist = new rss($feed_url);
        $feeds = $feedlist->display(10,"Upcoming Events");
        echo $feeds;
    ?>
            </div>
        </div>
    </div>

    <hr>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <p class="copyright text-muted">Copyright &copy; UW Events 2016</p>
                    <p class="copyright text-muted">Created by: Jonathan Donas, Ryan Newman, Rolina Wu, Neo Chen and Wang Yang</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="/static/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="/static/bootstrap.min.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="/static/uw-events.min.js"></script>

</body>
</html>
